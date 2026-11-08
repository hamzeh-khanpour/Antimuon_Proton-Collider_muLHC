#!/usr/bin/env python3
"""Reproducible assertions for the released FCC-mue kick-off project."""
from pathlib import Path
import csv,math,re,fitz
r=Path(__file__).resolve().parents[1]
with (r/'data/cross_sections_48.csv').open(newline='') as f: fig=list(csv.DictReader(f))
with (r/'data/cross_sections_original_CERN.csv').open(newline='') as f: origin=list(csv.DictReader(f))
key=lambda a:(a['process_id'],a['energy_id'],int(a['polarization_percent']))
a={key(x):x for x in fig}; b={key(x):x for x in origin}
expected={(p,e,pol) for p in ('CC_H','CC_HH','NC_H','NC_HH') for e in ('E1','E2') for pol in (0,20,40,60,80,100)}
assert len(fig)==len(origin)==len(a)==len(b)==48
assert set(a)==set(b)==expected
for k in expected:
    x,y=a[k],b[k]
    assert x['job_id']==y['job_id'] and x['seed']==y['seed']
    assert x['status']==y['status']=='COMPLETED_UNVALIDATED'
    assert int(x['n_events'])==int(y['n_events'])==30000
    for field in ('sigma_fb','sigma_mc_err_fb'):
        assert math.isclose(float(x[field]),float(y[field]),rel_tol=1e-12,abs_tol=1e-14)
tex=(r/'FCCmue_Higgs_Physics_Kickoff_2026.tex').read_text()
assert len(re.findall(r'\\begin\{frame\}',tex)) ==48
assert r'\appendix' in tex
assert len(re.findall(r'^% Slide',tex,flags=re.M))==48
assert '0.63' in tex and '0.844640' in tex and '0.0077129' in tex
for p,expected_pages in [('CC_H',1),('CC_HH',4),('NC_H',1),('NC_HH',4)]:
    source=r/'figures/original_mg5'/f'{p}_matrix.pdf'
    assert source.exists()
    extracted=fitz.open(str(source))[0].get_text()
    assert ('diagram '+str(expected_pages)) in extracted.lower(),p
pdf=r/'FCCmue_Higgs_Physics_Kickoff_2026.pdf'
with fitz.open(str(pdf)) as d:
    assert len(d)==48
    widths={round(p.rect.width/p.rect.height,5) for p in d}
    assert all(abs(x-1.6)<.01 for x in widths),widths
print('PASS: 48/48 CERN source-data matches; 48 frames/pages; original diagram files; exact source caveats; AGH 16:10.')
