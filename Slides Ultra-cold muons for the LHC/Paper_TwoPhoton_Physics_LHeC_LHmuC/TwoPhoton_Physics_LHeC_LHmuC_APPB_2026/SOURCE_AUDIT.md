# Source and result audit — 30 October 2026

**Status terms:** `Web verified` = source metadata, abstract or published text checked on the web; `Conversation only` = number supplied in this conversation/earlier assistant summary but not verified against recoverable numerical file; `Generated` = new reproducible local diagram/model calculation.

| Statement/figure | Source | Configuration/cuts | Verification | Action before publication |
|---|---|---|---|---|
| LHeC reference: 50 GeV electron, 7 TeV proton, ~1.18 TeV | Forthomme et al., PoS(DIS2024)269, sec. 1 | Reference beams | **Web verified** (`https://pos.sissa.it/469/269/pdf`) | Confirm final machine scenario as appropriate |
| Earlier LHmuC: 0.5 TeV muon, 7 TeV proton, ~3.74 TeV | Earlier project discussion and 2026 conference abstracts | Nominal beams | **Web/context verified** | Identify baseline figure versions |
| Higher energy LHmuC: 1 and 2 TeV muon; 5.3 and 7.5 TeV; instantaneous luminosity near 1e34 | Piotrzkowski arXiv:2610.35154, abstract | Machine proposal, not integrated event sample | **Web verified (abstract only)** | Read and audit full paper when accessible |
| EPA convolution and elastic proton flux | Budnev et al., Phys. Rep. 15 (1975) 181; Drees & Zeppenfeld, PRD39 (1989) 2536 | Quasi-real collinear EPA | **Web verified literature, equations checked dimensionally** | Crosscheck conventions/virtuality cuts of author's source paper |
| Photon/proton inelastic structure functions | Manohar et al., PRL117 (2016) 242002 and JHEP 12 (2017) 046 | Structure-function approach | **Web verified** | Choose explicit implementation for quantitative fits |
| `figures/gamma_gamma_topologies.pdf` | `make_figures.py` | Diagram schematic only | **Generated** | Not a borrowed paper figure |
| `figures/photon_luminosity.pdf` | `make_figures.py`; Eq. (3); DZ elastic proton approximation | E_e=50 GeV, E_mu=0.5/1/2 TeV, E_p=7 TeV, Q2_l,max=10 GeV2 | **Generated** | Illustrative only. Recompute with author's photon and acceptance definitions for final forecasts |
| Tau elastic cross sections: 50.40, 58.5, 70.3 pb | Prior presentation revision in this conversation | Source cuts not recoverable; baseline energies 1.2/3.7/5.3 TeV | **Conversation only** | Check W0, Q2, elastic selection, collider configuration and numerical precision |
| Tau dipole example delta a_tau=0.008 and 5e-4 | Earlier dedicated tau study and updated draft described in conversation | Different illustrative EFT benchmarks | **Conversation only** | Recover original labelled curves before adding plots/limits |
| WW elastic cross sections 0.037, 0.166 pb | Earlier workshop slide discussions | LHeC 1.2 TeV, LHmuC 3.7 TeV, exact cuts not recoverable | **Conversation only** | Verify matching cuts. Event estimates calculated as sigma x 250 fb^-1, not detector yields |
| Example f_M2/Lambda^4 = 1 TeV^-4 | Earlier aQGC slide and original draft | EFT benchmark, not limit | **Conversation only** | Check operator basis, coefficient convention and relevant sqrt(s) |
| High-M_WW EFT effects and validity | Eboli et al. PRD74 (2006) 073005; Eboli & Gonzalez-Garcia PRD93 (2016) 093013 | Dimension-eight operator scheme | **Web verified literature** | Quantify EFT truncation and unitarity before exclusion study |
| `figures/heavy_thresholds.pdf` | `make_figures.py` | Illustrative m_higgsino = 250 GeV | **Generated** | Not predicted event rates/exclusions |

## Unavailable primary materials

The original PDFs and ZIP were identifiable in Project file history, but attempts to retrieve their original bytes failed with `The requested Library file does not have a downloadable backing file yet.` They are intentionally **not** included in this final ZIP. No figures are misattributed as originating from these files.

## Journal formatting

Official APPB class source URL was checked through website metadata but could not be downloaded into the current container. A **portable article-class layout** has been supplied; exact journal class compliance and page count require fresh verification after applying the official class.

## Publication readiness

**Not ready for direct submission:** pending author's final numerical cross-check, source-figure restoration if desired, full collider-paper examination, official class replacement, authorship/affiliation sign-off, and conference submission instructions.
