from pathlib import Path
import zipfile,io,csv,json,re,hashlib,math
import numpy as np
from scipy.stats import chi2
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator,MaxNLocator

SRC=Path('/mnt/data/FCCmue_Higgs_PolScan_full_exact_REVIEW.zip')
PKG=Path('/mnt/data/FCCmue_Higgs_PolScan_v1_1_CERN_PTL_FIX(1).zip')
OUT=Path('/mnt/data/FCCmue_results_audit')
Z=zipfile.ZipFile(SRC)
DATA=list(csv.DictReader(io.StringIO(Z.read('reports/cross_sections.csv').decode())))
for r in DATA:
 for k in ('sigma_fb','sigma_mc_err_fb','sqrts_GeV'):r[k]=float(r[k])
 for k in ('polarization_percent','n_events','seed'):r[k]=int(r[k])
PROC=['CC_H','CC_HH','NC_H','NC_HH']
PSTR={'CC_H':r'$e^-\mu^+\to\nu_e\bar\nu_\mu H$','CC_HH':r'$e^-\mu^+\to\nu_e\bar\nu_\mu HH$','NC_H':r'$e^-\mu^+\to e^-\mu^+H$','NC_HH':r'$e^-\mu^+\to e^-\mu^+HH$'}
COL={'E1':'#2165A3','E2':'#DA823B'}

def rows(e,p):return sorted((r for r in DATA if r['energy_id']==e and r['process_id']==p),key=lambda x:x['polarization_percent'])

checks=[];cut_fail=[];rerun=[]
for r in DATA:
 j=r['job_id'];audit=json.loads(Z.read(f'jobs/{j}/run_card_audit.json'));card=Z.read(f'jobs/{j}/process/Cards/run_card.dat').decode();log=Z.read(f'jobs/{j}/run.log').decode();proc=Z.read(f'jobs/{j}/process/Cards/proc_card_mg5.dat').decode()
 def v(k):
  x=re.findall(r'^\s*([^#!\n]+?)\s*=\s*'+re.escape(k)+r'\b',card,flags=re.M|re.I)
  return x[-1].strip() if x else None
 expected={'lpp1':0,'lpp2':0,'polbeam1':0,'polbeam2':r['polarization_percent'],'nevents':30000,'ebeam1':125 if r['energy_id']=='E1' else 200,'ebeam2':2000 if r['energy_id']=='E1' else 5000}
 for key,val in expected.items():
  if v(key) is None or abs(float(v(key))-val)>1e-6:cut_fail.append(f'{j} {key}: {v(key)} expected {val}')
 for k in ['ptl','ptheavy','mmll','mmnl','ptl1min','ptl2min','xptl']:
  if v(k) is not None and float(v(k))>0:cut_fail.append(f'{j} positive {k} cut {v(k)}')
 for k in ['etal','ptlmax','mmllmax']:
  if v(k) is not None and float(v(k))>0:cut_fail.append(f'{j} positive upper cut {k}: {v(k)}')
 if v('fixed_ren_scale')!='True' or abs(float(v('scale'))-125)>1e-6:cut_fail.append(f'{j} scale mismatch')
 pg=Z.read(f'jobs/{j}/process/Cards/param_card.dat').decode()
 if '1.250000e+02 # MH' not in pg:cut_fail.append(f'{j} Higgs mass not 125')
 if audit['set_values']['iseed']!=str(r['seed']):cut_fail.append(f'{j} seed audit mismatch')
 m=re.search(r'Using random number seed offset\s*=\s*(\d+)',log)
 if not m or int(m.group(1))!=r['seed']:cut_fail.append(f'{j} seed not in run log')
 generate={'CC_H':'generate e- mu+ > ve vm~ h QCD=0','CC_HH':'generate e- mu+ > ve vm~ h h QCD=0','NC_H':'generate e- mu+ > e- mu+ h QCD=0','NC_HH':'generate e- mu+ > e- mu+ h h QCD=0'}[r['process_id']]
 if generate not in proc:cut_fail.append(f'{j} process mismatch')
 if 'No need for second refine' not in log:rerun.append(j)
 if r['n_events']!=30000 or r['status']!='COMPLETED_UNVALIDATED':cut_fail.append(f'{j} status/events mismatch')
 checks.append(j)

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.titlesize':11,'axes.labelsize':10,'legend.fontsize':9,'pdf.fonttype':42,'ps.fonttype':42,'savefig.bbox':'tight'})

def formatter(ax):
 ax.grid(axis='y',linestyle='--',alpha=0.22)
 ax.spines[['top','right']].set_visible(False)
 ax.set_xlim(-4,104);ax.set_xticks([0,20,40,60,80,100]);ax.set_xlabel(r'$P_{\mu^+}$ (%)');ax.tick_params(direction='out')

fig,axes=plt.subplots(2,2,figsize=(11.8,8.1), constrained_layout=True)
for ax,p in zip(axes.flat,PROC):
 for e in ['E1','E2']:
  rs=rows(e,p);x=np.array([r['polarization_percent'] for r in rs]);y=np.array([r['sigma_fb'] for r in rs]);dy=np.array([r['sigma_mc_err_fb'] for r in rs]);
  ax.errorbar(x,y,yerr=dy,fmt='o-',capsize=2.3,lw=1.7,markersize=4.6,color=COL[e],label='1 TeV' if e=='E1' else '2 TeV',zorder=3)
 ax.set_title(PSTR[p]);formatter(ax);ax.set_ylabel(r'$\sigma_{\rm LO}$ (fb)');
 if p.endswith('HH'):ax.ticklabel_format(axis='y',style='plain',useOffset=False)
 ax.legend(loc='best',frameon=False)
fig.suptitle('FCC–μe | Inclusive Higgs production',fontweight='bold',fontsize=16)
fig.savefig(OUT/'Figure_1_absolute_cross_sections.pdf');fig.savefig(OUT/'Figure_1_absolute_cross_sections.png',dpi=300)
plt.close(fig)

fig,axes=plt.subplots(2,2,figsize=(11.8,8.1), constrained_layout=True)
for ax,p in zip(axes.flat,PROC):
 for e in ['E1','E2']:
  rs=rows(e,p);x=np.array([r['polarization_percent'] for r in rs]);b=rs[0]['sigma_fb'];db=rs[0]['sigma_mc_err_fb'];y=np.array([r['sigma_fb']/b for r in rs]);
  dy=np.array([0 if r['polarization_percent']==0 else math.hypot(r['sigma_mc_err_fb']/b,r['sigma_fb']*db/b**2) for r in rs]);
  ax.errorbar(x,y,yerr=dy,fmt='o',capsize=2.2,markersize=4.4,color=COL[e],label='1 TeV' if e=='E1' else '2 TeV',zorder=4)
  w=1/np.array([r['sigma_mc_err_fb'] for r in rs])**2; xx=np.array([r['polarization_percent']/100 for r in rs]); yy=np.array([r['sigma_fb'] for r in rs]);xm=np.array([0,1]);X=np.column_stack([np.ones(len(xx)),xx]); b_fit=np.linalg.solve((X.T*w)@X,(X.T*w)@yy)
  ax.plot([0,100],(b_fit[0]+b_fit[1]*xm)/b,lw=1.35,color=COL[e],alpha=.85)
 if p.startswith('CC'):
  ax.plot([0,100],[1,2],color='#444444',lw=1.2,linestyle='--',label=r'SM: $1+P_{\mu^+}$')
  ax.set_ylim(.96,2.07)
 else:ax.set_ylim(.98,1.255)
 ax.set_title(PSTR[p]);formatter(ax);ax.set_ylabel(r'$\sigma(P_{\mu^+})/\sigma(0)$');ax.legend(loc='upper left',frameon=False)
fig.suptitle('FCC–μe | Positive-muon polarization enhancement',fontweight='bold',fontsize=16)
fig.savefig(OUT/'Figure_2_polarization_ratios.pdf');fig.savefig(OUT/'Figure_2_polarization_ratios.png',dpi=300)
plt.close(fig)

fitrows=[]
for p in PROC:
 for e in ['E1','E2']:
  rs=rows(e,p);x=np.array([r['polarization_percent']/100 for r in rs]);y=np.array([r['sigma_fb'] for r in rs]);dy=np.array([r['sigma_mc_err_fb'] for r in rs]);w=1/dy**2;X=np.column_stack([np.ones(len(x)),x]);cov=np.linalg.inv((X.T*w)@X);a,b=np.linalg.solve((X.T*w)@X,(X.T*w)@y)
  err=np.sqrt(np.diag(cov));sl=b/a;grad=np.array([-b/a**2,1/a]);slope_err=float(np.sqrt(grad@cov@grad));chi=float(np.sum(((y-(a+b*x))/dy)**2));pval=float(chi2.sf(chi,4));
  ff={'process_id':p,'energy_id':e,'energy_GeV':1000 if e=='E1' else 2000,'intercept_fb':a,'intercept_err_fb':err[0],'derivative_fb_per_unit_p':b,'derivative_err_fb_per_unit_p':err[1],'relative_slope':sl,'relative_slope_error':slope_err,'chi2':chi,'ndof':4,'p_value':pval}
  fitrows.append(ff)
with (OUT/'linear_fits.csv').open('w',newline='') as f:
 d=csv.DictWriter(f,fieldnames=list(fitrows[0]));d.writeheader();d.writerows(fitrows)
with (OUT/'cross_sections_48.csv').open('w',newline='') as f:
 d=csv.DictWriter(f,fieldnames=['process_id','energy_id','sqrts_GeV','polarization_percent','sigma_fb','sigma_mc_err_fb','relative_mc_error_percent','job_id','seed','n_events','status']);d.writeheader();
 for r in DATA:
  d.writerow({k:(100*r['sigma_mc_err_fb']/r['sigma_fb'] if k=='relative_mc_error_percent' else r[k]) for k in d.fieldnames})
summary={'source_archive':SRC.name,'source_sha256':hashlib.sha256(SRC.read_bytes()).hexdigest(),'package_archive':PKG.name,'package_sha256':hashlib.sha256(PKG.read_bytes()).hexdigest(),'jobs_checked':len(checks),'job_count':len(DATA),'events_per_job':30000,'event_total':len(DATA)*30000,'unique_seeds':len(set(r['seed'] for r in DATA)),'card_validation_issues':cut_fail,'rerun_second_refinement_jobs':rerun,'fit_rows':fitrows,'caveats':['review archive omits full LHE event samples','seed in post-run run_card.dat equals 0; actual seed verified via run.log seed offset and run_card_audit.json','no independent-seed reruns yet','no independent forward-region cut/regulator stability scan yet','no ISR/beamstrahlung/Higgs branching/detector','MC integration errors only']}
(OUT/'independent_audit.json').write_text(json.dumps(summary,indent=2))
print('QA:',len(DATA),'issues',len(cut_fail),'second refine',rerun,'max relative stat err',max(r['sigma_mc_err_fb']/r['sigma_fb'] for r in DATA))
print('FITS:')
for d in fitrows:print(d['process_id'],d['energy_id'],'rel slope',d['relative_slope'],'err',d['relative_slope_error'],'p',d['p_value'])
