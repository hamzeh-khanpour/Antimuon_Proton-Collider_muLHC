#!/usr/bin/env python3
"""FCC-mue unpolarized kappa3 scan using the validated HHVBF MadEvent workflow."""
import argparse
import collections
import gzip
import hashlib
import io
import json
import math
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
import traceback

import card_utils
from scan_grid import ENERGIES, PACKAGE, jobs, sm_rows

ROOT = Path(__file__).resolve().parent
PREPARED_PARAM_SHA = '22a08b9317018acaa51ea7098c7a8d60e2b775c050cd44e0d798e40603f8737b'
PARAM_SHA = '1782870ce8b7f2744f8607e646fdaf77ce99c64175821c2a8e2e5280f995cbfe'
CHANNELS = {
    'CC_HH': ('e- mu+ > ve vm~ h h', [12, -14, 25, 25]),
    'NC_HH': ('e- mu+ > e- mu+ h h', [11, -13, 25, 25]),
}
COMMANDS = {p: 'generate '+v[0]+' QCD=0 QED=4 CV=2 C2V=1 C3=1'
            for p, v in CHANNELS.items()}


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for b in iter(lambda: f.read(1024*1024), b''):
            h.update(b)
    return h.hexdigest()


def dump(obj, path):
    Path(path).write_text(json.dumps(obj, indent=2, sort_keys=True)+'\n')


def parameter_values(text):
    result, block = {}, None
    for line in text.splitlines():
        a = line.split('#', 1)[0].split()
        if not a:
            continue
        if a[0].lower() == 'block':
            block = a[1].lower()
            continue
        if a[0].lower() == 'decay':
            key, value = ('decay', int(a[1])), a[2]
            block = None
        elif block is not None:
            key, value = (block, *map(int, a[:-1])), a[-1]
        else:
            continue
        if key in result:
            raise ValueError('Duplicate parameter '+str(key))
        result[key] = float(value.replace('D', 'E').replace('d', 'e'))
        if not math.isfinite(result[key]):
            raise ValueError('Nonfinite parameter '+str(key))
    return result


def validate_parameter_text(text, kappa3):
    reference = ROOT/'param_card_SM.dat'
    if sha(reference) != PARAM_SHA:
        raise ValueError('Bundled SM parameter card checksum changed')
    wanted = parameter_values(reference.read_text())
    actual = parameter_values(text)
    wanted['new', 3] = kappa3
    mz = wanted['mass', 23]
    aew = 1 / wanted['sminputs', 1]
    gf = wanted['sminputs', 2]
    mw = math.sqrt(mz**2/2 + math.sqrt(mz**4/4 - aew*math.pi*mz**2/(gf*math.sqrt(2))))
    if not math.isclose(wanted['mass', 24], mw, rel_tol=1e-12):
        raise ValueError('Reference W mass does not match the UFO electroweak relation')
    bad = {str(k): (v, actual.get(k)) for k, v in wanted.items()
           if k not in actual or not math.isclose(v, actual[k], rel_tol=1e-10, abs_tol=1e-14)}
    if bad:
        raise ValueError('Runtime parameter mismatch: '+str(bad))
    return {'CV': actual['new', 1], 'C2V': actual['new', 2], 'C3': actual['new', 3],
            'MW_GeV': actual['mass', 24],
            'sm_reference_sha256': PARAM_SHA}


def validate_parameters(path, kappa3=1.0):
    return dict(validate_parameter_text(path.read_text(), kappa3), actual_file_sha256=sha(path))


def read_lhe_cards(path, job):
    """Check the cards recorded by MadEvent in the generated LHE header."""
    opener = gzip.open if path.suffix == '.gz' else open
    header = []
    with opener(path, 'rt') as f:
        for line in f:
            if line.strip() in ('<init>', '<event>'):
                break
            header.append(line)
    text = ''.join(header)

    def card(tag):
        parts = re.findall(rf'<{tag}>(.*?)</{tag}>', text, re.I | re.S)
        if len(parts) != 1:
            raise ValueError(f'Expected one {tag} block in LHE header')
        return parts[0].replace('<![CDATA[', '').replace(']]>', '')

    run = card_utils.parse(card('MGRunCard'))
    expected = {'lpp1': '0', 'lpp2': '0', 'polbeam1': '0', 'polbeam2': '0',
                'ebeam1': str(job['electron_GeV']), 'ebeam2': str(job['muplus_GeV']),
                'iseed': str(job['seed'])}
    if any(key not in run or not card_utils._equal(value, run[key])
           for key, value in expected.items()):
        raise ValueError('LHE run card differs from declared beams, polarization or seed')
    return validate_parameter_text(card('slha'), job['kappa3'])


def reference_rows():
    rows = json.loads((ROOT/'reference/SM_benchmarks.json').read_text())
    if len(rows) != 4:
        raise ValueError('Expected four historical reference rows')
    for row in rows:
        if sha(ROOT/row['run_card_file']) != row['run_card_sha256']:
            raise ValueError('Historical reference run card changed')
    lookup = {(r['energy_id'], r['process_id']): r for r in rows}
    if set(lookup) != {(e, p) for e in ENERGIES for p in CHANNELS}:
        raise ValueError('Historical reference grid mismatch')
    for j in jobs():
        r = lookup[j['energy_id'], j['process_id']]
        if j['seed'] == r['seed']:
            raise ValueError('Pilot seed must differ from historical seed')
        if r['polarization_percent'] != 0 or r['n_events'] != 30000:
            raise ValueError('Reference configuration mismatch')
    return lookup


def protected_files():
    return ['scan.py', 'card_utils.py', 'worker.sh', 'param_card_SM.dat',
            'scan_grid.py', 'scan_results.py', 'reference/SM_benchmarks.json',
            'reference/SM_closure_report.json'] + sorted({j['run_card_file'] for j in jobs()})


def verified_manifest():
    m = json.loads((ROOT/'run_manifest.json').read_text())
    if m['status'] != 'TEMPLATES_READY_NOT_INTEGRATED' or m['jobs'] != jobs():
        raise ValueError('Manifest configuration is not this coupling scan')
    if set(m['files']) != set(protected_files()):
        raise ValueError('Manifest protected-file list mismatch')
    for f, expected in m['files'].items():
        if sha(ROOT/f) != expected:
            raise ValueError('Prepared scan file changed: '+f)
    reference_rows()
    return m


def check_process_card(path, channel):
    text = re.sub(r'\\\r?\n', '', path.read_text())
    lines = [s.split('#', 1)[0].strip() for s in text.splitlines()]
    generated = [s for s in lines if s.startswith('generate ') or s.startswith('add process ')]
    if generated != [COMMANDS[channel]]:
        raise ValueError('Unexpected process command(s): '+str(generated))
    if 'import model HHVBF_UFO_FCCmue-fccmue' not in lines:
        raise ValueError('Expected named matched model and fccmue restriction')


def export_evidence(proc, channel):
    """Inspect the generated amplitude, independently of command history."""
    subdirs = [p for p in (proc/'SubProcesses').glob('P*') if p.is_dir()]
    if len(subdirs) != 1:
        raise ValueError('Expected one ungrouped subprocess directory: '+channel)
    sub = subdirs[0]
    candidates = list(sub.glob('template_matrix*.f')) or list(sub.glob('matrix*.f'))
    if not candidates:
        raise ValueError('No exported Fortran matrix source found: '+channel)
    expected_orders = {'QCD=0', 'QED<=4', 'CV<=2', 'C2V<=1', 'C3<=1'}
    evidence = {}
    for p in candidates:
        text = p.read_text()
        matches = sorted(set(re.findall(r'^C\s+Process:\s*(.*?)\s*$', text, re.M)))
        if len(matches) != 1:
            raise ValueError('Ambiguous generated matrix process header: '+str(p))
        tokens = matches[0].split()
        base = CHANNELS[channel][0].split()
        if tokens[:len(base)] != base or set(tokens[len(base):]) != expected_orders:
            raise ValueError('Generated matrix process/order mismatch: '+matches[0])
        if not re.search(r'PARAMETER\s*\(\s*NGRAPHS\s*=\s*4\s*\)', text, re.I):
            raise ValueError('Generated matrix does not contain four diagrams')
        evidence[str(p.relative_to(proc))] = sha(p)
    coupling = proc/'Source/MODEL/couplings1.f'
    compact = re.sub(r'\s+', '', coupling.read_text()).upper()
    if 'GC_89=-6.000000D+00*MDL_C3*MDL_COMPLEXI*MDL_LAM*MDL_VEV' not in compact:
        raise ValueError('Exported trilinear coupling is not the audited C3 interaction')
    evidence[str(coupling.relative_to(proc))] = sha(coupling)
    return evidence


def history_for_template(proc, channel):
    """Repair missing exec_cmd history only in a transferred snapshot."""
    original = (proc/'Cards/proc_card_mg5.dat').read_text()
    try:
        check_process_card(proc/'Cards/proc_card_mg5.dat', channel)
        return original, 'ORIGINAL_HISTORY_VERIFIED'
    except ValueError:
        # prepare_model.py v1 used exec_cmd(precmd=False). MG5 then omits the
        # import/generate history despite a correct exported matrix. Never
        # repair contradictory process/model commands: those need investigation.
        active = [s.split('#', 1)[0].strip() for s in original.splitlines()]
        if any(s.startswith(('generate ', 'add process ', 'import model ')) for s in active):
            raise ValueError('Contradictory existing process history; refusing to rewrite it')
        text = '\n'.join([
            '# FCCmue command history reconstructed from preparation_manifest.json',
            '# and independently checked exported matrix headers/coupling source.',
            '# Original exported history preserved in FCCMUE_ORIGINAL_proc_card_mg5.dat.',
            'set automatic_html_opening False', 'set group_subprocesses False',
            'set gauge unitary', 'import model HHVBF_UFO_FCCmue-fccmue',
            COMMANDS[channel], 'output '+str(proc), ''])
        return text, 'HISTORY_RECONSTRUCTED_FROM_MANIFEST_AND_GENERATED_SOURCES'


def add_text(tar, name, text):
    data = text.encode()
    info = tarfile.TarInfo(name)
    info.size = len(data)
    info.mode = 0o644
    tar.addfile(info, io.BytesIO(data))


def prepare(args):
    """Package existing CERN exports. Never regenerates or launches a process."""
    if (ROOT/'run_manifest.json').exists() or (ROOT/'templates').exists():
        raise ValueError('Scan already prepared or partial output exists; preserving all files')
    source = Path(args.prepared).expanduser().resolve()
    manifest_path = source/'preparation_manifest.json'
    original = json.loads(manifest_path.read_text())
    if (original['status'] != 'PREPARED_NOT_RATE_VALIDATED'
            or 'version = 3.6.4' not in original['mg5_version']
            or original['restriction'] != 'fccmue' or original['gauge'] != 'unitary'
            or original['runtime_param_card_sha256'] != PREPARED_PARAM_SHA):
        raise ValueError('CERN preparation manifest failed the expected model/version/card checks')
    channels = {c['channel']: c for c in original['channels']}
    if set(channels) != set(CHANNELS) or len(original['channels']) != 2:
        raise ValueError('Expected exactly CC_HH and NC_HH in preparation manifest')
    reference_rows()
    sm_rows(ROOT)
    validate_parameters(ROOT/'param_card_SM.dat')
    audit = {}
    with tempfile.TemporaryDirectory(prefix='scan_staging_', dir=ROOT) as tmp:
        td = Path(tmp)
        for channel in CHANNELS:
            c = channels[channel]
            proc = source/channel
            if c['diagram_counts'] != [4] or c['command'] != COMMANDS[channel]:
                raise ValueError('Four-diagram process manifest mismatch: '+channel)
            if Path(c['output']).resolve() != proc.resolve():
                raise ValueError('Manifest output directory differs from supplied preparation')
            for rel in ['bin/generate_events', 'Cards/run_card.dat', 'Cards/param_card.dat',
                        'Cards/proc_card_mg5.dat']:
                if not (proc/rel).is_file():
                    raise ValueError('Missing MadEvent export file: '+str(proc/rel))
            if sha(proc/'Cards/param_card.dat') != PREPARED_PARAM_SHA:
                raise ValueError('Prepared SM runtime card changed: '+channel)
            evidence = export_evidence(proc, channel)
            history, history_status = history_for_template(proc, channel)
            parsed = card_utils.parse((proc/'Cards/run_card.dat').read_text())
            if set(card_utils.REQUIRED)-set(parsed):
                raise ValueError('Prepared run card lacks essential beam/seed fields')
            if any((proc/'Events').glob('run_*')):
                raise ValueError('Preparation already contains runs; preserve it and investigate')
            # Resolve links while preparing, then archive regular files only. The
            # worker does not need the original EOS/AFS model installation.
            for p in proc.rglob('*'):
                target = p.resolve(strict=True)
                if proc.resolve() not in target.parents and target != proc.resolve():
                    raise ValueError('Export contains external dependency: '+str(p))
                if not (p.is_file() or p.is_dir()):
                    raise ValueError('Unsupported export file type: '+str(p))
            archive = td/(channel+'.tar.gz')
            export_audit = {'history_status': history_status, 'command': COMMANDS[channel],
                            'generated_source_sha256': evidence,
                            'original_history_sha256': sha(proc/'Cards/proc_card_mg5.dat'),
                            'note': 'Only transferred history metadata may be reconstructed. Generated amplitude source is unchanged.'}
            with tarfile.open(archive, 'w:gz', dereference=True) as t:
                def keep(info):
                    if '__pycache__' in Path(info.name).parts or info.name == 'process/Cards/proc_card_mg5.dat':
                        return None
                    return info
                t.add(proc, arcname='process', filter=keep)
                add_text(t, 'process/Cards/proc_card_mg5.dat', history)
                add_text(t, 'process/FCCMUE_ORIGINAL_proc_card_mg5.dat',
                         (proc/'Cards/proc_card_mg5.dat').read_text())
                add_text(t, 'process/FCCMUE_EXPORT_AUDIT.json', json.dumps(export_audit, indent=2)+'\n')
            audit[channel] = {'archive_sha256': sha(archive), 'diagram_counts': [4],
                              'command': COMMANDS[channel], 'source': str(proc),
                              'export_audit': export_audit,
                              'generated_run_card_sha256': sha(proc/'Cards/run_card.dat'),
                              'note': 'Worker replaces default run card with archived historical run card.'}
        (td/'archives').mkdir()
        for channel in CHANNELS:
            shutil.move(str(td/(channel+'.tar.gz')), td/'archives'/ (channel+'.tar.gz'))
        shutil.move(str(td/'archives'), ROOT/'templates')
    m = {'status': 'TEMPLATES_READY_NOT_INTEGRATED', 'package': PACKAGE,
         'mg5_version': original['mg5_version'], 'source_preparation': original,
         'runtime_param_card_sha256': PARAM_SHA,
         'source_preparation_manifest_sha256': sha(manifest_path), 'templates': audit,
         'files': {f: sha(ROOT/f) for f in protected_files()}, 'jobs': jobs()}
    dump(m, ROOT/'run_manifest.json')
    print(f'READY: two transferred templates and {len(m["jobs"])} new scan jobs.')
    print('No integration, event generation or Condor submission performed.')


def unpack_regular_archive(archive, dest):
    with tarfile.open(archive, 'r:gz') as t:
        seen = set()
        for p in t.getmembers():
            name = Path(p.name)
            if (name.is_absolute() or '..' in name.parts or not name.parts
                    or name.parts[0] != 'process' or not (p.isfile() or p.isdir())
                    or p.name in seen):
                raise ValueError('Unsafe/duplicate template member: '+p.name)
            seen.add(p.name)
        if (dest/'process').exists():
            raise ValueError('Scratch process already exists; refusing to mix runs')
        t.extractall(dest)


def configure_me(proc):
    cfg = proc/'Cards/me5_configuration.txt'
    lines = cfg.read_text().splitlines() if cfg.exists() else []
    lines = [x for x in lines if not re.match(r'^\s*(run_mode|nb_core|automatic_html_opening)\s*=', x)]
    cfg.write_text('\n'.join(lines+['run_mode = 0', 'nb_core = 1', 'automatic_html_opening = False'])+'\n')
    # Defaults ending in _default.dat remain available, but active analysis,
    # shower and detector cards must not trigger unwanted additional stages.
    for p in (proc/'Cards').iterdir():
        if p.is_file() and not p.name.endswith('_default.dat') and (
                p.name.startswith('madanalysis5_') or p.name in (
                'pythia_card.dat', 'pythia8_card.dat', 'delphes_card.dat',
                'pgs_card.dat', 'rivet_card.dat', 'madspin_card.dat', 'reweight_card.dat')):
            p.unlink()


def read_lhe(path, job):
    """Stream all events; validate topology, beams, normalization and count."""
    expected = collections.Counter(CHANNELS[job['process_id']][1])
    init, event, weights, count = [], None, [], 0
    in_init, seen_init, closed = False, False, False
    opener = gzip.open if str(path).endswith('.gz') else open
    with opener(path, 'rt') as f:
        for line in f:
            s = line.strip()
            if s == '<init>':
                if seen_init:
                    raise ValueError('Duplicate init block')
                in_init = seen_init = True
            elif s == '</init>':
                in_init = False
            elif s == '<event>':
                if event is not None:
                    raise ValueError('Nested or unterminated event')
                event = []
            elif s == '</event>':
                if not event or len(event[0]) < 3:
                    raise ValueError('Empty/truncated event')
                npart = int(event[0][0])
                w = float(event[0][2].replace('D', 'E'))
                if not math.isfinite(w) or w <= 0 or len(event) < npart+1:
                    raise ValueError('Invalid weight or truncated particle list')
                particles = event[1:npart+1]
                final = collections.Counter(int(r[0]) for r in particles if int(r[1]) == 1)
                incoming = collections.Counter(int(r[0]) for r in particles if int(r[1]) == -1)
                if final != expected or incoming != collections.Counter([11, -13]):
                    raise ValueError('Incorrect particle topology in event '+str(count+1))
                weights.append(w)
                count += 1
                event = None
            elif s == '</LesHouchesEvents>':
                closed = True
            elif s and not s.startswith(('#', '<')):
                if in_init:
                    init.append(s.split('#', 1)[0].split())
                elif event is not None:
                    event.append(s.split())
    if event is not None or in_init or not closed or len(init) != 2 or len(init[0]) < 10:
        raise ValueError('Malformed/incomplete LHE file or unexpected subprocess count')
    h = init[0]
    if (int(h[0]), int(h[1])) != (11, -13) or int(h[9]) != 1:
        raise ValueError('Wrong LHE beam IDs or NPRUP')
    e1, e2 = map(float, h[2:4])
    if not (math.isclose(e1, job['electron_GeV'], rel_tol=0, abs_tol=1e-6)
            and math.isclose(e2, job['muplus_GeV'], rel_tol=0, abs_tol=1e-6)):
        raise ValueError('Wrong LHE beam energies')
    xs, err, xmax, lpr = [float(x.replace('D', 'E')) for x in init[1][:4]]
    if not all(math.isfinite(x) for x in [xs, err, xmax, lpr]) or xs <= 0 or err <= 0:
        raise ValueError('Invalid LHE normalization')
    convention = int(h[8])
    if convention == -4:
        target, tol = xs, .005
    elif convention == 3:
        target, tol = 1.0, 1e-6
    else:
        raise ValueError('Unsupported LHE IDWTUP '+str(convention))
    if any(not math.isclose(w, target, rel_tol=tol, abs_tol=1e-14) for w in weights):
        raise ValueError('LHE weights inconsistent with declared unweighting convention')
    if count == 0:
        raise ValueError('Final LHE contains no events')
    return dict(sigma_fb=1000*xs, sigma_mc_err_fb=1000*err, n_events=count,
                event_shortfall=max(0, job['nevents']-count),
                idwtup=convention, beam_ids=[11, -13], beam_energies_GeV=[e1, e2],
                normalization='XSECUP in pb converted once to fb; no branching factor')


def archive_output(root):
    paths = [root/x for x in ['result.json', 'exception.txt', 'run.log',
             'run_card_audit.json', 'run_manifest.json', 'snapshots']]
    proc = root/'process'
    if proc.exists():
        paths += [proc/'Cards', proc/'SubProcesses/randinit',
                  proc/'FCCMUE_ORIGINAL_proc_card_mg5.dat', proc/'FCCMUE_EXPORT_AUDIT.json',
                  proc/'error']
        paths.extend(proc.glob('*_debug.log'))
        for p in (proc/'Events').glob('run_*/*'):
            if p.is_file() and (p.name.endswith(('.lhe', '.lhe.gz', '.log', 'banner.txt'))):
                paths.append(p)
    with tarfile.open(root/'job_output.tar.gz', 'w:gz', dereference=True) as t:
        for p in paths:
            if p.exists():
                t.add(p, arcname=str(p.relative_to(root)))


def worker(args):
    root = Path.cwd()
    record = {'job_id': args.job_id, 'status': 'FAILED', 'package': PACKAGE}
    error = None
    try:
        m = verified_manifest()
        lookup = {j['job_id']: j for j in jobs()}
        if args.job_id not in lookup:
            raise ValueError('Unknown scan job ID')
        j = lookup[args.job_id]
        record.update(j)
        record['run_manifest_sha256'] = sha(ROOT/'run_manifest.json')
        record['python_version'] = sys.version
        record['gfortran'] = shutil.which('gfortran')
        archive = root/j['archive']
        if sha(archive) != m['templates'][j['process_id']]['archive_sha256']:
            raise ValueError('Transferred template checksum mismatch')
        unpack_regular_archive(archive, root)
        proc = root/'process'
        check_process_card(proc/'Cards/proc_card_mg5.dat', j['process_id'])
        if sha(proc/'Cards/param_card.dat') != PREPARED_PARAM_SHA:
            raise ValueError('Unexpected input parameter card in transferred template')
        snapshot = root/'snapshots'
        snapshot.mkdir()
        shutil.copy2(proc/'Cards/run_card.dat', snapshot/'run_card_generated_default.dat')
        # Reuse the exact archived successful run settings rather than new UFO
        # defaults. Only the audited job-specific beam/event/seed settings vary.
        shutil.copy2(ROOT/j['run_card_file'], proc/'Cards/run_card.dat')
        install_runtime_card(proc/'Cards/param_card.dat', j['kappa3'])
        if (proc/'Cards/param_card_default.dat').exists():
            shutil.copy2(proc/'Cards/param_card.dat', proc/'Cards/param_card_default.dat')
        a = card_utils.configure(proc/'Cards/run_card.dat', j['electron_GeV'],
                                 j['muplus_GeV'], 0, j['nevents'], j['seed'], 125.0)
        a['parameters'] = validate_parameters(proc/'Cards/param_card.dat', j['kappa3'])
        a['reference_run_card_sha256'] = sha(ROOT/j['run_card_file'])
        for name in ['run_card.dat', 'param_card.dat', 'proc_card_mg5.dat']:
            shutil.copy2(proc/'Cards'/name, snapshot/('pre_'+name))
        configure_me(proc)
        dump(a, root/'run_card_audit.json')
        with (root/'run.log').open('w') as f:
            ret = subprocess.run([sys.executable, str(proc/'bin/generate_events'), '-f'],
                                 cwd=proc, stdout=f, stderr=subprocess.STDOUT)
        if ret.returncode:
            raise RuntimeError('MadEvent exit '+str(ret.returncode)+'; inspect run.log')
        log = (root/'run.log').read_text(errors='replace')
        log = re.sub(r'(?:\x1b|\\u001b)\[[0-9;]*m', '', log)
        failures = re.findall(r'(?m)^.*interrupted with error:[ \t]*\n([^\n]+)', log)
        if failures:
            raise RuntimeError('MadEvent interrupted: '+failures[-1].strip())
        files = list((proc/'Events').glob('run_*/unweighted_events.lhe*'))
        files = [p for p in files if p.name in ('unweighted_events.lhe', 'unweighted_events.lhe.gz')]
        if len(files) != 1:
            raise ValueError('Expected exactly one final LHE, found '+str(files)+'; inspect run.log')
        used = set(map(int, re.findall(r'Using random number seed offset\s*=\s*(\d+)', log)))
        if used != {j['seed']}:
            raise ValueError('Cannot verify the actual MadEvent seed: '+str(used))
        record['actual_seed_verified_from_log'] = j['seed']
        record['post_parameters'] = validate_parameters(proc/'Cards/param_card.dat', j['kappa3'])
        before = card_utils.parse((snapshot/'pre_run_card.dat').read_text())
        after = card_utils.parse((proc/'Cards/run_card.dat').read_text())
        for k, v in before.items():
            if k == 'iseed' and after.get(k) == '0':
                continue  # MG5 intentionally resets this; seed is checked in log.
            if k not in after or not card_utils._equal(v, after[k]):
                raise ValueError('MadEvent changed a configured run-card value: '+k)
        record['lhe_parameters'] = read_lhe_cards(files[0], j)
        record.update(read_lhe(files[0], j))
        record['lhe_file'] = str(files[0].relative_to(root))
        record['lhe_sha256'] = sha(files[0])
        record['status'] = 'GENERATED'
        record['scope'] = 'Stable HH, full four-diagram LO amplitude; no decays or Higgs branching factors.'
        print('GENERATED:', j['job_id'], record['sigma_fb'], '+/-', record['sigma_mc_err_fb'], 'fb')
    except Exception as ex:
        error = str(ex)
        record.update(status='FAILED', error=error)
        (root/'exception.txt').write_text(traceback.format_exc())
        print('FAILED:', args.job_id, error, file=sys.stderr)
    finally:
        dump(record, root/'result.json')
        archive_output(root)
    return 1 if error else 0



def install_runtime_card(path, kappa3):
    text = (ROOT/'param_card_SM.dat').read_text()
    lines, block, replaced = [], None, 0
    for line in text.splitlines(keepends=True):
        tokens = line.split('#', 1)[0].split()
        if tokens and tokens[0].lower() == 'block':
            block = tokens[1].lower()
        elif tokens and tokens[0].lower() == 'decay':
            block = None
        elif block == 'new' and tokens and tokens[0] == '3':
            line = f'  3 {kappa3:.12e} # C3 = kappa3\n'
            replaced += 1
        lines.append(line)
    if replaced != 1:
        raise ValueError('Expected exactly one NEW[3] in corrected SM card')
    path.write_text(''.join(lines))
    return validate_parameters(path, kappa3)


def submit_file(args):
    manifest = verified_manifest()
    if not re.fullmatch(r'[A-Za-z0-9_-]+', args.tag):
        raise ValueError('Batch tag must use letters, digits, underscores or hyphens')
    if re.search(r'[\s,;"\x27$]', str(ROOT)):
        raise ValueError('Use a package path without whitespace or Condor metacharacters')
    known = {j['job_id']: j for j in jobs()}
    if args.only and (set(args.only)-set(known) or len(set(args.only)) != len(args.only)):
        raise ValueError('Unknown or duplicate job ID in --only')
    selected = [known[j] for j in args.only] if args.only else list(known.values())
    for channel in {j['process_id'] for j in selected}:
        archive = ROOT/'templates'/f'{channel}.tar.gz'
        if sha(archive) != manifest['templates'][channel]['archive_sha256']:
            raise ValueError('Template archive checksum mismatch: '+channel)
    tag = args.tag
    for name in ['submissions', f'results/{tag}', f'condor_logs/{tag}']:
        (ROOT/name).mkdir(parents=True, exist_ok=True)
    dest = ROOT/'submissions'/f'{tag}.sub'
    (ROOT/'worker.sh').chmod(0o755)
    text = f'''# FCC-mue kappa3 scan, unpolarized beams.
universe = vanilla
executable = {ROOT}/worker.sh
initialdir = {ROOT}
arguments = $(job_id)
should_transfer_files = YES
when_to_transfer_output = ON_EXIT
transfer_input_files = templates/$(archive),scan.py,scan_grid.py,scan_results.py,card_utils.py,run_manifest.json,param_card_SM.dat,reference
transfer_output_files = job_output.tar.gz
transfer_output_remaps = "job_output.tar.gz=results/{tag}/$(job_id).$(Cluster).tar.gz"
output = condor_logs/{tag}/$(job_id).$(Cluster).out
error = condor_logs/{tag}/$(job_id).$(Cluster).err
log = condor_logs/{tag}/$(job_id).$(Cluster).log
request_cpus = 1
request_memory = 4GB
request_disk = 8GB
+JobFlavour = "tomorrow"
max_materialize = 12
queue job_id,archive from (
'''+''.join(j['job_id']+' '+j['archive']+'\n' for j in selected)+')\n'
    with dest.open('x') as f:
        f.write(text)
    print(f'{len(selected)} jobs in {dest}')


def main():
    from scan_results import collect, write_job_table
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest='cmd', required=True)
    p = sub.add_parser('prepare', help='Snapshot the existing verified MadEvent exports')
    p.add_argument('--prepared', default=str(Path.home()/'FCCmue_HHVBF_ModelValidation_v1/prepared'))
    p = sub.add_parser('submit-file', help='Write a Condor submit description')
    p.add_argument('--tag', default='main')
    p.add_argument('--only', nargs='+', metavar='JOB_ID', help='Select jobs for a pilot or retry')
    p = sub.add_parser('worker', help=argparse.SUPPRESS)
    p.add_argument('job_id')
    sub.add_parser('collect', help='Audit returned archives and assemble the scan table')
    sub.add_parser('grid', help='Print the planned jobs and their seeds')
    args = ap.parse_args()
    if args.cmd == 'prepare':
        prepare(args)
        with (ROOT/'scan_jobs.csv').open('w', newline='') as f:
            write_job_table(f)
    elif args.cmd == 'submit-file':
        submit_file(args)
    elif args.cmd == 'worker':
        return worker(args)
    elif args.cmd == 'collect':
        return collect()
    else:
        write_job_table(sys.stdout)
    return 0


if __name__ == '__main__':
    # Make the executable and the collector use the same module instance.
    sys.modules['scan'] = sys.modules[__name__]
    try:
        sys.exit(main())
    except Exception as ex:
        print('ERROR:', ex, file=sys.stderr)
        sys.exit(1)
