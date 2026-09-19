# Two-Photon Physics at the LHmuC - Ultra-cold muons for the LHC (2026)

**Author:** Hamzeh Khanpour, AGH University of Krakow  
**Workshop:** Ultra-cold muons for the LHC, 24-26 September 2026  
**Talk:** Two-Photon Physics  
**Number of slides:** 26

## Main files

- `Hamzeh_Khanpour_Ultra-cold-muons-for-the-LHC.tex` - editable LaTeX/Beamer source
- `Hamzeh_Khanpour_Ultra-cold-muons-for-the-LHC.pdf` - compiled 26-slide PDF
- `beamerthemeAGH.sty` and `beamercolorthemeAGH.sty` - original AGH Beamer theme
- `figures/` - all local figures needed by the presentation
- `README_PLACEHOLDERS.md` - documentation for the single intentionally retained detector-figure placeholder

## Compilation

A standard TeX Live installation with Beamer, TikZ and TikZ-Feynman is sufficient.

```bash
pdflatex Hamzeh_Khanpour_Ultra-cold-muons-for-the-LHC.tex
pdflatex Hamzeh_Khanpour_Ultra-cold-muons-for-the-LHC.tex
```

All figure paths are relative. No `/mnt/data` or other machine-specific path is required.

## Original slides / visual elements retained or adapted

The new deck was created by modifying the supplied `Ultra-cold-muons_2026_Slides_LHmuC` LaTeX project and retains its AGH theme, 16:10 layout, title-page design, section/header/footer structure, HELP4CERN branding, colour language and block styling.

The following concepts/visuals were retained or adapted from the original material:

- title and HELP4CERN branding
- LHmuC benchmark working points
- elastic gamma-gamma luminosity comparison
- tau-pair elastic cross-section plot
- gamma-gamma physics overview plot
- WW, ZZ and exclusive ttbar benchmark curves
- supersymmetric pair-production reference curves
- original Beamer/TikZ visual language

Generic QCD, broad Higgs, top-FCNC, RPV-squark and color-octet-muon sections were removed from the main talk to keep the 20-minute contribution focused on two-photon physics.

## Principal physics sources

1. `draft_yy_lhec.pdf` - newest detailed gamma-gamma material; used as the highest-priority source for updated tau moments, WW/ZZ aQGC discussion, compressed SUSY, LbL and exact-EPA comments.
2. `yy_lhec.pdf` - main EPA formalism, elastic/inelastic photon luminosities, lepton-pair calibration, and core gamma-gamma channel discussion.
3. `Hamzeh_Khanpour_a_tau_LHeC_LHmuC.pdf` - tau electromagnetic vertex and SMEFT interpretation.
4. The supplied Ultra-cold-muons / CERN / DIS2026 / HELP4CERN decks - LHmuC benchmarks, established cross sections and visual material.

## Scientific caution encoded in the deck

Several updated EFT plots in `draft_yy_lhec.pdf` are currently LHeC reference calculations. The slides explicitly label them as such and present the LHmuC extension as a motivated next step rather than silently relabelling LHeC results as LHmuC predictions.
