#!/usr/bin/env python3
"""Non-destructive MG5 orchestration with process/output/log failure checks."""

# export MG5=/home/hamzeh-khanpour/MG5_aMC_v3_6_6/bin/mg5_aMC

import argparse
import datetime
import json
import os
from pathlib import Path
import platform
import re
import subprocess
import sys
import uuid
from processes import COMPONENTS, GROUPS, write_cards
from collect_results import collect
from analyze_lhe import sha256

ROOT=Path(__file__).resolve().parent
FATAL_PATTERNS=(r'Traceback \(most recent call last\)',
                r'Error detected in',r'command .* interrupted',r'MadGraph5Error',
                r'(?m)^[ \t]*(?:CRITICAL|FATAL|ERROR)[ \t]*[: ]',r'No amplitudes generated',
                r'No matrix elements generated',r'CompilationError',
                r'(?m)^[ \t]*STOP[ \t]+[1-9]')
ANSI=re.compile(r'\x1b\[[0-9;]*[A-Za-z]')

# MG5 can query Git for its version even when installed from a release tarball.
# Git reports this exact benign diagnostic, while MG5 still exits successfully
# and writes a complete process directory.  Do not ignore any OTHER Git error.
BENIGN_GIT_VERSION_MESSAGE = (
    'fatal: not a git repository (or any of the parent directories): .git'
)


def fatal_log(text):
    """Return fatal-pattern matches, excluding only a known harmless Git probe.

    Filtering changes *only* error classification, not the saved log. A nonzero
    subprocess exit code remains fatal, irrespective of this allowlist.
    """
    clean = ANSI.sub('', text)
    clean = '\n'.join(
        line for line in clean.splitlines()
        if line.strip() != BENIGN_GIT_VERSION_MESSAGE
    )
    return [
        pattern for pattern in FATAL_PATTERNS
        if re.search(pattern, clean, re.IGNORECASE)
    ]


def run_logged(command,cwd,log):
    with Path(log).open('w') as stream:
        stream.write('COMMAND: '+repr(command)+'\n');stream.flush()
        proc=subprocess.Popen(command,cwd=cwd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,
                              text=True,bufsize=1,stdin=subprocess.DEVNULL)
        assert proc.stdout is not None
        for line in proc.stdout:
            print(line,end='',flush=True)
            stream.write(line)
        code=proc.wait()
    problems=fatal_log(Path(log).read_text(errors='replace'))
    if code != 0 or problems:
        raise RuntimeError(f'Command failed (exit={code}, fatal_log_matches={problems}); see {log}')


def discover_lhe(process):
    files=sorted((Path(process)/'Events').rglob('unweighted_events.lhe*'))
    files=[p for p in files if p.name in ('unweighted_events.lhe','unweighted_events.lhe.gz') and p.stat().st_size>0]
    if len(files)!=1:
        raise RuntimeError(f'Expected one fresh unweighted LHE output, found {len(files)}; refusing to guess')
    return files[0]


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--mg5',default=os.getenv('MG5'))
    p.add_argument('--work',type=Path,default=os.getenv('WORK'))
    p.add_argument('--config',type=Path,default=ROOT/'configuration.json')
    p.add_argument('--nevents',type=int,default=int(os.getenv('NEVENTS','10000')))
    p.add_argument('--decays',type=int,default=int(os.getenv('NDECAYS','50')))
    p.add_argument('--seed',type=int,default=int(os.getenv('SEED','2301026')))
    p.add_argument('--only',choices=(*GROUPS,*COMPONENTS))
    p.add_argument('--prepare-only',action='store_true',help='Generate/configure sources but do not integrate')
    p.add_argument('--param-card',type=Path,default=os.getenv('PARAM_CARD'))
    args=p.parse_args()
    if not args.mg5:
        p.error('Set MG5=/absolute/path/to/MG5_aMC/bin/mg5_aMC')
    mg=Path(args.mg5).expanduser().resolve()
    mgroot=mg.parent.parent
    if not mg.is_file() or not (mgroot/'madgraph'/'various'/'banner.py').is_file():
        p.error('MG5 must point to a complete local installation (bin/mg5_aMC)')
    if not 2<=args.nevents<=1000000 or args.decays<1 or not 0<args.seed<30081**2-20000:
        p.error('Need 2<=NEVENTS<=1000000, NDECAYS>=1, and a valid positive MG seed')
    if args.param_card and not args.param_card.is_file():
        p.error('PARAM_CARD does not exist')
    config=json.loads(args.config.read_text())
    if config['model']!='sm':
        p.error('This audited baseline requires the default restricted sm model')
    chosen=[name for name,spec in COMPONENTS.items()
            if not args.only or name==args.only or spec['group']==args.only]
    stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    work=(args.work or ROOT/'work'/('run_'+stamp+'_'+uuid.uuid4().hex[:8])).expanduser().resolve()
    if work.exists():
        p.error('Output directory already exists; choose a NEW WORK path. Nothing overwritten.')
    work.mkdir(parents=True)
    for folder in ('cards','logs','reports'):
        (work/folder).mkdir()
    write_cards(work/'cards')
    # Store the complete effective analysis/runtime config, not merely the original defaults.
    config['runtime'].update(nevents_per_component=args.nevents,decays_per_hh_event=args.decays,seed=args.seed)
    (work/'configuration.json').write_text(json.dumps(config,indent=2)+'\n')
    version=(mgroot/'VERSION').read_text(errors='replace') if (mgroot/'VERSION').is_file() else 'See MG logs'
    manifest={'package_version':config['package_version'],'started_utc':stamp,'work':str(work),
              'mg5_path':str(mg),'mg5_version_file':version,'python':sys.version,
              'platform':platform.platform(),'components':chosen,'prepare_only':args.prepare_only,
              'effective_configuration_sha256':sha256(work/'configuration.json'),
              'scripts_sha256':{f.name:sha256(f) for f in ROOT.glob('*.py')},
              'execution':{},'overall_status':'STARTED'}
    def save():
        (work/'manifest.json').write_text(json.dumps(manifest,indent=2,allow_nan=False)+'\n')
    save()
    print('NEW WORK DIRECTORY:',work,flush=True)
    try:
        for name in chosen:
            index=list(COMPONENTS).index(name)
            seed=args.seed+100*index
            manifest['execution'][name]='GENERATING';save()
            print('\n=== '+name+' ===',flush=True)
            run_logged([sys.executable,str(mg),str(work/'cards'/(name+'.mg5'))],work,work/'logs'/(name+'_generate.log'))
            proc=work/name
            for required in ('Cards/param_card.dat','Cards/run_card.dat','bin/generate_events','SubProcesses'):
                if not (proc/required).exists():
                    raise RuntimeError('Missing required generated artifact: '+str(proc/required))
            command=[sys.executable,str(ROOT/'configure_run.py'),str(proc),'--mg-root',str(mgroot),
                     '--component',name,'--config',str(work/'configuration.json'),
                     '--nevents',str(args.nevents),'--seed',str(seed)]
            if args.param_card:
                command += ['--param-card',str(args.param_card.resolve())]
            run_logged(command,work,work/'logs'/(name+'_configure.log'))
            manifest['execution'][name]='PREPARED_NOT_INTEGRATED';save()
            if args.prepare_only:
                continue
            run_logged([sys.executable,str(proc/'bin'/'generate_events'),'-f'],proc,work/'logs'/(name+'_run.log'))
            lhe=discover_lhe(proc)
            command=[sys.executable,str(ROOT/'analyze_lhe.py'),str(lhe),'--component',name,
                     '--param-card',str(proc/'Cards'/'param_card.dat'),'--config',str(work/'configuration.json'),
                     '--decays',str(args.decays),'--seed',str(seed+20000),
                     '--json',str(work/'reports'/(name+'.json'))]
            run_logged(command,work,work/'logs'/(name+'_analysis.log'))
            manifest['execution'][name]='ANALYZED_NOT_CONVERGENCE_VALIDATED';save()
            collect(work)
        manifest['overall_status']='PREPARED_ONLY' if args.prepare_only else 'FINISHED_NOT_CONVERGENCE_VALIDATED'
        collect(work);save()
        print('\nReports:',work/'results.csv')
        print('Do not call these precision results until integration and sample convergence are checked.')
    except Exception as exc:
        manifest['overall_status']='FAILED'
        manifest['error']=str(exc)
        save()
        # Preserve all partial results, logs, and MG-generated debug files in place.
        try:
            collect(work)
        except Exception as collection_error:
            manifest['collection_error']=str(collection_error);save()
        p.exit(2,'ERROR: '+str(exc)+'\nAll artifacts preserved in '+str(work)+'\n')


if __name__=='__main__':
    main()
