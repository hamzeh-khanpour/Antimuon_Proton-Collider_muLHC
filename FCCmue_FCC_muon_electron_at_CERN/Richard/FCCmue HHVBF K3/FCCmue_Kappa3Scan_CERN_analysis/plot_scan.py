#!/usr/bin/env python3
"""Plot verified cross sections and test the tree-level quadratic dependence."""
import argparse
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

from scan_grid import CHANNEL_IDS, ENERGIES, KAPPA_TENTHS, OBSERVED_ATLAS_CMS


GRID = sorted([k/10 for k in KAPPA_TENTHS] + [1.0])
STYLE = {'CC_HH': ('CC', '#1251A0', 'o', '-'),
         'NC_HH': ('NC', '#AC3A28', 's', '--'),
         'total': ('CC + NC', '#20232A', '^', '-.')}


def fit_curve(rows):
    k = np.array([r['kappa3'] for r in rows], dtype=float)
    y = np.array([r['sigma_fb'] for r in rows], dtype=float)
    err = np.array([r['sigma_mc_err_fb'] for r in rows], dtype=float)
    if (list(k) != GRID or not np.isfinite(y).all() or not np.isfinite(err).all()
            or np.any(y <= 0) or np.any(err <= 0)):
        raise ValueError('Expected the complete verified grid with positive rates and MC errors')
    design = np.column_stack((np.ones(len(k)), k, k*k))
    weighted = design/err[:, None]
    coefficients, _, rank, _ = np.linalg.lstsq(weighted, y/err, rcond=None)
    if rank != 3:
        raise ValueError('Quadratic fit is rank deficient')
    covariance = np.linalg.inv(weighted.T @ weighted)
    residuals = (y-design@coefficients)/err

    anchor = np.isin(k, [0.0, 1.0, 2.0])
    inverse = np.linalg.inv(design[anchor])
    anchor_coeff = inverse@y[anchor]
    anchor_cov = (inverse*err[anchor]**2)@inverse.T
    held = design[~anchor]
    held_err = np.sqrt(err[~anchor]**2 + np.einsum('ij,jk,ik->i', held, anchor_cov, held))
    pulls = (y[~anchor]-held@anchor_coeff)/held_err
    a, b, c = coefficients
    minimum = -b/(2*c) if c > 0 else None
    return dict(coefficients_ABC_fb=coefficients.tolist(),
                coefficient_covariance_fb2=covariance.tolist(),
                chi2=float(residuals@residuals), dof=len(k)-3,
                anchor_kappa3=[0.0, 1.0, 2.0], anchor_coefficients_ABC_fb=anchor_coeff.tolist(),
                held_out=[{'kappa3': float(x), 'pull': float(p)} for x, p in zip(k[~anchor], pulls)],
                max_abs_held_out_pull=float(np.max(np.abs(pulls))),
                min_kappa3_in_scan=float(minimum) if minimum is not None and -10 <= minimum <= 10 else None)


def plot_energy(eid, points, totals, out):
    channel_rows = {c: sorted((r for r in points if r['energy_id'] == eid and r['process_id'] == c),
                              key=lambda r: r['kappa3']) for c in CHANNEL_IDS}
    channel_rows['total'] = sorted((r for r in totals if r['energy_id'] == eid), key=lambda r: r['kappa3'])
    diagnostics = {c: fit_curve(channel_rows[c]) for c in CHANNEL_IDS}
    coeff = {c: np.array(diagnostics[c]['coefficients_ABC_fb']) for c in CHANNEL_IDS}
    coeff['total'] = coeff['CC_HH'] + coeff['NC_HH']
    diagnostics['sum_coefficients_ABC_fb'] = coeff['total'].tolist()
    if [r['kappa3'] for r in channel_rows['total']] != GRID:
        raise ValueError('Missing CC+NC totals')
    energy = channel_rows['CC_HH'][0]['sqrts_GeV']/1000
    fig, axes = plt.subplots(1, 2, figsize=(11.3, 4.4), layout='constrained')
    fig.suptitle(rf'$e^-\mu^+\rightarrow hh+X$ at $\sqrt{{s}}={energy:g}$ TeV'
                 r'  |  $P_{e^-}=P_{\mu^+}=0$, $C_V=C_{2V}=1$', fontsize=13)
    for ax, limits in zip(axes, ((-10.35, 10.35), (-0.8, 2.15))):
        ax.axvspan(*OBSERVED_ATLAS_CMS, color='#DDEDE6', zorder=0,
                   label='ATLAS+CMS observed 95% CL')
        ax.axvline(1, color='#737B86', lw=1.1, ls=':', label='SM coupling')
        x = np.linspace(max(-10, limits[0]), min(10, limits[1]), 600)
        visible_y = []
        for channel, rows in channel_rows.items():
            label, color, marker, line = STYLE[channel]
            k, y, err = (np.array([r[f] for r in rows]) for f in ('kappa3', 'sigma_fb', 'sigma_mc_err_fb'))
            use = (k >= limits[0]) & (k <= limits[1])
            visible_y.extend((y[use]+err[use]).tolist())
            yfit = np.polynomial.polynomial.polyval(x, coeff[channel])
            visible_y.extend(yfit.tolist())
            ax.plot(x, yfit, color=color, lw=1.3, ls=line)
            ax.errorbar(k[use], y[use], yerr=err[use], fmt=marker, ms=4.2, capsize=2,
                        color=color, label=label)
        ax.set_xlim(*limits)
        ax.set_ylim(0, max(visible_y)*1.10)
        ax.set_xlabel(r'$\kappa_3=\lambda_3/\lambda_3^{\rm SM}$')
        ax.set_ylabel(r'$\sigma_{hh}$ [fb]')
        ax.grid(axis='y', color='#DCE1E6', lw=.7)
    axes[0].set_title('Full scan', loc='left')
    axes[1].set_title('Near the SM', loc='left')
    axes[0].legend(fontsize=8, frameon=True, loc='best')
    for ext in ('pdf', 'png'):
        fig.savefig(out/f'kappa3_scan_{eid}.{ext}', dpi=300)
    plt.close(fig)
    return diagnostics


def main():
    here = Path(__file__).resolve().parent
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--report', type=Path, default=here/'reports/scan_report.json')
    p.add_argument('--outdir', type=Path, default=here/'plots')
    args = p.parse_args()
    report = json.loads(args.report.read_text())
    if report['status'] != 'COMPLETE' or report['validated_new_jobs'] != 88:
        raise SystemExit('Complete the 88 direct integrations and run scan.py collect before plotting.')
    args.outdir.mkdir(parents=True, exist_ok=True)
    diagnostics = {}
    for eid in ENERGIES:
        diagnostics[eid] = plot_energy(eid, report['points'], report['totals'], args.outdir)
        for channel in CHANNEL_IDS:
            d = diagnostics[eid][channel]
            print(f'{eid} {channel}: chi2/dof={d["chi2"]:.2f}/{d["dof"]}, '
                  f'max |held-out pull|={d["max_abs_held_out_pull"]:.2f}')
    (args.outdir/'quadratic_fits.json').write_text(json.dumps(diagnostics, indent=2, allow_nan=False)+'\n')
    print('Plots and fit diagnostics:', args.outdir)


if __name__ == '__main__':
    main()
