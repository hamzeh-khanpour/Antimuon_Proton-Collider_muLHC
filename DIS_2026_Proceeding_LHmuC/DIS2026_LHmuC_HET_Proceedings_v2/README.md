# DIS2026 LHmuC HET proceedings — v2

This project contains the revised manuscript **“Perspectives for HET physics studies at a muon-hadron collider at CERN”**, by Hamzeh Khanpour, on behalf of HELP4CERN Study Group.

## Build

Run from this project directory:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error DIS2026_LHmuC_HET_Proceedings_v2.tex
```

The output is `DIS2026_LHmuC_HET_Proceedings_v2.pdf`. The bibliography is supplied through `references.tex`; no BibTeX/Biber step is needed. All input paths are relative. No original source archive, external data file, absolute workspace path, or network connection is needed to build.

Use a complete TeX Live or MiKTeX installation with pdfLaTeX and latexmk. Required packages include the bundled `pos.sty`, `newtxtext`, `newtxmath`, `newtxtt`, TeX Gyre fonts, AMS packages, `graphicx`, `natbib`, `caption`, `xcolor`, `hyperref`, `booktabs`, `placeins`, PGF/TikZ, and `tikz-feynman`, together with their normal dependencies. The supplied PoS style and logo are unchanged.

The verified environment used pdfTeX 1.40.25 (TeX Live 2023/Debian), latexmk 4.83, PGF 3.1.10, TikZ-Feynman 1.1.0, newtxtext 1.744, newtxmath 1.754, and newtxtt 1.051. The Feynman diagrams use explicit coordinates and `\diagram*`; LuaTeX graph layout is unnecessary. Their manual-layout configuration avoids unused automatic-spacing defaults under pdfLaTeX.

## Contents

- `DIS2026_LHmuC_HET_Proceedings_v2.tex`: main editable manuscript.
- `DIS2026_LHmuC_HET_Proceedings_v2.pdf`: matching compiled manuscript, **8 PDF pages in total**.
- `references.tex`: all 13 cited references, including DOI/arXiv hyperlinks where applicable.
- `higgs_diagrams.tex`: editable paired CC/NC Feynman diagrams, included by the main file.
- `pos.sty`, `PoSlogo.pdf`: supplied PoS appearance and front matter.
- `figures/dis_eta_acceptance.pdf`: original HELP4CERN kinematic coverage figure.
- `figures/LHmuC_fermion.pdf`, `figures/LHmuC_vector.pdf`, `figures/LHmuC_loop.pdf`: the three selected original HELP4CERN coupling panels, combined in one manuscript figure.
- `figures/Sgg.jpg`, `figures/yytautau.jpg`: original photon panels retained from v1 and matched to the DIS2026 presentation.
- `DIS2026_LHmuC_HET_Proceedings_v2_Revision_and_Validation.md`: scientific provenance, changes, checks, deferred corrections, and external page-rule qualification.

The article contains two tables, four numbered figures (including both diagrams and all three coupling panels), and three numbered equations. All six scientific figure files are unchanged from v1. Ordinary build products are intentionally excluded from the distribution.

## Status

The eight-page output follows the author's current working allowance. The public DIS2026 limit for contributed talks remains seven pages, including front matter and references; no organizer waiver is established. See the companion note before submission.

Numerical corrections remain deferred. The polished manuscript preserves the adopted source results and distinguishes study-specific Higgs exposures, exploratory combined-fit assumptions, and general machine benchmarks. This package does not establish resolution of the source discrepancies or record any submission or collaboration approval.
