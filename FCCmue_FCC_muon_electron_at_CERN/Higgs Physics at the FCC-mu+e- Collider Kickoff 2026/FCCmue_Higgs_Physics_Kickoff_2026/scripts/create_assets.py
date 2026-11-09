#!/usr/bin/env python3
"""Reproducible auxiliary scientific figures; never alters the original CERN data."""
from pathlib import Path
import csv, math
import fitz
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
root=Path(__file__).resolve().parents[1]
fig=root/'figures'; data=root/'data'
# Vector crops preserve the MG5 diagram source, don't rasterize or redraw.
for p in ['CC_H','CC_HH','NC_H','NC_HH']:
    doc=fitz.open(str(fig/'original_mg5'/f'{p}_matrix.pdf'))
    pg=doc[0]
    if p.endswith('HH'):
        pg.set_cropbox(fitz.Rect(50,85,575,555))
    else:
        pg.set_cropbox(fitz.Rect(50,95,340,325))
    doc.save(str(fig/f'{p}_diagrams_cropped.pdf'))
    doc.close()
# Data-derived energy scaling
with (data/'cross_sections_48.csv').open(newline='') as f: rows=list(csv.DictReader(f))
by={(r['process_id'],r['energy_id'],int(r['polarization_percent'])):float(r['sigma_fb']) for r in rows}
labels=['CC $H$','NC $H$','CC $HH$','NC $HH$']; ids=['CC_H','NC_H','CC_HH','NC_HH']
values=[by[(p,'E2',0)]/by[(p,'E1',0)] for p in ids]
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'axes.spines.top':False,'axes.spines.right':False})
fig0,ax=plt.subplots(figsize=(10.4,4.2),layout='constrained')
colors=['#00693c','#418c72','#a71930','#cb6674']
bars=ax.barh(labels[::-1],values[::-1],color=colors[::-1],height=.56)
for b,v in zip(bars,values[::-1]):ax.text(v+0.08,b.get_y()+b.get_height()/2,f'{v:.2f}×',va='center',fontweight='bold')
ax.set_xlim(0,6.5);ax.set_xlabel(r'$\sigma(2\,\mathrm{TeV})/\sigma(1\,\mathrm{TeV})$  (unpolarized, stable Higgs)')
ax.grid(axis='x',alpha=.2);ax.set_axisbelow(True)
fig0.savefig(root/'figures'/'Figure_energy_scaling.pdf',bbox_inches='tight');fig0.savefig(root/'figures'/'Figure_energy_scaling.png',dpi=240,bbox_inches='tight');plt.close(fig0)
# clean rate overview: log-scale
fig0,ax=plt.subplots(figsize=(10.2,4.3),layout='constrained')
import numpy as np
x=np.arange(4);w=.34
for i,E in enumerate(['E1','E2']):
 vals=[by[(p,E,0)] for p in ids]
 ax.bar(x+(-w/2 if i==0 else w/2),vals,width=w,color=['#00693c','#a71930'][i],label=['1 TeV','2 TeV'][i])
ax.set_yscale('log');ax.set_xticks(x,labels);ax.set_ylabel(r'Inclusive $\sigma_{\rm LO}$ [fb]');ax.legend(frameon=False,ncol=2)
ax.grid(axis='y',alpha=.18,which='both');ax.set_axisbelow(True)
fig0.savefig(root/'figures'/'Figure_rate_overview.pdf',bbox_inches='tight');plt.close(fig0)
# machine schematic - schematic, explicitly NOT source image, based on proposal Fig.1
from matplotlib.patches import Arc
fig0,ax=plt.subplots(figsize=(11,4.1),layout='constrained');ax.set_xlim(0,12);ax.set_ylim(0,4.6);ax.axis('off')
ax.plot([1.1,3.2,5.3],[1.25,1.25,1.25],lw=7,c='#a71930',solid_capstyle='round');ax.text(1.1,.75,'FCC-ee electron beam',fontsize=12,color='#a71930',fontweight='bold')
for x,y,r,color,txt in [(6.8,2.35,1.28,'#2e7d5c',r'$\mu^+$ storage ring'),(9.7,3.15,.43,'#5c90b6','source')]:
 ax.add_patch(Circle((x,y),r,fill=False,edgecolor=color,lw=4));ax.text(x,y,txt,ha='center',va='center',fontsize=12)
ax.plot([9.27,7.75],[3.15,3.15],c='#2b2b2b',lw=2.4);ax.annotate('',(7.55,3.15),(8.05,3.15),arrowprops=dict(arrowstyle='->',lw=2))
ax.annotate('',(5.75,1.25),(5.0,1.25),arrowprops=dict(arrowstyle='->',lw=2.5,color='#a71930'))
ax.plot(5.62,1.25,'o',markersize=14,color='#d89a15',markeredgecolor='black');ax.text(5.65,.58,'Interaction point (IP)',ha='center',fontweight='bold')
ax.text(9.65,2.35,r'Ultra-cold $\mu^+$',ha='center',fontsize=11)
ax.text(9.65,2.02,'booster / linacs',ha='center',fontsize=11)
ax.annotate('',(6.17,1.65),(7.05,2.75),arrowprops=dict(arrowstyle='->',lw=2,color='#00693c'))
fig0.text(.5,.01,'Conceptual redrawing after Piotrzkowski, arXiv:2610.40451v2, Fig. 1 — not to scale',fontsize=9,ha='center',color='#666666')
fig0.savefig(root/'figures'/'Figure_FCCmue_concept_schematic.pdf',bbox_inches='tight');plt.close(fig0)
# workflow graphic
fig0,ax=plt.subplots(figsize=(11,2.7));ax.set_xlim(0,12);ax.set_ylim(0,3);ax.axis('off')
steps=['4 full SM\nprocess cards','2 exact-energy\nbeam presets','6 positive-muon\npolarizations','48 HTCondor jobs\n30k events / job','Source CSV\nfigures + QA']
for i,s in enumerate(steps):
 x=.1+i*2.42
 patch=FancyBboxPatch((x,1.0),2.03,1.24,boxstyle='round,pad=0.11',fc='#e4f1e9' if i<4 else '#f5e1e6',ec='#00693c' if i<4 else '#a71930',lw=1.5)
 ax.add_patch(patch);ax.text(x+1.02,1.63,s,ha='center',va='center',fontsize=10.5,linespacing=1.4)
 if i<4:ax.add_patch(FancyArrowPatch((x+2.05,1.63),(x+2.38,1.63),arrowstyle='-|>',mutation_scale=15,color='#373737',lw=1.6))
fig0.savefig(root/'figures'/'Figure_scan_workflow.pdf',bbox_inches='tight');plt.close(fig0)
# provenance checks
assert len(rows)==48
assert len(by)==48
assert set(float(x) for x in [v for v in by.values()])
print('Asset generation OK;',len(rows),'source rows and 4 vector MG5 diagram crops.')
