# Source manifest and attribution

## Source hierarchy

| Source | Availability / check | Scope |
|---|---|---|
| `https://arxiv.org/pdf/2610.40451v2` (K. Piotrzkowski) | **Read via authoritative web PDF; v2 dated 5 November 2026; external PDF itself not bundled** | FCC-mue concept, Table 1, machine parameters, running options, neutrino factory; cited on slides 4--9, B1 |
| `https://inspirehep.net/literature/3220545` | **User-provided primary bibliographic entry** | Proposal metadata |
| FCC Collaboration, *FCC Feasibility Study Report, Vol. 1*, EPJC 85 (2025) 1468, DOI 10.1140/epjc/s10052-025-15077-x | **Bibliography checked via public publisher page; paper not bundled** | FCC-ee complementarity, 240/365 GeV Higgs programme |
| Q.-H. Cao et al., *Measuring hhWW coupling at lepton colliders*, PRD 109 (2024) 073005 | **Journal publication checked** | Important prior e-mu double-Higgs / HHWW detector phenomenology; cited not treated as our own result |
| `references/CERN_48Run_Original_REVIEW.zip` | **Available, inspected; includes all 48 result records, process/run cards and quality files** | Source of original inclusive CC/NC H and HH cross sections |
| `data/cross_sections_original_CERN.csv` | **Extracted unchanged from review ZIP; compared numerically against plotting CSV in 48/48 rows** | Authoritative machine-readable inclusive results |
| `data/cross_sections_48.csv` | **Available, checked 48 unique rows and exact numeric agreement** | Publication figure data, slopes and source plots |
| `figures/Figure_1_absolute_cross_sections.pdf`, `Figure_2_polarization_ratios.pdf` | **Regenerated from genuine dataset; PDF vector** | 1/2 TeV inclusive Higgs polarization figures |
| `figures/original_mg5/{CC_H,CC_HH,NC_H,NC_HH}_matrix.pdf` | **Available original CERN-generated diagram PDFs; 1/4/1/4 diagram inventory** | Slides 15--18, B5; preserved original diagrams and numbers |
| `figures/{CC_H,CC_HH,NC_H,NC_HH}_diagrams_cropped.pdf` | **Vector crops of original PDFs; no redraw** | More readable layouts in slides |
| `references/CC_HH4b_Historical_Review_20261025.zip` | **Available; audited 16-row fiducial summary and provenance** | FCC-mue and muon-collider HH->4b/full neutrino4b comparisons |
| `references/NC_ThreeProcess_Audit_20261027.pdf` | **Available, read** | NC three-process results, cuts, unresolved discrepancy |
| `references/CC_NC_4b_Process_Inventory_20261028.pdf` | **Available, read** | Historical process definitions and channels |
| `references/AssociatedHiggs_Results_20261028.pdf` | **Available, with preliminary rate status** | Higher-energy polarized bbH rates |
| `references/MuC_ZH_4b_Wide80_130_20261029.pdf` | **Available, read** | Two resonant muon-collider ZH cross sections and fiducial uncertainties |
| `references/AGH_Original_Reference_Source.tex`, `AGH_Original_Reference.pdf` | **User-provided, inspected** | Authentic AGH 16:10 slide language |
| `beamerthemeAGH.sty`, `beamercolorthemeAGH.sty` | **User-provided, copied unchanged** | Exact original AGH Beamer styling |

## Key provenance distinctions

1. **Proposal revision:** The arXiv **v2** Table 1 reports peak luminosities of `4.5` and `0.63` in units of `10^34 cm^-2 s^-1` at 0.6 and 0.98 TeV, respectively. Earlier versions contain **different** luminosity benchmarks. Slide 7/B1 explicitly use v2 and cite it.
2. **Machine layout:** The original proposal Figure 1 was inspected via web PDF, but its image file was not available as a local editable/redistributable asset in the work environment. `Figure_FCCmue_concept_schematic.pdf` is an **original redrawn schematic, not to scale**, attributed to v2 Fig. 1; it must not be described as the proposal's original artwork.
3. **Inclusive versus fiducial:** The 48-run inclusive dataset uses uncut stable-H generators; the older HH->4b, NC four-bottom and ZH files have *different* cuts and branching-ratio conventions. They are never numerically combined as though identical.
4. **Old branching ratio:** A historical MadGraph parameter card uses `BR(H->bb)=0.844640`, rather than approximately 0.58 for a conventional precision-SM setup. The historical table is retained without pretending otherwise.
5. **Diagram verification:** Original MadGraph double-Higgs `matrix.pdf` exports contain diagrams 1 (contact), 2 and 3 (separate emissions), 4 (off-shell H*->HH). They must interfere in the full matrix element. The separate diagram subsets are not declared gauge invariant.
6. **Unverified physics:** Independent-seed convergence, neutral-current forward-region stability, and detector-level sensitivity projections were **not** executed for this slide-production task. The presentation labels them future checks.
7. **Triple Higgs:** HHH cross sections and quartic-Higgs precision projections were not part of completed CERN simulations; these appear exclusively as future research proposals.

## Citation and asset permissions

The journal and arXiv sources are cited as bibliographic sources; the deck includes a self-drawn accelerator schematic rather than reusing the source figure. User-provided project artifacts are included in the source package solely for reproducing this presentation. Original AGH theme credits/license are retained in its supplied `.sty` files (LPPL).
