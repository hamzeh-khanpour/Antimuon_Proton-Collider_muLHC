#!/usr/bin/env python3
"""Use the installed MG5 run-card schema to disable ALL registered cuts.
Final eta and disjoint-pair requirements are deliberately applied in analysis.
Actual MG5 integration of this adapter must be tested on the user's installation.
"""
import argparse
import json
import math
import re
from pathlib import Path
import shutil
import sys
from physics import model_inputs
from processes import COMPONENTS

ROOT=Path(__file__).resolve().parent


def settings_for(config,component,nevents,seed):
    beams=config['beam_setups'][COMPONENTS[component]['beam']]
    scale=config['physics_conventions']['renormalization_scale_GeV']
    return dict(nevents=nevents,iseed=seed,lpp1=0,lpp2=0,
        ebeam1=beams['energies_GeV'][0],ebeam2=beams['energies_GeV'][1],
        polbeam1=0.,polbeam2=0.,maxjetflavor=4,
        ptj=0.,ptb=0.,ptheavy=0.,ptl=0.,misset=0.,etab=-1.,etaj=-1.,
        drbb=0.,drjj=0.,mmbb=0.,mmbbmax=-1.,mmjj=0.,mmjjmax=-1.,
        ickkw=0,xqcut=0.,ktdurham=-1.,ptlund=-1.,
        cut_decays=False,auto_ptj_mjj=False,
        fixed_ren_scale=True,scale=scale,dsqrt_q2fact1=scale,dsqrt_q2fact2=scale,
        fixed_fac_scale1=True,fixed_fac_scale2=True,
        use_syst=False,event_norm='average',
        custom_fcts=[],pdlabel='none',
        req_acc=config['runtime']['integration_accuracy_target'])


def neutralize_registered_cuts(card):
    """Mirror the schema's own conventions but handle booleans explicitly."""
    if not getattr(card,'cuts_parameter',None):
        raise ValueError('Installed MG5 exposes no cut registry; refusing a partial patch')
    changes={}
    for name in card.cuts_parameter:
        old=card[name]
        # MadGraph registers dparameter alongside kT/Durham settings, but it
        # is a distance-measure parameter, NOT an independent event cut.
        # MG5 3.6.6 serializes it at its native 0.4. Do not force it to 0:
        # ktdurham=-1, ptlund=-1 and ickkw=0 disable the relevant selection
        # and matching mechanisms. Preserve this value and audit it below.
        if name == 'dparameter':
            continue
        if isinstance(old,bool):
            new=False
        elif isinstance(old,dict):
            new={}
        elif isinstance(old,(int,float)):
            if 'min' in name:
                new=0
            elif 'max' in name or 'eta' in name:
                new=-1
            else:
                new=0
        else:
            raise ValueError('Unknown cut type; requires audit: '+name)
        card[name]=new
        changes[name]={'before':old,'after':card[name]}
    return changes



def roundtrip_equal(actual, expected):
    """Accept harmless float serialization rounding; reject real changes.

    Booleans and container-valued settings must still match exactly.
    """
    if isinstance(actual, bool) or isinstance(expected, bool):
        return type(actual) is type(expected) and actual == expected
    if (isinstance(actual, (float, int)) and not isinstance(actual, bool)
            and isinstance(expected, (float, int)) and not isinstance(expected, bool)):
        return math.isclose(float(actual), float(expected), rel_tol=1e-7, abs_tol=1e-9)
    return actual == expected


def assert_roundtrip(key, actual, expected, context):
    if not roundtrip_equal(actual, expected):
        raise ValueError(
            f'{context} {key}: in-memory={expected!r} ({type(expected).__name__}), '
            f'read-back={actual!r} ({type(actual).__name__}). '
            'Check the written Cards/run_card.dat and installed MadGraph schema; '
            'the check has NOT been bypassed.'
        )



def ensure_serialized_scale(path, requested_scale):
    """Repair a scale assignment swallowed by an MG5 run-card comment.

    MG5 3.6.6 may produce a line equivalent to:
      True = fixed_fac_scale2 ! ... beam 2 125.0 = scale ! fixed ren scale
    so the scale is commented out and the parser falls back to MZ.  Only
    repair this exact structure or an unambiguous standalone scale line.
    """
    path = Path(path)
    content = path.read_text()
    lines = content.splitlines(keepends=True)
    standalone = []
    swallowed = []
    for index, line in enumerate(lines):
        part = line.split('!', 1)[0]
        if re.fullmatch(r'\s*[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eEdD][+-]?\d+)?\s*=\s*scale\s*', part, re.I):
            standalone.append(index)
        elif re.search(r'=\s*scale\b', line, re.I):
            swallowed.append(index)
    if len(standalone) == 1 and not swallowed:
        idx = standalone[0]
        body, bang, tail = lines[idx].partition('!')
        lines[idx] = f' {requested_scale:.12e} = scale' + ((' !' + tail) if bang else '\n')
    elif not standalone and len(swallowed) == 1:
        idx = swallowed[0]
        line = lines[idx]
        # Match a swallowed scale ONLY after either observed fixed-factorization setting.
        if not re.match(r'\s*(?:True|False)\s*=\s*(?:fixed_fac_scale2|fixed_fac_scale)\b', line, re.I):
            raise ValueError('Scale field swallowed in an unexpected run-card line: ' + repr(line))
        match = re.search(r'(?<![\w.])([+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eEdD][+-]?\d+)?)\s*=\s*scale\b', line, re.I)
        if match is None:
            raise ValueError('Could not isolate swallowed renormalization scale field')
        left = line[:match.start()].rstrip()
        right = line[match.end():].rstrip('\n')
        if '!' not in left or '!' not in right:
            raise ValueError('Unexpected swallowed-scale comment structure')
        lines[idx] = left + '\n' + f' {requested_scale:.12e} = scale' + right + '\n'
    else:
        raise ValueError(f'Ambiguous scale assignments: standalone={len(standalone)}, swallowed={len(swallowed)}')
    repaired = ''.join(lines)
    if repaired != content:
        path.write_text(repaired)
    return 1


def remove_invalid_bypass_check_entry(path):
    """Omit MG5 3.6.6's invalid empty-list override from the serialized card.

    The default is an empty bypass list. Explicitly serializing [''] triggers
    a bug in MG5's banner RunCard parser when combining LHE events. Removing
    the assignment leaves the native no-bypass default in effect.
    Never remove a nonempty value, and reject ambiguous duplicates.
    """
    path = Path(path)
    lines = path.read_text().splitlines(keepends=True)
    entries = [i for i, line in enumerate(lines)
               if re.fullmatch(r"[ \t]*bypass_check", line.split('#', 1)[0].split('=', 1)[-1].strip(), re.I)
               and '=' in line.split('#', 1)[0]]
    if len(entries) == 0:
        return 'already_absent'
    if len(entries) != 1:
        raise ValueError(f'Expected at most one bypass_check assignment; found {len(entries)}')
    index = entries[0]
    value = lines[index].split('#', 1)[0].split('=', 1)[0].strip()
    if value not in ("['']", '[]', '[ ]'):
        raise ValueError('Refusing to remove nonempty or unexpected bypass_check: '+repr(value))
    del lines[index]
    path.write_text(''.join(lines))
    if re.search(r'(?mi)^[ \t]*[^#\n]*=[ \t]*bypass_check\b', path.read_text()):
        raise ValueError('bypass_check entry remains after cleanup')
    return value


def prepare(process_dir,mg_root,component,config,nevents,seed,custom_card=None):
    if nevents < 2 or nevents > 1000000 or not 0 < seed < 30081**2:
        raise ValueError('Need 2<=NEVENTS<=1000000 and 0<seed<30081^2')
    sys.path.insert(0,str(mg_root))
    from madgraph.various.banner import RunCardLO
    proc=Path(process_dir)
    path=proc/'Cards'/'run_card.dat'
    param=proc/'Cards'/'param_card.dat'
    if not path.is_file() or not param.is_file():
        raise ValueError('Generated process lacks run_card.dat or param_card.dat')
    shutil.copy2(path,proc/'Cards'/'run_card.before_package.dat')
    shutil.copy2(param,proc/'Cards'/'param_card.before_package.dat')
    if custom_card:
        shutil.copy2(custom_card,param)
    inputs=model_inputs(param)
    for pdg in (5,25):
        value=inputs['all_slha_inputs'][f'mass:{pdg}']
        expected=config['required_model_values'][f'mass_{pdg}_GeV']
        if not math.isclose(value,expected,rel_tol=1.e-10,abs_tol=1.e-10):
            raise ValueError(f'Baseline requires MASS {pdg}={expected}, found {value}')
    for block,pdg in [('mass',4),('mass',11),('mass',13),('yukawa',4),('yukawa',11),('yukawa',13),
                      ('wolfenstein',1),('wolfenstein',2),('wolfenstein',3),('wolfenstein',4)]:
        if inputs['all_slha_inputs'].get(f'{block}:{pdg}',0.) != 0:
            raise ValueError(f'{block} {pdg} is removed by the default sm restriction; a param-card edit cannot restore it')
    # Fresh output only: archive active secondary-stage cards instead of running them.
    disabled=[]
    for filename in ('pythia_card.dat','pythia8_card.dat','madspin_card.dat',
                     'delphes_card.dat','shower_card.dat','reweight_card.dat',
                     'madanalysis5_parton_card.dat','madanalysis5_hadron_card.dat'):
        active=proc/'Cards'/filename
        if active.exists():
            target=active.with_name(filename+'.disabled_by_baseline')
            if target.exists():
                raise ValueError('Refusing to overwrite an existing archived card: '+str(target))
            active.rename(target)
            disabled.append(filename)
    run=RunCardLO(str(path))
    changes=neutralize_registered_cuts(run)
    settings=settings_for(config,component,nevents,seed)
    # MG5 3.6.6 defines boost_event as a string, not a Python boolean.
    # Keep the generated run card's native no-boost setting rather than
    # coercing False or guessing the exact string representation.
    if 'boost_event' in run:
        native_boost = run['boost_event']
        if not isinstance(native_boost, str):
            raise ValueError('Unexpected boost_event schema type: '+type(native_boost).__name__)
        if native_boost.strip().lower() not in ('', 'false', 'none', '0'):
            raise ValueError('Generated run card requests a non-default boost_event: '+repr(native_boost))
        settings['boost_event'] = native_boost
    # MG5 3.6.6 also exposes the legacy global `fixed_fac_scale` flag.
    # Its hidden False default can override fixed_fac_scale1/2 on parsing.
    # Keep both the global and per-beam flags consistent, and verify them all.
    if 'fixed_fac_scale' in run:
        if not isinstance(run['fixed_fac_scale'], bool):
            raise ValueError('Unexpected fixed_fac_scale type')
        settings['fixed_fac_scale'] = True
    if 'fixed_fact_scale' in run:
        settings['fixed_fact_scale'] = True
    optional={'boost_event','custom_fcts','req_acc','auto_ptj_mjj',
              'fixed_fac_scale1','fixed_fac_scale2','ptlund'}
    applied={}
    unsupported=[]
    for key,value in settings.items():
        if key not in run:
            if key not in optional:
                raise ValueError('Required run-card option unsupported by this MG5: '+key)
            unsupported.append(key)
            continue
        if key=='pdlabel':
            # lpp=0 is decisive. Older releases may not implement pdlabel='none'.
            try:
                run[key]=value
            except Exception:
                run[key]='nn23lo1'
                value='nn23lo1'
        else:
            run[key]=value
        applied[key]=run[key]
    # Save full schema, including hidden fields, not a hand-patched short card.
    run.write(str(path),write_hidden=True)
    # MG5 3.6.6 serializes its empty bypass_check default as [''], which
    # crashes banner.write during combine_events: list has no .lower().
    # Remove only that redundant malformed override; keep every real cut and
    # every physics setting unchanged. Fail closed on an unexpected value.
    bypass_removed = remove_invalid_bypass_check_entry(path)
    # Some MG5 3.6.6 RunCardLO writers retain the default 91.188 GeV in the
    # serialized `scale` field despite `run['scale']=125`. Correct the explicit
    # field, then independently reparse and check every requested setting.
    after=RunCardLO(str(path))
    if not roundtrip_equal(after['scale'], applied['scale']):
        ensure_serialized_scale(path, settings['scale'])
        after=RunCardLO(str(path))
    for key,value in applied.items():
        assert_roundtrip(key, after[key], value, 'Run-card round-trip changed setting')
    for key,entry in changes.items():
        expected=applied.get(key,entry['after'])
        assert_roundtrip(key, after[key], expected,
                         'A disabled generation cut changed on read-back:')
    # dparameter is a distance measure for the inactive kT/Durham machinery,
    # not a stand-alone veto. Retain MG's default value and verify that it
    # has not changed, while strictly enforcing disabled merging switches.
    if 'dparameter' in run:
        assert_roundtrip('dparameter', after['dparameter'], run['dparameter'],
                         'Inactive kT distance parameter changed on read-back:')
    for key,expected in (('ickkw',0), ('ktdurham',-1), ('ptlund',-1), ('xqcut',0.0)):
        if key in after:
            assert_roundtrip(key, after[key], expected,
                             'Required disabled merging/jet cut changed on read-back:')
    audit={'component':component,'model_inputs':inputs,'all_cut_changes':changes,
           'settings':applied,'bypass_check_serialized_value_removed':bypass_removed,'optional_keys_absent':unsupported,'secondary_stage_cards_disabled':disabled,
           'analysis_cuts_only':config['selection'],
           'note':'No generator eta/mass/pT/DeltaR selection; final cuts are evaluated on LHE four-vectors.'}
    (proc/'configuration_audit.json').write_text(json.dumps(audit,indent=2,allow_nan=False)+'\n')
    return audit


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('process_dir',type=Path)
    p.add_argument('--mg-root',type=Path,required=True)
    p.add_argument('--component',choices=COMPONENTS,required=True)
    p.add_argument('--config',type=Path,default=ROOT/'configuration.json')
    p.add_argument('--nevents',type=int,required=True)
    p.add_argument('--seed',type=int,required=True)
    p.add_argument('--param-card',type=Path)
    a=p.parse_args()
    try:
        audit=prepare(a.process_dir,a.mg_root,a.component,json.loads(a.config.read_text()),a.nevents,a.seed,a.param_card)
        print('All registered generation cuts disabled; beam settings and full card audited.')
        print('Model-consistent BR(H->bbbar):',audit['model_inputs']['br_hbb_model'])
    except Exception as exc:
        p.exit(2,'ERROR: '+str(exc)+'\n')


if __name__=='__main__':
    main()
