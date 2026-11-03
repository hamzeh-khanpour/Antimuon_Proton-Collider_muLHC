#!/usr/bin/env python3
"""Extract all four *original* MG5 process diagram sets from CERN templates.

Usage on lxplus from your FCCmue_Higgs_PolScan_v1_1_CERN_PTL_FIX_AFS directory:
    python3 extract_FCCmue_all4_MG5_diagrams.py

Input: templates/{CC_H,CC_HH,NC_H,NC_HH}.tar.gz
Output: FCCmue_original_MG5_feynman_diagrams_all4.zip

No physics generation, diagram modification, or recalculation is performed.
"""
from pathlib import Path
import tarfile
import zipfile
import subprocess
import shutil
import sys
import os

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else '.').expanduser().resolve()
PROCS = ('CC_H', 'CC_HH', 'NC_H', 'NC_HH')
EXTS = {'.ps', '.eps', '.pdf', '.jpg', '.jpeg', '.png', '.svg'}
OUT = ROOT / 'FCCmue_original_MG5_feynman_diagrams_all4'
OUT.mkdir(parents=True, exist_ok=True)
counts = {}
for proc in PROCS:
    archive = ROOT / 'templates' / (proc + '.tar.gz')
    if not archive.is_file():
        print(f'ERROR: missing {archive}', file=sys.stderr)
        sys.exit(2)
    files = []
    with tarfile.open(archive, 'r:gz') as tf:
        for m in tf:
            if not m.isfile():
                continue
            parts = Path(m.name).parts
            if parts and parts[0] == 'process':
                parts = parts[1:]
            if not parts or any(p in ('', '.', '..') for p in parts):
                continue
            rel = Path(*parts)
            in_relevant_dir = 'SubProcesses' in parts or 'HTML' in parts
            is_diagram = in_relevant_dir and rel.suffix.lower() in EXTS
            # Save model/process definitions for provenance too.
            is_card = rel.as_posix() == 'Cards/proc_card_mg5.dat'
            if not (is_diagram or is_card):
                continue
            fh = tf.extractfile(m)
            if fh is None:
                continue
            dest = OUT / proc / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            with fh, dest.open('wb') as of:
                shutil.copyfileobj(fh, of)
            if is_diagram:
                files.append(dest)
    counts[proc] = len(files)
    print(f'{proc:6s}: {len(files)} original diagram-graphic file(s) extracted')

# If Ghostscript tools are available, offer PDF copies of original PS graphics.
ps2pdf = shutil.which('ps2pdf')
if ps2pdf:
    for ps in OUT.rglob('*.ps'):
        pdf = ps.with_suffix('.pdf')
        if not pdf.exists():
            run = subprocess.run([ps2pdf, str(ps), str(pdf)],
                                 capture_output=True, text=True)
            if run.returncode != 0:
                print('WARN: could not convert:', ps, run.stderr[-250:])
else:
    print('INFO: ps2pdf unavailable; original PostScript and JPEG remain usable.')

readme = '''Original MadGraph5_aMC@NLO Feynman-diagram graphics for four FCC-mue processes.\n\nCC_H:  e- mu+ > ve vm~ h QCD=0\nCC_HH: e- mu+ > ve vm~ h h QCD=0\nNC_H:  e- mu+ > e- mu+ h QCD=0\nNC_HH: e- mu+ > e- mu+ h h QCD=0\n\nSource: process archives under templates/ from the FCCmue Higgs PolScan CERN package.\nThese are MadGraph-exported diagrams; the full 2->3 or 2->4 tree amplitudes\nmay contain more graphs than the illustrative VBF subtopologies.\nThe 1-TeV/2-TeV beam energies and beam polarization affect the matrix-element\nevaluation and cross section, not which diagrams are generated.\n'''
(OUT / 'README.txt').write_text(readme)
zippath = ROOT / 'FCCmue_original_MG5_feynman_diagrams_all4.zip'
with zipfile.ZipFile(zippath, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
    for file in OUT.rglob('*'):
        if file.is_file():
            zf.write(file, file.relative_to(ROOT))
print('OUTPUT:', zippath)
print('ZIP bytes:', zippath.stat().st_size)
if not any(counts.values()):
    print('WARNING: no original diagram graphics were found in any template.')
    print('Run MG5 process generation with default JPEG/PS output to create them.')
    sys.exit(1)
if any(v == 0 for v in counts.values()):
    print('WARNING: at least one process has no extracted graphics; inspect its archive.')
else:
    print('SUCCESS: diagram graphics extracted for all four processes.')
