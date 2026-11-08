# FCC-mue Higgs Physics Kick-off — Rebuild instructions

## Contents

- `FCCmue_Higgs_Physics_Kickoff_2026.tex`: complete editable 48-page AGH Beamer presentation (40 main + 8 backups)
- `FCCmue_Higgs_Physics_Kickoff_2026.pdf`: compiled 16:10 slide PDF
- `beamerthemeAGH.sty`, `beamercolorthemeAGH.sty`: **original supplied AGH themes**
- `figures/`: original MG5 `matrix.pdf` files, vector crops, two source-data polarization plots, additional vector graphics, PNG plot exports
- `data/cross_sections_original_CERN.csv`: untouched original CERN 48-row result CSV
- `data/cross_sections_48.csv`: validated 48-row plotting dataset, numerically matched with original
- `data/historical_cross_sections.csv`: labelled historical 4b fiducial summary; see source caveats
- `scripts/`: sources to regenerate all graphics and the editable LaTeX deck
- `references/`: original user-supplied AGH template and relevant CERN review reports
- `SOURCE_MANIFEST.md`, `SCIENTIFIC_QA_REPORT.md`, `SLIDE_CONTENT_MAP.md`

## Requirements

TeX Live with `pdflatex`, `beamer`, `tikz`, `booktabs`, `hyperref`, `lmodern`; optional `latexmk` (used here). Python 3.9+ with `matplotlib`, `numpy`, `PyMuPDF` (the PyMuPDF import is `fitz`) for regenerating all figures. The `pandas` package is **not** required. Figures and original diagrams are already included, so Python is not needed merely to recompile.

## Build from the extracted ZIP

From this project directory:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error FCCmue_Higgs_Physics_Kickoff_2026.tex
pdfinfo FCCmue_Higgs_Physics_Kickoff_2026.pdf | grep Pages
```

Expect **48 PDF pages**, exactly **40 main** and **eight backup** frames. The theme is the original AGH 16:10 theme, with no externally downloaded logo file needed.

## Regenerate analysis figures and slides (optional)

```bash
python3 -m pip install numpy matplotlib pymupdf
python3 scripts/create_assets.py
python3 scripts/plot_fccmue_publication.py --data data/cross_sections_48.csv --out figures --dpi 400
python3 scripts/build_deck.py
latexmk -pdf -interaction=nonstopmode -halt-on-error FCCmue_Higgs_Physics_Kickoff_2026.tex
```

`create_assets.py` does **not** regenerate MadGraph physics; it crops original **vector** MG5 PDFs for layout and draws source-labelled auxiliary schematics. `plot_fccmue_publication.py` uses the genuine 48-row CERN dataset. `build_deck.py` generates exactly the 48 slides and `data/historical_cross_sections.csv`.

## Scientific boundaries

- The inclusive scan is at exactly 1/2 TeV, while earlier FCC-mue four-bottom simulations used 0.980/1.913 TeV machine-like energies.
- The former uses stable Higgs bosons and no generation-level kinematic cuts; historic four-bottom channels use explicit fiducial selections, and the older resonant samples use a nonstandard `BR(H->bb)=0.844640` model input.
- All 48 generator jobs completed, **but independent-seed convergence, complete NC-4b/associated-H internal consistency, and realistic detector-level coupling sensitivity are still outstanding**.
- The FCC-mue machine figure in this deck is an original **schematic redrawn after** the proposal, **not** the author's original accelerator-layout figure. The original PDF layout is linked in `SOURCE_MANIFEST.md`.
- HHH and kappa-coupling scans are **proposed work only**. No projected bounds or HHH cross sections were invented.
