# Source and figure provenance — 20-page FCC-mue Higgs note

## Primary publicly verified

| Source | Status | Claims used |
|---|---|---|
| Krzysztof Piotrzkowski, arXiv:2610.40451v2, revised 5 Nov 2026 | PUBLIC SOURCE, consulted through arXiv PDF | FCC-mue concept, energy reach, v2 machine Table 1 luminosities; 0.60 TeV: 4.5×10^34, 0.98 TeV: 0.63×10^34 cm^-2 s^-1 |
| FCC Collaboration, FCC Feasibility Study Report Vol. 1, EPJC 85 (2025) 1468; DOI 10.1140/epjc/s10052-025-15077-x | PUBLIC SOURCE; publisher entry checked | Complementarity with FCC-ee Higgs physics; 2026 erratum acknowledged |
| Q.-H. Cao, K. Cheng, Y. Liu, X.-R. Wang, Phys. Rev. D 109 (2024) 073005 | PUBLIC SOURCE; APS page checked | Existing prior electron-muon hhWW phenomenology |
| PDG (2024), Higgs physics review Table 11.3 | PUBLIC SOURCE; table checked | BR(H→bb)=0.582 at 125 GeV |

## Original CERN user-provided calculation sources

| Local file | Status | Interpretation |
|---|---|---|
| `references/CERN_48Run_Original_REVIEW.zip` | AVAILABLE AND VERIFIED | Full 48-process/energy/polarization result CSV; source cards/logs and status |
| `data/cross_sections_48.csv` | AVAILABLE AND VERIFIED against source 48/48 | Complete uncut stable-Higgs LO σ, MC errors, events/seeds/jobs |
| `data/linear_fits.csv` | AVAILABLE (from prior audited report) | Eight slopes for absolute cross-section fit, not experimental errors |
| `figures/Figure_1_absolute_cross_sections.pdf` and `Figure_2_polarization_ratios.pdf` | AVAILABLE, original-data-derived vector plots | Absolute cross sections and ratios at exact 1 and 2 TeV |
| `figures/original_mg5/{CC_H,CC_HH,NC_H,NC_HH}_matrix.pdf` | AVAILABLE, original MG5 vector files | Original full-process Feynman diagrams (1,4,1,4 graphs) |
| `figures/{CC_HH,NC_HH}_diagrams_cropped.pdf` | AVAILABLE; vector crops, original content preserved | Figure in note page 9 |
| `references/CC_HH4b_Historical_Review_20261025.zip` | AVAILABLE; data read in project slide audit | Historic FCC-mue and mu+mu- resonant/complete νν4b |
| `references/NC_ThreeProcess_Audit_20261027.pdf` | AVAILABLE; earlier audit | NC-4b/bbH/HH channels and unresolved discrepancy |
| `references/MuC_ZH_4b_Wide80_130_20261029.pdf` | AVAILABLE; historic result report | Resonant muon collider ZH→4b at 1 and 2 TeV |
| `figures/Figure_FCCmue_concept_schematic.pdf` | AVAILABLE, source-inspired redrawing, not original proposal figure | Machine concept; not to scale |

## Explicit limitations

- The primary public FCC-mue proposal PDF was consulted online but is not copied into this ZIP. The accelerator drawing is a self-produced schematic with attribution, not reused original artwork.
- The old resonant HH→4b model card contains BR(H→bb)=0.844640, not precision-SM ≈0.582. The historical rates retain their native normalization.
- NC full 4b (0.007713 fb) below separately generated bbH (0.012925 fb) is an unresolved consistency issue, **not** claimed to be an understood interference effect.
- No independent CERN reruns, higher-order corrections, HHH production or coupling-likelihood projection were performed during article creation.
- “Preliminary” is intentional: MC integration error is not a measurement/theory uncertainty.
