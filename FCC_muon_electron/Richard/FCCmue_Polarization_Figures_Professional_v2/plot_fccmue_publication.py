#!/usr/bin/env python3
"""Reproduce publication-quality FCC-mue Higgs production figures.

Inputs: the 48 genuine MadGraph results from CERN, in cross_sections_48.csv.
Output: two vector PDF figures plus high-resolution PNG copies.

Requires Python 3.9+, numpy, matplotlib. Does not alter data or run MadGraph.
Usage:
  python plot_fccmue_publication.py
  python plot_fccmue_publication.py --data cross_sections_48.csv --out figures --dpi 450
"""
from __future__ import annotations

import argparse
import csv
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use('Agg')  # works on CERN batch and Windows, no GUI required
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.ticker import AutoMinorLocator, MaxNLocator, FormatStrFormatter

HERE = Path(__file__).resolve().parent
PROCESSES = ['CC_H', 'CC_HH', 'NC_H', 'NC_HH']
ENERGIES = ['E1', 'E2']
POL_VALUES = np.array([0, 20, 40, 60, 80, 100], dtype=float)

# Both diagrams use the same channels, panel positions, and energy coding.
PALETTE = {
    'ink': '#152636',
    'muted': '#5b6b78',
    'grid': '#d8e0e5',
    'teal': '#006b80',
    'orange': '#d45c30',
    'reference': '#697784',
    'spine': '#aebbc5',
    'benchmark': '#b4c6cd',
}
ENERGY_SPEC = {
    'E1': dict(color=PALETTE['teal'], marker='o', linestyle='-', label=r'$\sqrt{s}=1$ TeV'),
    'E2': dict(color=PALETTE['orange'], marker='D', linestyle=(0, (5, 2)), label=r'$\sqrt{s}=2$ TeV'),
}
CHANNEL_LABELS = {
    'CC_H':  ('', 'CHARGED CURRENT   |   SINGLE HIGGS', r'$e^-\mu^+\;\to\;\nu_e\bar{\nu}_\mu H$'),
    'CC_HH': ('', 'CHARGED CURRENT   |   DOUBLE HIGGS', r'$e^-\mu^+\;\to\;\nu_e\bar{\nu}_\mu HH$'),
    'NC_H':  ('', 'NEUTRAL CURRENT   |   SINGLE HIGGS', r'$e^-\mu^+\;\to\;e^-\mu^+H$'),
    'NC_HH': ('', 'NEUTRAL CURRENT   |   DOUBLE HIGGS', r'$e^-\mu^+\;\to\;e^-\mu^+HH$'),
}


def read_data(path):
    with open(path, newline='', encoding='utf-8-sig') as fh:
        rows = list(csv.DictReader(fh))
    expected = {(p, e, int(pol)) for p in PROCESSES for e in ENERGIES for pol in POL_VALUES}
    found = {}
    for raw in rows:
        p, e, pol = raw['process_id'], raw['energy_id'], int(raw['polarization_percent'])
        k = (p, e, pol)
        if k in found:
            raise ValueError(f'Duplicate process/energy/polarization point: {k}')
        if raw['status'] != 'COMPLETED_UNVALIDATED':
            raise ValueError(f'Job is not a completed result: {k}: {raw["status"]}')
        sigma = float(raw['sigma_fb'])
        err = float(raw['sigma_mc_err_fb'])
        energy = float(raw['sqrts_GeV'])
        if not (np.isfinite(sigma) and np.isfinite(err) and sigma > 0 and err > 0):
            raise ValueError(f'Invalid cross section or MC integration uncertainty at {k}')
        if energy != (1000. if e == 'E1' else 2000.):
            raise ValueError(f'Unexpected sqrt(s) at {k}: {energy}')
        found[k] = (sigma, err)
    if set(found) != expected:
        raise ValueError(f'Expected 48 points; missing: {sorted(expected - set(found))}; extras: {sorted(set(found) - expected)}')
    return found


def arrays(data, p, e):
    vals = [data[p, e, int(pol)] for pol in POL_VALUES]
    return np.array([v[0] for v in vals]), np.array([v[1] for v in vals])


def weighted_line(x, y, dy):
    """Straight-line weighted least squares in fractional polarization."""
    x = np.asarray(x, float)
    X = np.column_stack((np.ones_like(x), x))
    W = 1 / np.asarray(dy, float)**2
    return np.linalg.solve(X.T @ (W[:, None] * X), X.T @ (W * y))


def configure_style():
    plt.rcParams.update({
        'font.family': 'DejaVu Sans',
        'font.size': 12.4,
        'axes.labelsize': 13.5,
        'xtick.labelsize': 11.6,
        'ytick.labelsize': 11.6,
        'axes.linewidth': 0.85,
        'mathtext.fontset': 'stix',
        'pdf.fonttype': 42,
        'ps.fonttype': 42,
        'savefig.facecolor': 'white',
        'savefig.edgecolor': 'white',
        'axes.unicode_minus': False,
        'lines.antialiased': True,
    })


def make_canvas(title, subtitle, bottomnote, kind):
    fig = plt.figure(figsize=(12.4, 9.0), facecolor='white')
    axes = fig.subplots(2, 2, gridspec_kw={
        'left': .095, 'right': .975, 'top': .742, 'bottom': .185,
        'wspace': .27, 'hspace': .65,
    }).flat
    fig.text(.095, .959, 'FCC–μe  /  HIGGS PHYSICS',
             fontsize=11, weight='bold', color=PALETTE['teal'], ha='left')
    fig.text(.095, .918, title, fontsize=23, weight='bold', color=PALETTE['ink'], ha='left')
    fig.text(.095, .883, subtitle, fontsize=11.7, color=PALETTE['muted'], ha='left')
    fig.add_artist(Line2D([.095, .975], [.862, .862], transform=fig.transFigure,
                          color=PALETTE['grid'], lw=1.2))
    handles = [
        Line2D([], [], color=ENERGY_SPEC[e]['color'], linestyle=ENERGY_SPEC[e]['linestyle'],
               marker=ENERGY_SPEC[e]['marker'], markersize=6.3, linewidth=2.0,
               markeredgecolor='white', markeredgewidth=0.6, label=ENERGY_SPEC[e]['label'])
        for e in ENERGIES
    ]
    if kind == 'ratio':
        handles.append(Line2D([], [], color=PALETTE['reference'], ls=':', lw=2.2,
                              label=r'SM CC: $R=1+P_{\mu^+}$'))
    fig.legend(handles=handles, loc='upper right', ncol=len(handles),
               bbox_to_anchor=(.977, .845), frameon=False, fontsize=11.8,
               handlelength=2.7, columnspacing=1.4, borderaxespad=0)
    fig.text(.095, .061, bottomnote, fontsize=10.8, color=PALETTE['muted'], ha='left')
    fig.text(.975, .061, 'MadGraph5_aMC@NLO  |  30,000 events / point',
             fontsize=10.4, color=PALETTE['muted'], ha='right')
    fig.add_artist(Line2D([.095, .975], [.091, .091], transform=fig.transFigure,
                          color=PALETTE['grid'], lw=.9))
    return fig, axes


def decorate_axis(ax, process, mode):
    letter, title, reaction = CHANNEL_LABELS[process]
    ax.text(0, 1.22, letter, transform=ax.transAxes, ha='left', va='center',
            fontsize=11, weight='bold', color='white',
            bbox=dict(boxstyle='round,pad=.34,rounding_size=.15',
                      facecolor=PALETTE['ink'], edgecolor='none'))
    ax.text(.078, 1.228, title, transform=ax.transAxes, ha='left', va='center',
            fontsize=11.1, weight='bold', color=PALETTE['ink'])
    ax.text(.00, 1.073, reaction, transform=ax.transAxes, ha='left', va='bottom',
            fontsize=15.2, color=PALETTE['ink'])
    ax.set_xlim(-3, 103)
    ax.set_xticks(POL_VALUES)
    if process in ('NC_H', 'NC_HH'):
        ax.set_xlabel(r'$P_{\mu^+}$ (%)', labelpad=9)
    ax.set_ylabel(r'$\sigma_{\rm LO}$ (fb)' if mode == 'absolute'
                  else r'$\sigma(P)/\sigma(0)$', labelpad=9)
    ax.grid(axis='y', linewidth=.75, color=PALETTE['grid'], alpha=.72)
    ax.grid(axis='x', visible=False)
    ax.tick_params(axis='both', colors=PALETTE['ink'], direction='out',
                   length=3.6, width=.85, pad=4)
    ax.spines[['top', 'right']].set_visible(False)
    ax.spines[['left', 'bottom']].set_color(PALETTE['spine'])
    ax.spines[['left', 'bottom']].set_linewidth(.9)
    ax.axvline(80, color=PALETTE['benchmark'], ls=(0, (2, 3)), lw=1.2, zorder=0)
    ax.set_axisbelow(True)
    if mode == 'ratio':
        ax.axhline(1, color=PALETTE['reference'], ls=(0, (2, 4)), lw=.85, alpha=.55, zorder=0)
        ax.set_ylim((.97, 2.075) if process.startswith('CC') else (.98, 1.265))
        ax.yaxis.set_major_locator(MaxNLocator(nbins=6, min_n_ticks=5))
    else:
        ymax = {'CC_H': 850, 'CC_HH': .92, 'NC_H': 53, 'NC_HH': .075}[process]
        ax.set_ylim(0, ymax)
        ax.yaxis.set_major_locator(MaxNLocator(nbins=5))
        if process == 'NC_HH':
            ax.yaxis.set_major_formatter(FormatStrFormatter('%.3f'))


def save(fig, out_dir, name, dpi):
    out_dir.mkdir(parents=True, exist_ok=True)
    pdf = out_dir / (name + '.pdf')
    png = out_dir / (name + '.png')
    fig.savefig(pdf)
    fig.savefig(png, dpi=dpi)
    plt.close(fig)
    print('Saved:', pdf)
    print('Saved:', png)


def make_absolute(data, out_dir, dpi):
    fig, axes = make_canvas(
        'Inclusive Higgs-production cross sections',
        r'LO Standard Model  ·  $\sqrt{s}=1$ and $2$ TeV  ·  unpolarized $e^-$ beam',
        'Full tree-level matrix elements  ·  Stable H/HH  ·  No imposed kinematic cuts',
        'absolute',
    )
    fine = np.linspace(0, 100, 161)
    for ax, p in zip(axes, PROCESSES):
        decorate_axis(ax, p, 'absolute')
        for e in ENERGIES:
            spec = ENERGY_SPEC[e]
            sigma, dsigma = arrays(data, p, e)
            a, b = weighted_line(POL_VALUES/100., sigma, dsigma)
            fitted = a + b * (fine/100.)
            ax.plot(fine, fitted, color=spec['color'], ls=spec['linestyle'],
                    lw=2.15, zorder=3)
            ax.errorbar(POL_VALUES, sigma, yerr=dsigma,
                        fmt=spec['marker'], markersize=6.0,
                        markerfacecolor=spec['color'], markeredgecolor='white',
                        markeredgewidth=.65, color=spec['color'],
                        ecolor=spec['color'], elinewidth=1.15, capsize=2.1,
                        capthick=1.1, zorder=5)
    save(fig, out_dir, 'Figure_1_absolute_cross_sections', dpi)


def make_ratio(data, out_dir, dpi):
    fig, axes = make_canvas(
        'Positive-muon polarization enhancement',
        r'Normalized to $P_{\mu^+}=0$  ·  matched process and collision energy',
        'Points: MadGraph results  ·  Curves: linear fits  ·  Vertical guides: 80% benchmark',
        'ratio',
    )
    fine = np.linspace(0, 100, 161)
    for ax, p in zip(axes, PROCESSES):
        decorate_axis(ax, p, 'ratio')
        if p.startswith('CC'):
            ax.plot(fine, 1 + fine/100., color=PALETTE['reference'], lw=2.2,
                    ls=':', zorder=2)
        for e in ENERGIES:
            spec = ENERGY_SPEC[e]
            sigma, dsigma = arrays(data, p, e)
            ref, dref = sigma[0], dsigma[0]
            ratio = sigma / ref
            # First point is exactly 1 by construction and is not independent of itself.
            dratio = np.hypot(dsigma/ref, sigma*dref/(ref*ref))
            dratio[0] = 0.
            a, b = weighted_line(POL_VALUES/100., sigma, dsigma)
            curve = (a + b * (fine/100.))/ref
            ax.plot(fine, curve, color=spec['color'], ls=spec['linestyle'],
                    lw=2.0, zorder=3)
            ax.errorbar(POL_VALUES, ratio, yerr=dratio, fmt=spec['marker'],
                        markersize=6.2, markerfacecolor=spec['color'],
                        markeredgecolor='white', markeredgewidth=.65,
                        ecolor=spec['color'], elinewidth=1.1, capsize=2.1,
                        capthick=1.05, zorder=5 if e == 'E1' else 6)
    save(fig, out_dir, 'Figure_2_polarization_ratios', dpi)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', type=Path, default=HERE / 'cross_sections_48.csv',
                        help='CSV with all 48 CERN cross-section points')
    parser.add_argument('--out', type=Path, default=HERE,
                        help='Directory for figure output')
    parser.add_argument('--dpi', type=int, default=400, help='PNG resolution (default: 400)')
    args = parser.parse_args()
    data = read_data(args.data)
    print(f'Loaded {len(data)} independent process/energy/polarization configurations')
    configure_style()
    make_absolute(data, args.out, args.dpi)
    make_ratio(data, args.out, args.dpi)


if __name__ == '__main__':
    main()
