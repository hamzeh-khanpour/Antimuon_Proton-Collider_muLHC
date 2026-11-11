"""Audit job archives and assemble direct cross-section tables."""
import csv
import json
import math
import re
import shutil
import tarfile
import tempfile
from pathlib import Path

import card_utils
from scan_grid import CHANNEL_IDS, EXPERIMENTAL_INTERVALS, jobs, baseline_rows


POINT_FIELDS = ('energy_id', 'sqrts_GeV', 'process_id', 'polarization_percent',
                'kappa3', 'sigma_fb', 'sigma_mc_err_fb', 'n_events',
                'event_shortfall', 'seed', 'job_id', 'source')
TOTAL_FIELDS = ('energy_id', 'sqrts_GeV', 'polarization_percent', 'kappa3',
                'sigma_CC_fb', 'sigma_NC_fb', 'sigma_fb', 'sigma_mc_err_fb')


def write_job_table(file):
    points = jobs()
    writer = csv.DictWriter(file, fieldnames=list(points[0]))
    writer.writeheader()
    writer.writerows(points)


def archive_result(archive, job, manifest_sha, run_dir):
    # Lazy import so the worker entry point and collector share the same checks.
    import scan
    with tarfile.open(archive, 'r:gz') as t, tempfile.TemporaryDirectory(prefix='kappa_collect_') as tmp:
        members = {}
        for member in t.getmembers():
            if member.name in members:
                raise ValueError('Duplicate archive member: '+member.name)
            members[member.name] = member

        def member_file(name):
            m = members.get(name)
            if m is None or not m.isfile():
                raise ValueError('Missing or nonregular evidence: '+name)
            return t.extractfile(m)

        with member_file('result.json') as f:
            record = json.load(f)
        if record.get('status') != 'GENERATED':
            raise ValueError(record.get('error', 'Worker did not produce a valid result'))
        if any(record.get(k) != v for k, v in job.items()):
            raise ValueError('Job metadata differs from scan manifest')
        if (record.get('run_manifest_sha256') != manifest_sha
                or record.get('actual_seed_verified_from_log') != job['seed']):
            raise ValueError('Archive manifest or seed differs from declared job')
        with member_file('run_manifest.json') as f:
            if f.read() != (run_dir/'run_manifest.json').read_bytes():
                raise ValueError('Embedded manifest mismatch')
        for name in ('snapshots/pre_param_card.dat', 'process/Cards/param_card.dat'):
            with member_file(name) as f:
                scan.validate_parameter_text(f.read().decode(), job['kappa3'])
        with member_file('snapshots/pre_run_card.dat') as f:
            actual = card_utils.parse(f.read().decode())
        expected = card_utils.parse((run_dir/job['run_card_file']).read_text())
        updates = card_utils.desired(job['electron_GeV'], job['muplus_GeV'], job['polarization_percent'],
                                     job['nevents'], job['seed'])
        expected.update({k: v for k, v in updates.items() if k in expected})
        if set(actual) != set(expected) or any(not card_utils._equal(v, actual[k])
                                                for k, v in expected.items()):
            raise ValueError('Archived run card differs from the reference settings')
        name = record['lhe_file']
        if not re.fullmatch(r'process/Events/run_\d+/unweighted_events\.lhe(?:\.gz)?', name):
            raise ValueError('Unexpected LHE member path')
        lhe = Path(tmp)/Path(name).name
        with member_file(name) as src, lhe.open('wb') as dst:
            shutil.copyfileobj(src, dst)
        if scan.sha(lhe) != record['lhe_sha256']:
            raise ValueError('Archived LHE checksum mismatch')
        if scan.read_lhe_cards(lhe, job) != record['lhe_parameters']:
            raise ValueError('Recorded LHE cards and archive disagree')
        readback = scan.read_lhe(lhe, job)
        if any(record.get(k) != v for k, v in readback.items()):
            raise ValueError('Recorded cross section and archived LHE disagree')
    return {**{k: record[k] for k in POINT_FIELDS if k != 'source'},
            'source': 'direct_HHVBF_integration'}


def sum_channels(points):
    rates = {(r['energy_id'], r['process_id'], r['polarization_percent'], r['kappa3']): r
             for r in points}
    totals = []
    for eid, pol, k in sorted({(r['energy_id'], r['polarization_percent'], r['kappa3'])
                               for r in points}):
        cc, nc = (rates.get((eid, c, pol, k)) for c in CHANNEL_IDS)
        if cc is None or nc is None:
            continue
        totals.append(dict(energy_id=eid, sqrts_GeV=cc['sqrts_GeV'], polarization_percent=pol,
                           kappa3=k, sigma_CC_fb=cc['sigma_fb'], sigma_NC_fb=nc['sigma_fb'],
                           sigma_fb=cc['sigma_fb']+nc['sigma_fb'],
                           sigma_mc_err_fb=math.hypot(cc['sigma_mc_err_fb'], nc['sigma_mc_err_fb'])))
    return totals


def write_csv(path, rows, fields):
    with path.open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def collect():
    import scan
    root = scan.ROOT
    scan.verified_manifest()
    manifest_sha = scan.sha(root/'run_manifest.json')
    planned = {j['job_id']: j for j in jobs()}
    points = baseline_rows(root)
    baseline_count = len(points)
    failed, accepted, duplicates, unexpected = [], {}, [], []
    for archive in sorted((root/'results').glob('*/*.tar.gz')):
        archive_name = archive.relative_to(root).as_posix()
        match = re.fullmatch(r'(.+)\.(\d+)\.tar\.gz', archive.name)
        jid = match[1] if match else ''
        if jid not in planned:
            unexpected.append(archive_name)
            continue
        try:
            row = archive_result(archive, planned[jid], manifest_sha, root)
        except Exception as ex:
            failed.append(dict(job_id=jid, archive=archive_name, error=str(ex)))
            continue
        if jid in accepted:
            duplicates.append(dict(job_id=jid, archive=archive_name,
                                   other_archive=accepted[jid][1]))
        else:
            accepted[jid] = row, archive_name
    points.extend(row for row, _ in accepted.values())
    points.sort(key=lambda p: (p['energy_id'], p['process_id'], p['polarization_percent'], p['kappa3']))
    totals = sum_channels(points)
    missing = sorted(set(planned)-set(accepted))
    complete = not (missing or duplicates or unexpected)
    report = dict(status='COMPLETE' if complete else 'INCOMPLETE_OR_REVIEW_REQUIRED',
                  run_manifest_sha256=manifest_sha, expected_new_jobs=len(planned),
                  validated_new_jobs=len(accepted), reused_unpolarized_points=baseline_count,
                  observed_95cl_intervals=EXPERIMENTAL_INTERVALS,
                  missing_or_failed_jobs=missing, rejected_attempts=failed,
                  duplicate_valid_attempts=duplicates, unexpected_archives=unexpected,
                  event_shortfalls=[r['job_id'] for r in points if r['event_shortfall']],
                  accepted_archives={jid: path for jid, (_, path) in accepted.items()},
                  points=points, totals=totals)
    reports = root/'reports'
    reports.mkdir(exist_ok=True)
    write_csv(reports/'scan_points.csv', points, POINT_FIELDS)
    write_csv(reports/'scan_totals.csv', totals, TOTAL_FIELDS)
    scan.dump(report, reports/'scan_report.json')
    print(f'{report["status"]}: {len(accepted)}/{len(planned)} new jobs verified, {baseline_count} unpolarized points reused.')
    for jid in missing[:12]:
        print('MISSING OR FAILED:', jid)
    if len(missing) > 12:
        print('See the report for the remaining missing job IDs.')
    for item in failed:
        print('REJECTED:', item['archive'], item['error'])
    for item in duplicates:
        print('DUPLICATE VALID ATTEMPT:', item['archive'], item['other_archive'])
    for name in unexpected:
        print('UNEXPECTED ARCHIVE:', name)
    if report['event_shortfalls']:
        print('Event-count shortfalls recorded in the report:', len(report['event_shortfalls']))
    print('REPORT:', reports/'scan_report.json')
    return 0 if complete else 2
