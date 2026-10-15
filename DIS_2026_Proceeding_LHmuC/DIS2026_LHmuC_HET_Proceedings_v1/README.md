# DIS2026 HET proceedings source project

This project builds **Perspectives for HET physics studies at a muon-hadron collider at CERN**, by Hamzeh Khanpour, on behalf of HELP4CERN Study Group.

The delivered author-review draft has **seven PDF pages**, including its title/abstract page and references. The HELP4CERN numerical results are retained as instructed; the separate validation note records the deferred scientific issues. This is not a submission or an assertion of collaboration approval.

## Build

Extract the ZIP, enter its `DIS2026_HET_Proceedings_Source` directory, and run:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error DIS2026_HET_Proceedings.tex
```

The build produces `DIS2026_HET_Proceedings.pdf` in that directory. It uses pdfLaTeX and a manual bibliography in `references.tex`; BibTeX and Biber are not required. Without latexmk, run pdfLaTeX repeatedly until references and labels stabilize.

Verified environment: pdfTeX 1.40.25 (TeX Live 2023/Debian) and latexmk 4.83. A complete TeX Live or MiKTeX installation with the packages required by the supplied PoS style is appropriate. Required packages include `newtx` (`newtxtext` and `newtxmath`), `newtxtt`, `amsmath`, `amsthm`, `graphicx`, `natbib`, `caption`, `xcolor`, `hyperref`, `booktabs`, `tabularx`, `expl3`, and `xparse`, together with their normal dependencies. The verified environment additionally installed the official CTAN packages `mweights`, `kastrup` (for `binhex.tex`), and TeX Gyre fonts; the `newtx`, `newtxtt`, `qhv`, and `qtm` font maps were enabled. Use the TeX distribution's package manager to supply missing dependencies. No font substitution or style modification is needed.

## Files

- `DIS2026_HET_Proceedings.tex`: main manuscript entry point.
- `references.tex`: all 12 bibliography entries, with DOI/arXiv hyperlinks where verified.
- `pos.sty` and `PoSlogo.pdf`: unchanged supplied template files.
- `figures/dis_eta_acceptance.pdf`: original HELP4CERN kinematic-coverage figure.
- `figures/LHmuC_vector.pdf`: original HELP4CERN vector-coupling panel.
- `figures/Sgg.jpg` and `figures/yytautau.jpg`: original DIS2026 photon panels.
- `DIS2026_HET_Validation_and_Deferred_Corrections.md`: validation, provenance, and deferred-corrections record.

The main TEX file relies on these relative-path inputs. Download and extract the source ZIP to compile it; the separately delivered TEX file alone does not contain the graphics or style. The compiled PDF is delivered separately. Original source archives and temporary build products are deliberately excluded from this portable project.

The optional photon display is controlled by `\PhotonFiguretrue` in the main source. It is included in the delivered seven-page version. Any author edits require recompilation and a fresh page-count/layout check.

The supplied A4, 11-point PoS style and its geometry are unchanged. Public DIS2026 instructions confirm the inclusive seven-page limit and conference metadata. A conference-specific style package distributed privately to speakers was not available for equivalence checking; that limited formatting question remains documented in the companion note.
