# FCC-mue Higgs physics — 20-page scientific research note

## Files
- `FCCmue_Higgs_Physics_Research_Handout_20pages.tex`: editable, 12-pt A4 article source with embedded numbered bibliography.
- `FCCmue_Higgs_Physics_Research_Handout_20pages.pdf`: compiled 20-page A4 PDF.
- `figures/original_mg5/`: unmodified original CERN MadGraph diagram exports, plus `figures/*_diagrams_cropped.pdf` which are vector crops of the originals.
- `figures/Figure_1_absolute_cross_sections.pdf` and `Figure_2_polarization_ratios.pdf`: original CERN-data-derived vector plots.
- `data/cross_sections_48.csv`: complete 48-point inclusive scan, source cross sections/errors, random seeds and run IDs.
- `data/historical_cross_sections.csv`, `data/linear_fits.csv`: checked historical rates and fitted polarization slopes.
- `scripts/plot_fccmue_publication.py`: standalone original-data figure regeneration script (requires numpy and matplotlib).
- `references/`: source calculation archives and historic reports (user-provided project artifacts).
- `SOURCE_MANIFEST.md`, `SCIENTIFIC_QA_REPORT.md`: verification scope and limitations.

## Build the article
Install a reasonably complete TeX Live distribution with `pdflatex`, `latexmk`, and standard packages including `amsmath`, `mathtools`, `booktabs`, `subcaption`, `hyperref`, `fancyhdr`, `microtype`, `siunitx` and `lmodern`.

From the folder containing the TeX file:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error FCCmue_Higgs_Physics_Research_Handout_20pages.tex
pdfinfo FCCmue_Higgs_Physics_Research_Handout_20pages.pdf | grep -E 'Pages|Page size'
```

Expected: **20 pages**, A4 (595.276 × 841.89 pt). Compilation is offline; external literature PDF downloads are not needed to build this document.

## Regenerate numerical figures (optional)
Requires `numpy` and `matplotlib`. The numerical file is the fully audited 48-row original-source data. Run from the project root:

```bash
python3 scripts/plot_fccmue_publication.py --help
```

The plotting script supports an input CSV and output directory; see `--help` for options. Numerical figures already included can be used directly without Python.

## Scientific status
These are preliminary **leading-order** Standard Model cross sections, not an experimental prediction of Higgs-coupling precision. Historical four-bottom simulations used different cuts and a nonstandard model-card H→bb branching fraction; full-NC-4b/bbH normalization remains an open validation issue. HHH and anomalous-coupling scans are future studies, not completed computations.
