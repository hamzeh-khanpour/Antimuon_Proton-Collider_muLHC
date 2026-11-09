#!/usr/bin/env python3
"""Publication-style polarization figures from genuine, completed MG5 job reports.

Run after `python3 scan.py collect --mode full --preset exact --energy both`.
Matplotlib is only needed here, not in MadGraph production or the collector.
"""
import argparse
import csv
import json
import math
from pathlib import Path

ROOT=Path(__file__).resolve().parent
PROCESSES=['CC_H','CC_HH','NC_H','NC_HH']
NAMES={'CC_H':r'CC $H$', 'CC_HH':r'CC $HH$',
       'NC_H':r'NC $H$', 'NC_HH':r'NC $HH$'}

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--preset',choices=['exact','fcc_design'],default='exact')
    p.add_argument('--energy',choices=['both','E1','E2'],default='both')
    a=p.parse_args()
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
    except ImportError:
        raise SystemExit('Matplotlib not installed. Install it on your laptop with: python -m pip install matplotlib')
    f=ROOT/'reports/cross_sections.csv'
    if not f.exists():raise SystemExit('Missing '+str(f)+'; first run: python3 scan.py collect --mode full ...')
    with f.open() as fin:
        rows=[r for r in csv.DictReader(fin) if r['preset']==a.preset and
              r['job_id'].startswith('full_') and r['status']=='COMPLETED_UNVALIDATED' and
              (a.energy=='both' or r['energy_id']==a.energy)]
    if not rows:raise SystemExit('No actual completed full-run results found; no plots generated.')
    energies=['E1','E2'] if a.energy=='both' else [a.energy]
    missing=[]
    for proc in PROCESSES:
        for eid in energies:
            for pol in (0,20,40,60,80,100):
                if not any(r['process_id']==proc and r['energy_id']==eid and int(r['polarization_percent'])==pol for r in rows):
                    missing.append((proc,eid,pol))
    if missing:
        raise SystemExit(f'Missing {len(missing)} completed points (e.g. {missing[:5]}). Refusing to draw incomplete misleading curves.')
    out=ROOT/'reports';out.mkdir(exist_ok=True)
    label={'E1':'1 TeV (exact)','E2':'2 TeV (exact)'} if a.preset=='exact' else {'E1':'979.8 GeV (FCC design)','E2':'1913.1 GeV (FCC design)'}
    colors=['tab:blue','tab:orange']
    for quantity in ('absolute','ratio'):
        fig, axs=plt.subplots(2,2,figsize=(10,7),constrained_layout=True)
        for i,proc in enumerate(PROCESSES):
            ax=axs.flat[i]
            for eidx,eid in enumerate(energies):
                rr=sorted([r for r in rows if r['process_id']==proc and r['energy_id']==eid],
                          key=lambda x:int(x['polarization_percent']))
                pol=[int(r['polarization_percent']) for r in rr]
                xs=[float(r['sigma_fb']) for r in rr]
                err=[float(r['sigma_mc_err_fb']) for r in rr]
                if quantity=='ratio':
                    x0=xs[0];e0=err[0]
                    if x0<=0:raise SystemExit('Nonpositive sigma at polarization=0')
                    yy=[x/x0 for x in xs]
                    ee=[0 if k==0 else math.sqrt((err[k]/x0)**2+(xs[k]*e0/x0**2)**2)
                        for k in range(len(xs))]
                else:yy,ee=xs,err
                ax.errorbar(pol,yy,yerr=ee,fmt='o-',capsize=2.5,
                            label=label[eid],color=colors[eidx])
                if quantity=='ratio' and proc.startswith('CC_'):
                    ax.plot([0,100],[1,2],linestyle=':',color='gray',linewidth=1.0,
                            label='SM CC expectation' if eidx==0 else None)
            ax.set_title(NAMES[proc]);ax.set_xlim(-3,103)
            ax.set_xticks([0,20,40,60,80,100]);ax.grid(alpha=.2)
            ax.set_xlabel(r'$P_{\mu^+}$ (%)')
            ax.set_ylabel(r'$\sigma_\mathrm{LO}$ (fb)' if quantity=='absolute'
                          else r'$\sigma(P)/\sigma(0)$')
            ax.legend(fontsize=8)
        fig.suptitle('FCC-$\\mu e$ inclusive Higgs: '+('cross sections' if quantity=='absolute' else 'polarization ratios') +
                     '\nFull tree-level SM, no kinematic cuts; MC integration errors only',fontsize=12)
        prefix=out/f'FCCmue_{a.preset}_{quantity}'
        fig.savefig(str(prefix)+'.pdf')
        fig.savefig(str(prefix)+'.png',dpi=250)
        plt.close(fig)
        print('WROTE:',str(prefix)+'.pdf',str(prefix)+'.png')

if __name__=='__main__':main()
