"""Declared unpolarized scan and the validated SM inputs."""
import hashlib
import json
import math

PACKAGE = 'FCCmue_HHVBF_Kappa3Scan_P000_v1'
ENERGIES = {'E1': (125.0, 2000.0), 'E2': (200.0, 5000.0)}
CHANNEL_IDS = ('CC_HH', 'NC_HH')
KAPPA_TENTHS = (-100, -50, -30, -20, -10, 0, 1, 5, 7, 8, 9,
                 11, 12, 13, 15, 19, 20, 30, 40, 50, 70, 100)
OBSERVED_ATLAS_CMS = (-0.71, 6.1)
SM_REPORT_SHA = '9e2ac3796b720fd122b436bf170616a13d7e359bdfac4f12bc0c67e6563575ef'


def jobs():
    out = []
    for ie, (eid, (electron, muplus)) in enumerate(ENERGIES.items()):
        for ic, channel in enumerate(CHANNEL_IDS):
            for ik, k in enumerate(KAPPA_TENTHS):
                point = f'{"m" if k < 0 else "p"}{abs(k):03d}'
                out.append(dict(job_id=f'kappa3_{eid}_{channel}_k{point}',
                                process_id=channel, energy_id=eid, kappa3=k/10,
                                electron_GeV=electron, muplus_GeV=muplus,
                                sqrts_GeV=2*math.sqrt(electron*muplus),
                                polarization_percent=0, CV=1.0, C2V=1.0,
                                nevents=30000, seed=74100037+ie*200000+ic*100000+ik*1007,
                                archive=f'{channel}.tar.gz',
                                run_card_file=f'reference/{eid}_{channel}_run_card.dat'))
    return out


def sm_rows(root):
    content = (root/'reference/SM_closure_report.json').read_bytes()
    if hashlib.sha256(content).hexdigest() != SM_REPORT_SHA:
        raise ValueError('Validated SM closure report checksum mismatch')
    report = json.loads(content)
    if report['status'] != 'FOUR_POINT_SM_RATE_CLOSURE_COMPATIBLE':
        raise ValueError('The SM closure input did not pass')
    out = []
    for row in report['comparisons']:
        eid, channel = row['energy_id'], row['process_id']
        out.append(dict(energy_id=eid, process_id=channel, kappa3=1.0,
                        sqrts_GeV=2*math.sqrt(math.prod(ENERGIES[eid])),
                        polarization_percent=0, sigma_fb=row['sigma_fb'],
                        sigma_mc_err_fb=row['sigma_mc_err_fb'], seed=row['seed'],
                        n_events=row['n_events'], event_shortfall=0,
                        job_id=row['job_id'], source='validated_local_HHVBF_SM_closure'))
    if len(out) != 4 or {(r['energy_id'], r['process_id']) for r in out} != {
            (e, c) for e in ENERGIES for c in CHANNEL_IDS}:
        raise ValueError('Expected one validated SM point per energy and channel')
    if {r['seed'] for r in out} & {j['seed'] for j in jobs()}:
        raise ValueError('A scan seed overlaps a validated SM seed')
    return out
