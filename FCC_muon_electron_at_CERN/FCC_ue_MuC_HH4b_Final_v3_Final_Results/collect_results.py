#!/usr/bin/env python3
"""Sum distinct neutrino flavors, never signal plus the full four-bottom rate."""
import argparse
import csv
import json
import math
from pathlib import Path
from processes import COMPONENTS, GROUPS

MODEL_KEYS=('mb_GeV','mh_GeV','ymb_GeV','GF_GeV_minus2','higgs_width_GeV')


def collect(work):
    work=Path(work)
    available={}
    for name in COMPONENTS:
        path=work/'reports'/(name+'.json')
        if path.is_file():
            result=json.loads(path.read_text())
            if result['component'] != name:
                raise ValueError('Wrong component in '+str(path))
            available[name]=result
    if available:
        first=next(iter(available.values()))
        for result in available.values():
            for key in MODEL_KEYS:
                if not math.isclose(result['model_inputs'][key],first['model_inputs'][key],rel_tol=1.e-10):
                    raise ValueError('Cannot combine different model inputs: '+key)
            if result['selection'] != first['selection']:
                raise ValueError('Cannot combine different fiducial selections')
            # Relevant SM external inputs should also coincide when present in both cards.
            a=first['model_inputs']['all_slha_inputs']; b=result['model_inputs']['all_slha_inputs']
            for key in set(a).intersection(b):
                if not math.isclose(a[key],b[key],rel_tol=1.e-10,abs_tol=1.e-12):
                    raise ValueError('Different SLHA inputs across runs: '+key)
    rows=[]
    for group in GROUPS:
        required=[name for name,spec in COMPONENTS.items() if spec['group']==group]
        missing=[name for name in required if name not in available]
        rows.append(row := {'process':group,'status':'NOT_RUN' if len(missing)==len(required) else 'INCOMPLETE',
                           'components_required':','.join(required),'components_missing':','.join(missing),
                           'sigma_fb':None,'mc_integration_error_fb':None,'mc_selection_error_fb':None,
                           'mc_error_quadrature_approx_fb':None})
        if missing:
            continue
        pieces=[available[name] for name in required]
        if any(p['fiducial_xsec_fb'] is None for p in pieces):
            row['status']='UNRESOLVED_COMPONENT_NO_SELECTED_EVENTS'
            continue
        row['sigma_fb']=sum(p['fiducial_xsec_fb'] for p in pieces)
        for key in ('mc_integration_error_fb','mc_selection_error_fb','mc_error_quadrature_approx_fb'):
            row[key]=math.sqrt(sum(p[key]**2 for p in pieces))
        row['status']='ESTIMATE_NOT_CONVERGENCE_VALIDATED'
        if any(p['status'].startswith('LOW_SELECTED') for p in pieces):
            row['status']='LOW_SELECTED_STATISTICS_NOT_CONVERGENCE_VALIDATED'
    work.mkdir(parents=True,exist_ok=True)
    (work/'results.json').write_text(json.dumps(rows,indent=2,allow_nan=False)+'\n')
    with (work/'results.csv').open('w',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=list(rows[0]))
        writer.writeheader();writer.writerows(rows)
    return rows


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('work',type=Path)
    a=p.parse_args()
    try:
        for row in collect(a.work):
            print(row['process'],row['sigma_fb'],row['status'])
    except (ValueError,KeyError,OSError) as exc:
        p.exit(2,'ERROR: '+str(exc)+'\n')
