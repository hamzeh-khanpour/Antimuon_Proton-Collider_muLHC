"""Production grid and the verified unpolarized reference table."""
import hashlib
import json
import math

PACKAGE = 'FCCmue_HHVBF_Kappa3PolarizationScan_v1'
ENERGIES = {'E1': (125.0, 2000.0), 'E2': (200.0, 5000.0)}
CHANNEL_IDS = ('CC_HH', 'NC_HH')
KAPPA_TENTHS = (-100, -50, -30, -20, -10, 0, 1, 5, 7, 8, 9, 10,
                 11, 12, 13, 15, 19, 20, 30, 40, 50, 70, 100)
KAPPA_GRID = tuple(k/10 for k in KAPPA_TENTHS)
POLARIZATIONS = (0, 20, 40, 60, 80, 100)
NEW_POLARIZATIONS = POLARIZATIONS[1:]
SCAN_EVENTS = 30000
SCAN_SEED_BASE = 75100037
EXPERIMENTAL_INTERVALS = {'ATLAS+CMS': (-0.71, 6.1), 'ATLAS': (-1.2, 7.2),
                          'CMS': (-1.35, 6.37)}
BASELINE_SHA = '8d80b9efd82e4d502a8f11039ee3e9c39178bedc36cf5f9da22b4b46dbfee34b'


def jobs():
    out = []
    for eid, (electron, muplus) in ENERGIES.items():
        for channel in CHANNEL_IDS:
            for pol in NEW_POLARIZATIONS:
                for k in KAPPA_TENTHS:
                    point = f'{"m" if k < 0 else "p"}{abs(k):03d}'
                    out.append(dict(job_id=f'polscan_{eid}_{channel}_P{pol:03d}_k{point}',
                                    process_id=channel, energy_id=eid, kappa3=k/10,
                                    electron_GeV=electron, muplus_GeV=muplus,
                                    sqrts_GeV=2*math.sqrt(electron*muplus),
                                    polarization_percent=pol, CV=1.0, C2V=1.0,
                                    nevents=SCAN_EVENTS, seed=SCAN_SEED_BASE+len(out)*1009,
                                    archive=f'{channel}.tar.gz',
                                    run_card_file=f'reference/{eid}_{channel}_run_card.dat'))
    return out


def baseline_rows(root):
    content = (root/'reference/Unpolarized_CERN_scan_report.json').read_bytes()
    if hashlib.sha256(content).hexdigest() != BASELINE_SHA:
        raise ValueError('Unpolarized CERN scan report checksum mismatch')
    report = json.loads(content)
    if (report['status'], report['validated_new_jobs'], report['reused_sm_points']) != ('COMPLETE', 88, 4):
        raise ValueError('The unpolarized CERN scan is incomplete')
    rows = report['points']
    expected = {(e, c, k) for e in ENERGIES for c in CHANNEL_IDS for k in KAPPA_GRID}
    if len(rows) != len(expected) or {(r['energy_id'],r['process_id'],r['kappa3']) for r in rows} != expected:
        raise ValueError('Expected all 92 unpolarized grid points')
    for row in rows:
        if (row['polarization_percent'] != 0 or row['event_shortfall'] != 0
                or row['n_events'] != 30000
                or row['sqrts_GeV'] != 2*math.sqrt(math.prod(ENERGIES[row['energy_id']]))
                or any(not math.isfinite(row[key]) or row[key] <= 0
                       for key in ('sigma_fb','sigma_mc_err_fb'))):
            raise ValueError('Invalid unpolarized reference point: '+row['job_id'])
    seeds = {r['seed'] for r in rows}
    if len(seeds) != len(rows) or seeds & {j['seed'] for j in jobs()}:
        raise ValueError('Duplicated or overlapping unpolarized seed')
    return rows
