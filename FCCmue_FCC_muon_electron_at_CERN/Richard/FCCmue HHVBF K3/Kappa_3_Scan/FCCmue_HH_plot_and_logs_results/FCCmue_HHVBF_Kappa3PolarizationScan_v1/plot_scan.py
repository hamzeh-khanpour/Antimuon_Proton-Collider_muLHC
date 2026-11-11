#!/usr/bin/env python3
"""Plot measured grids and fits for the HH coupling and polarization scan."""
import argparse
import csv
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from matplotlib.ticker import MaxNLocator
import numpy as np

from scan_grid import CHANNEL_IDS, ENERGIES, EXPERIMENTAL_INTERVALS, KAPPA_GRID, POLARIZATIONS, jobs
from scan_results import sum_channels


CHANNEL_LABELS = {'CC_HH': 'CC', 'NC_HH': 'NC', 'total': 'CC + NC'}
LOWER = ((-1.35, 'CMS'), (-1.2, 'ATLAS'), (-0.71, 'ATLAS+CMS'), (-0.5, 'nearby'))
UPPER = ((5.8, 'nearby'), (6.1, 'ATLAS+CMS'), (6.37, 'CMS'), (7.2, 'ATLAS'))
BOUND_COLORS = {'CMS': '#ac3a28', 'ATLAS': '#1251a0', 'ATLAS+CMS': '#197350', 'nearby': '#77628c'}


def design(kappa, pol_percent):
    k, p = np.broadcast_arrays(np.asarray(kappa, dtype=float), np.asarray(pol_percent, dtype=float)/100)
    return np.stack((np.ones_like(k), k, k*k, p, p*k, p*k*k), axis=-1)


def fit_channel(rows, channel):
    lookup = {(r['kappa3'], r['polarization_percent']): r for r in rows}
    if len(rows) != len(KAPPA_GRID)*len(POLARIZATIONS) or set(lookup) != {
            (k, p) for k in KAPPA_GRID for p in POLARIZATIONS}:
        raise ValueError('Incomplete or duplicated channel grid')
    k, p, rate, err = (np.array([r[f] for r in rows], dtype=float) for f in
                        ('kappa3','polarization_percent','sigma_fb','sigma_mc_err_fb'))
    if not (np.isfinite(rate).all() and np.isfinite(err).all() and np.all(rate > 0) and np.all(err > 0)):
        raise ValueError('Fit requires finite positive rates and MC integration errors')
    x = design(k, p)
    weighted = x/err[:, None]
    coef, _, rank, _ = np.linalg.lstsq(weighted, rate/err, rcond=None)
    if rank != 6:
        raise ValueError('Polarization fit is rank deficient')
    cov = np.linalg.inv(weighted.T@weighted)
    pulls = (rate-x@coef)/err
    endpoint_checks, cc_checks = [], []
    for coupling in KAPPA_GRID:
        first, last = (lookup[coupling, v] for v in (0, 100))
        for pol in POLARIZATIONS[1:]:
            w = pol/100
            row = lookup[coupling, pol]
            v0, v1 = first['sigma_fb'], last['sigma_fb']
            e0, e1, e = first['sigma_mc_err_fb'], last['sigma_mc_err_fb'], row['sigma_mc_err_fb']
            if pol != 100:
                pred = (1-w)*v0+w*v1
                err_pred = np.sqrt(e**2+((1-w)*e0)**2+(w*e1)**2)
                endpoint_checks.append(dict(kappa3=coupling, polarization_percent=pol,
                                            pull=float((row['sigma_fb']-pred)/err_pred)))
            if channel == 'CC_HH':
                pred = (1+w)*v0
                cc_checks.append(dict(kappa3=coupling, polarization_percent=pol,
                                      pull=float((row['sigma_fb']-pred)/np.hypot(e,(1+w)*e0))))
    out = dict(coefficients_fb=coef.tolist(), covariance_fb2=cov.tolist(),
               chi2=float(pulls@pulls), dof=len(rows)-6,
               max_abs_fit_pull=float(np.max(np.abs(pulls))),
               endpoint_checks=endpoint_checks,
               max_abs_endpoint_pull=max(abs(r['pull']) for r in endpoint_checks))
    if cc_checks:
        out['cc_scaling_checks'] = cc_checks
        out['max_abs_cc_scaling_pull'] = max(abs(r['pull']) for r in cc_checks)
    return out


def predict(fit, kappa, pol_percent):
    return design(kappa, pol_percent)@np.asarray(fit['coefficients_fb'])


def save(fig, path):
    for ext in ('pdf','png'):
        fig.savefig(path.with_suffix('.'+ext), dpi=250, bbox_inches='tight', pad_inches=.08)
    plt.close(fig)


def caption(energy):
    return (rf'$e^-\mu^+\to hh+X$, $\sqrt{{s}}={energy:g}$ TeV'
            r'   •   $P_{e^-}=0$, $C_V=C_{2V}=1$')


def surfaces(eid, energy, rows, fits, out):
    k, p = np.meshgrid(np.linspace(-10,10,101), np.linspace(0,100,51))
    fig = plt.figure(figsize=(14.4,4.8), layout='constrained')
    fig.suptitle(caption(energy)+'\nMarkers: MC grid   •   Surfaces: fits', fontsize=13)
    for i, channel in enumerate((*CHANNEL_IDS,'total'),1):
        ax = fig.add_subplot(1,3,i, projection='3d')
        z = predict(fits[channel], k, p)
        upper = 1.04*max(float(z.max()), max(r['sigma_fb'] for r in rows[channel]))
        ax.plot_surface(k, p, z, cmap='viridis',
                        linewidth=0, antialiased=True, alpha=.77)
        ax.scatter([r['kappa3'] for r in rows[channel]],
                   [r['polarization_percent'] for r in rows[channel]],
                   [r['sigma_fb'] for r in rows[channel]], s=7, c='#1f252a', depthshade=False)
        ax.set(title=CHANNEL_LABELS[channel], xlabel=r'$\kappa_3$',
               ylabel=r'$P_{\mu^+}$ [%]', zlabel=r'$\sigma_{hh}$ [fb]',
               xlim=(-10,10), ylim=(0,100), zlim=(0,upper),
               xticks=(-10,-5,0,5,10), yticks=(0,20,40,60,80,100))
        ax.zaxis.set_major_locator(MaxNLocator(nbins=5))
        ax.view_init(elev=24,azim=-64)
    save(fig, out/f'polarization_surfaces_{eid}')


def contours(eid, energy, fit, out):
    fig, axes = plt.subplots(1,2, figsize=(10.8,4.6), layout='constrained')
    fig.suptitle(caption(energy)+'\nCC + NC', fontsize=13)
    lo, hi = EXPERIMENTAL_INTERVALS['ATLAS+CMS']
    for ax, limits, label in zip(axes, ((-10,10),(-1.5,3.0)), ('Full grid','Near the SM')):
        k,p=np.meshgrid(np.linspace(*limits,181),np.linspace(0,100,101))
        z=predict(fit,k,p)
        if label=='Full grid' and z.min()>0:
            m=ax.contourf(k,p,z,levels=np.geomspace(z.min(),z.max(),22),
                          norm=LogNorm(), cmap='viridis')
            bar=fig.colorbar(m, ax=ax, ticks=np.geomspace(z.min(),z.max(),6), format='%.2g')
            bar.set_label(r'$\sigma_{hh}$ [fb] (log scale)')
        else:
            m=ax.contourf(k,p,z,levels=20,cmap='viridis')
            bar=fig.colorbar(m,ax=ax)
            bar.set_label(r'$\sigma_{hh}$ [fb]')
        ax.axvline(1,color='white',ls=':',lw=1.2,label='SM coupling')
        for x in (lo,hi):
            if limits[0] <= x <= limits[1]:
                ax.axvline(x,color='#f8c566',ls='--',lw=1.3,
                           label='ATLAS+CMS 95% CL edges' if x==lo else None)
        ax.set(xlabel=r'$\kappa_3$',ylabel=r'$P_{\mu^+}$ [%]', title=label, xlim=limits,
               ylim=(0,100),yticks=POLARIZATIONS)
    axes[0].legend(loc='lower left',fontsize=8)
    save(fig,out/f'polarization_contours_{eid}')


def boundary_plots(eid, energy, fits, out):
    fig, axes=plt.subplots(1,2,figsize=(10.8,4.4),layout='constrained')
    fig.suptitle(caption(energy)+'\nFitted CC + NC rates near the observed 95% CL bounds',fontsize=13)
    pol=np.linspace(0,100,101)
    for ax, pts, label in zip(axes,(LOWER,UPPER),('Lower bounds','Upper bounds')):
        for k,source in pts:
            ax.plot(pol,predict(fits['total'],k,pol),color=BOUND_COLORS[source],
                    ls='--' if source=='nearby' else '-',lw=1.8,
                    label=rf'$\kappa_3={k:g}$ ({source})')
        ax.set(xlabel=r'$P_{\mu^+}$ [%]',ylabel=r'$\sigma_{hh}$ [fb]',title=label,
               xlim=(0,100),xticks=POLARIZATIONS)
        ax.grid(alpha=.23)
        ax.legend(fontsize=8)
    save(fig,out/f'polarization_near_limits_{eid}')
    output=[]
    for edge, pts in (('lower',LOWER),('upper',UPPER)):
        for k,source in pts:
            for p in POLARIZATIONS:
                x=design(k,p)
                for channel,fit in fits.items():
                    cov=np.asarray(fit['covariance_fb2'])
                    output.append(dict(energy_id=eid,sqrts_GeV=energy*1000,edge=edge,
                                       reference=source,channel=channel,kappa3=k,polarization_percent=p,
                                       fit_sigma_fb=float(predict(fit,k,p)),
                                       fit_mc_err_fb=float(np.sqrt(max(0,x@cov@x)))))
    return output


def main():
    here=Path(__file__).resolve().parent
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--report',type=Path,default=here/'reports/scan_report.json')
    p.add_argument('--outdir',type=Path,default=here/'plots')
    args=p.parse_args()
    report=json.loads(args.report.read_text())
    if (report['status'],report['validated_new_jobs'],report['reused_unpolarized_points']) != ('COMPLETE',len(jobs()),92):
        raise SystemExit('Collect the complete polarized grid before plotting.')
    expected={(e,c,p,k) for e in ENERGIES for c in CHANNEL_IDS for p in POLARIZATIONS for k in KAPPA_GRID}
    points=report['points']
    if len(points)!=len(expected) or {(r['energy_id'],r['process_id'],r['polarization_percent'],r['kappa3'])
                                     for r in points} != expected:
        raise ValueError('Report point list differs from the full 552-point grid')
    totals=sum_channels(points)
    if len(totals)!=276:
        raise ValueError('Expected 276 CC+NC sums')
    args.outdir.mkdir(parents=True,exist_ok=True)
    all_fits={}; limits=[]
    for eid,(electron,muplus) in ENERGIES.items():
        energy=2*np.sqrt(electron*muplus)/1000
        rows={c:[r for r in points if r['energy_id']==eid and r['process_id']==c] for c in CHANNEL_IDS}
        rows['total']=[r for r in totals if r['energy_id']==eid]
        fits={c:fit_channel(rows[c],c) for c in CHANNEL_IDS}
        fits['total']={k:sum(np.asarray(fits[c][k]) for c in CHANNEL_IDS).tolist()
                       for k in ('coefficients_fb','covariance_fb2')}
        all_fits[eid]=fits
        surfaces(eid,energy,rows,fits,args.outdir)
        contours(eid,energy,fits['total'],args.outdir)
        limits.extend(boundary_plots(eid,energy,fits,args.outdir))
        for c in CHANNEL_IDS:
            f=fits[c]
            print(f'{eid} {c}: chi2/dof={f["chi2"]:.1f}/{f["dof"]}, '
                  f'max |intermediate-polarization pull|={f["max_abs_endpoint_pull"]:.2f}')
    with (args.outdir/'near_limit_predictions.csv').open('w',newline='') as file:
        writer=csv.DictWriter(file,fieldnames=list(limits[0]));writer.writeheader();writer.writerows(limits)
    diagnostics={'coefficient_order':['1','kappa3','kappa3^2','P','P*kappa3','P*kappa3^2'],
                 'P_unit':'fraction, 1 = 100%', 'by_energy':all_fits}
    (args.outdir/'surface_fits.json').write_text(json.dumps(diagnostics,indent=2,allow_nan=False)+'\n')
    print('Plots and diagnostics:',args.outdir)


if __name__=='__main__':
    main()
