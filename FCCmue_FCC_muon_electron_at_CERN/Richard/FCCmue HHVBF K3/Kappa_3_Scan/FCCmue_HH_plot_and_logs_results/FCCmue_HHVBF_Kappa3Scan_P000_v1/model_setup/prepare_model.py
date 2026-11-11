#!/usr/bin/env python3
"""Prepare matched HH model templates. Never launches event generation or Condor.

Writes only a new named model beneath MG5/models (or verifies an existing
identical copy), and a new output directory. The original SM and CVMFS model
are never edited. Requires the user's existing MG5 installation.
"""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parent
MODEL_NAME = 'HHVBF_UFO_FCCmue'
CHANNELS = {
    'CC_HH': 'e- mu+ > ve vm~ h h',
    'NC_HH': 'e- mu+ > e- mu+ h h',
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def install_model(mg):
    source = ROOT/MODEL_NAME
    target = mg/'models'/MODEL_NAME
    files = [p for p in source.iterdir() if p.is_file()]
    if target.exists():
        for p in files:
            if not (target/p.name).is_file() or digest(target/p.name) != digest(p):
                raise RuntimeError('Existing different model preserved: '+str(target))
    else:
        shutil.copytree(source, target)
    return target


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--mg5', type=Path, required=True, help='Existing MG5 root directory')
    ap.add_argument('--output', type=Path, required=True, help='New output directory; must not exist')
    ap.add_argument('--format', choices=['madevent','standalone_cpp'], default='madevent')
    args = ap.parse_args()
    mg = args.mg5.expanduser().resolve()
    out = args.output.expanduser().resolve()
    if not (mg/'bin/mg5_aMC').is_file():
        raise RuntimeError('MG5 executable not found under '+str(mg))
    if out.exists():
        raise RuntimeError('Output exists; preserving it: '+str(out))
    version = (mg/'VERSION').read_text()
    if 'version = 3.6.4' not in version:
        raise RuntimeError('This validation package targets MG5 3.6.4; found '+version)
    if args.format == 'madevent' and shutil.which('gfortran') is None:
        raise RuntimeError('MadEvent preparation requires gfortran in PATH')
    model = install_model(mg)
    out.mkdir(parents=True)
    sys.path.insert(0,str(mg))
    from madgraph.interface.master_interface import MasterCmd
    cmd = MasterCmd()
    cmd.exec_cmd('set automatic_html_opening False',printcmd=False)
    cmd.exec_cmd('set group_subprocesses False',printcmd=False)
    cmd.exec_cmd('set gauge unitary',printcmd=False)
    cmd.exec_cmd('import model '+MODEL_NAME+'-fccmue',printcmd=False)
    externals = cmd._curr_model['parameters'][('external',)]
    new = {tuple(p.lhacode) for p in externals if p.lhablock.upper() == 'NEW'}
    if new != {(1,),(2,),(3,)}:
        raise RuntimeError('One or more NEW coupling knobs were fixed/merged at import')
    result = {'status':'PREPARATION_STARTED_NO_INTEGRATION','mg5_version':version,
              'model':str(model),'restriction':'fccmue','gauge':'unitary',
              'runtime_param_card_sha256':digest(ROOT/'param_card_SM.dat'),
              'channels':[],
              'scope':'Process preparation only. Run cards are not yet configured for production.'}
    for channel, process in CHANNELS.items():
        command = 'generate '+process+' QCD=0 QED=4 CV=2 C2V=1 C3=1'
        cmd.exec_cmd(command,printcmd=False)
        counts = [len(a['diagrams']) for a in cmd._curr_amps]
        if counts != [4]:
            raise RuntimeError(channel+' expected four complete HH diagrams, found '+str(counts))
        target = out/channel
        export = 'output '+('standalone_cpp ' if args.format=='standalone_cpp' else '')+str(target)
        cmd.exec_cmd(export,printcmd=False)
        # Critical: import restriction has 1.1,1.2,1.3 preservation values.
        # Every prepared template receives the separate matched SM runtime card.
        runtime = target/'Cards/param_card.dat'
        shutil.copy2(ROOT/'param_card_SM.dat',runtime)
        default = target/'Cards/param_card_default.dat'
        if default.exists():
            shutil.copy2(ROOT/'param_card_SM.dat',default)
        if digest(runtime) != digest(ROOT/'param_card_SM.dat'):
            raise RuntimeError('Runtime card copy failed')
        result['channels'].append({'channel':channel,'command':command,
                                   'diagram_counts':counts,'output':str(target)})
    result['status'] = 'PREPARED_NOT_RATE_VALIDATED'
    (out/'preparation_manifest.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
    print('No launch, integration, event generation, shower or batch submission was performed.')


if __name__ == '__main__':
    main()
