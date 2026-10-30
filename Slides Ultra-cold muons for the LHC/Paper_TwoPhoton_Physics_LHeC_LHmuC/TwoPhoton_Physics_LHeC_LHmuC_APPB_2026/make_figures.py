#!/usr/bin/env python3
"""Original, reproducible schematics and a deliberately illustrative EPA calculation.
No source plots are reconstructed or presented as the author's original numerical simulations.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, Circle
from scipy.integrate import quad
from pathlib import Path
D=Path(__file__).resolve().parent/'figures';D.mkdir(exist_ok=True)
plt.rcParams.update({'font.size':9,'mathtext.fontset':'dejavusans','pdf.fonttype':42,'axes.linewidth':.8})
C=['#244b73','#268481','#d08837','#a84f56']

# Figure 1: purely schematic physics topology, no external figure reuse.
fig,axes=plt.subplots(1,2,figsize=(7.05,1.88),sharey=True)
for a,el in zip(axes,[True,False]):
    a.set_xlim(0,8);a.set_ylim(0,5.3);a.axis('off')
    a.plot([.55,2.75],[4.5,4.0],color=C[0],lw=1.7)
    a.plot([2.75,6.9],[4.0,4.5],color=C[0],lw=1.7)
    a.plot([.55,2.75],[.8,1.3],color=C[1],lw=1.7)
    a.plot([2.75,6.9],[1.3,.8],color=C[1],lw=1.7)
    for y in [4.,1.3]:
        a.plot([2.75,4.15],[y,2.66],color=C[2],lw=1.8,ls=(0,(2,2)))
    a.add_patch(Circle((4.35,2.65),.34,facecolor='#e8edf3',edgecolor='#354b60',lw=1.2))
    a.text(4.35,2.64,'X',ha='center',va='center',weight='bold')
    a.text(.35,4.5,r'$\ell$',ha='right',va='center')
    a.text(7.0,4.55,r'$\ell$',ha='left',va='center')
    a.text(.35,.8,r'$p$',ha='right',va='center')
    a.text(7.0,.8,r'$p$' if el else r'$N^*$',ha='left',va='center')
    a.text(3.22,3.62,r'$\gamma^*$',ha='center',fontsize=9)
    a.text(3.24,1.73,r'$\gamma^*$',ha='center',fontsize=9)
    a.text(3.9,4.94,'Elastic' if el else 'Proton dissociation',ha='center',weight='bold',fontsize=10)
fig.subplots_adjust(left=.03,right=.97,top=.91,bottom=.04,wspace=.23)
fig.savefig(D/'gamma_gamma_topologies.pdf',bbox_inches='tight');plt.close(fig)

# Figure 2: illustrative, self-contained numerical EPA flux calculation.
alpha=1/137.035999084; mp=.9382720813; me=.00051099895; mm=.1056583755

def flux_lepton(y,m,qmax=10.):
    if y<=0 or y>=1: return 0.
    qmin=m*m*y*y/(1-y)
    if qmin>=qmax:return 0.
    return alpha/(2*np.pi)*((1+(1-y)**2)/y*np.log(qmax/qmin)-2*(1-y)/y*(1-qmin/qmax))

def flux_p(y):
    if y<=0 or y>=1: return 0.
    qmin=mp*mp*y*y/(1-y)
    A=1+0.71/qmin
    factor=np.log(A)-11/6+3/A-1.5/A**2+1/(3*A**3)
    return max(0.,alpha/(2*np.pi)*(1+(1-y)**2)/y*factor)

def sgg(W,E,m):
    s=4*E*7000
    lo=W*W/s
    if lo>=1:return np.nan
    def f(t):
        y=np.exp(t)
        return flux_lepton(y,m)*flux_p(lo/y)
    v=quad(f,np.log(lo),np.log(.999999),epsabs=3e-8,epsrel=2e-3,limit=100)[0]
    return max(v,1e-300)*2*W/s
Ws=np.geomspace(20,1150,100)
fig,ax=plt.subplots(figsize=(6.8,2.72))
for (name,E,m),color in zip([('LHeC: 50 GeV $e^-$',50,me),(r'LH$\mu$C: 0.5 TeV $\mu^+$',500,mm),(r'LH$\mu$C: 1 TeV $\mu^+$',1000,mm),(r'LH$\mu$C: 2 TeV $\mu^+$',2000,mm)],C):
    vals=np.array([sgg(w,E,m) for w in Ws]);ax.plot(Ws,vals,color=color,lw=1.9,label=name)
ax.set(xscale='log',yscale='log',xlabel=r'$W_{\gamma\gamma}$ [GeV]',ylabel=r'$S_{\gamma\gamma}(W)$ [GeV$^{-1}$]')
ax.grid(alpha=.15,which='both');ax.set_ylim(2e-11,2e-3)
ax.legend(loc='lower left',fontsize=7,frameon=False)
fig.text(.99,.015,r'Illustrative EPA: $Q^2_{\ell,\max}=10$ GeV$^2$, DZ elastic proton flux',fontsize=7,ha='right')
fig.tight_layout(rect=(0,.05,1,1));fig.savefig(D/'photon_luminosity.pdf',bbox_inches='tight');plt.close(fig)

# Figure 3: kinematic thresholds, not production probabilities or cross-section curves.
labels=[r'$\tau^+\tau^-$',r'$W^+W^-$',r'$t\bar t$',r'$\widetilde H^+\widetilde H^-$ (250 GeV benchmark)']
vals=[2*1.77686,2*80.377,2*172.57,500]
fig,ax=plt.subplots(figsize=(6.8,1.92))
for i,(label,val,col) in enumerate(zip(labels,vals,C)):
    y=3-i
    ax.hlines(y,0,val,color=col,lw=3)
    ax.plot(val,y,'o',color=col,ms=5)
    ax.text(val+23,y,label,va='center',fontsize=8.5)
ax.set(xlim=(0,1100),ylim=(-.7,3.7),yticks=[],xlabel=r'Partonic threshold $W_{\gamma\gamma}^{\rm thr}=2m_X$ [GeV]')
ax.set_xticks([0,160,350,500,800,1000]);ax.grid(axis='x',alpha=.2)
for sp in ['top','right','left']:ax.spines[sp].set_visible(False)
fig.tight_layout();fig.savefig(D/'heavy_thresholds.pdf',bbox_inches='tight');plt.close(fig)
print('Generated 3 original figures and EPA numerical integration plot.')
