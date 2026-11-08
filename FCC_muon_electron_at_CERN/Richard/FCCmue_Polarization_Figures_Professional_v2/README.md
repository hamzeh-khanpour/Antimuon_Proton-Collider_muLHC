# FCC–μe Higgs polarization figures — publication-style v2

## Contents and provenance

The two plots are based **only** on the 48 real LO MadGraph configurations from CERN:
`FCCmue_Higgs_PolScan_full_exact_REVIEW.zip` (full/exact/both, 30,000 events per configuration).
The numerical file `cross_sections_48.csv` is copied **unchanged** from the audited results,
not digitized from a figure. Every row includes process, energy, polarization, cross section,
Monte Carlo integration uncertainty, random seed, event count, and status.

- `plot_fccmue_publication.py` — the **new standalone plotting program** (both figures).
- `cross_sections_48.csv` — all **48 cross sections and integration errors**.
- `linear_fits_from_audit.csv` — previously audited straight-line fits for all eight curves.
- `Figure_1_absolute_cross_sections.pdf` — high-quality *vector* PDF.
- `Figure_1_absolute_cross_sections.png` — 400-dpi raster figure.
- `Figure_2_polarization_ratios.pdf` — high-quality *vector* PDF.
- `Figure_2_polarization_ratios.png` — 400-dpi raster figure.
- `LaTeX_figure_blocks.tex` — copy-ready figure blocks with captions and labels.
- `original_build.py` — the original analysis plotting code used for the previous report **for archival reference only**; it contains paths specific to the original `/mnt/data` workspace and is not standalone.
- `original_cern_plot_results.py` — CERN package `plot_results.py` **for archival reference only**; expects output in `reports/cross_sections.csv` inside the CERN package.

## Run it on Windows PowerShell

1. Download and extract the ZIP; open a PowerShell terminal in the extracted directory containing `plot_fccmue_publication.py`.
2. Install Python packages if needed:

   ```powershell
   py -m pip install numpy matplotlib
   ```

3. Generate figures:

   ```powershell
   py .\plot_fccmue_publication.py
   ```

4. Optional higher PNG resolution and custom output directory:

   ```powershell
   py .\plot_fccmue_publication.py --dpi 600 --out .\figures
   ```

The script checks that it has exactly four processes × two energies × six polarizations, that
energies are exactly 1000 or 2000 GeV, and that every sigma and uncertainty is finite and positive.
It stops with an error rather than silently draw incomplete data.

## Run it on CERN LXPLUS

Plotting is *not* required for the physics integration. If numpy and matplotlib are available:

```bash
python3 plot_fccmue_publication.py
```

If not installed on the shared machine, run the script on Windows instead; it uses the included CSV.

## What to edit to customize the style

Open `plot_fccmue_publication.py` in VS Code or another editor:

- `PALETTE` — figure colors.
- `ENERGY_SPEC` — line styles, markers, and legend labels.
- `configure_style()` — fonts and label sizes.
- `make_canvas()` — title, margins, legend, and figure dimensions.
- `decorate_axis()` — axes, process headings, grids, and 80% reference guides.
- `make_absolute()` and `make_ratio()` — exactly how the data are drawn.

The 80% reference guide is only a visual marker and does not change any cross section.

## Physics and uncertainty definitions

**CC H:** `generate e- mu+ > ve vm~ h QCD=0`  
**CC HH:** `generate e- mu+ > ve vm~ h h QCD=0`  
**NC H:** `generate e- mu+ > e- mu+ h QCD=0`  
**NC HH:** `generate e- mu+ > e- mu+ h h QCD=0`

Beam 1: unpolarized e-. Beam 2: longitudinally polarized mu+. Polarization is scanned at
`0, 20, 40, 60, 80, 100` percent. The fixed beam-energy pairs are (125, 2000) GeV and
(200, 5000) GeV, respectively.

The cross-section points and integration uncertainties are as reported by the real CERN MG5 runs.
The straight lines are weighted fits to *sigma* vs polarization at each process/energy.
For the ratio plot:

`R(P) = sigma(P)/sigma(0)`.

For nonzero P the approximate error shown is standard uncorrelated propagation of the reported
integration uncertainties. At P=0 the ratio is exactly 1 by definition, and its error is set to 0.
This simple error propagation is for visualization, not a fully correlated covariance treatment.

**Scientific caveat:** completed CERN jobs with small integration errors are *not* an independent
seed-convergence or forward-region regulator/cut stability certification. The NC processes should
be checked for very-forward stability before these numbers are used as final published predictions.
These are LO, stable-Higgs, cut-free parton-level results (no Higgs branching fractions or detector effects).
