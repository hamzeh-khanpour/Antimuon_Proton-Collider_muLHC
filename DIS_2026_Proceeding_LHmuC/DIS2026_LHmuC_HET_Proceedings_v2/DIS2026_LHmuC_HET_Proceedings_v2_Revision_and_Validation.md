# DIS2026 LHmuC HET proceedings v2 — revision and validation

Checked 15 October 2026. This note accompanies the scientific manuscript and is not part of its PDF.

## Inputs and revision scope

The active `DIS2026_LHmuC_HET_Proceedings_v2_Revision_Prompt(1).txt` was read in full. The supplied `DIS2026_LHmuC_HET_Proceedings_v1(1).zip` was inspected as the editing baseline, including its actual TEX, bibliography, PDF, six scientific assets, diagrams, style, logo, and stale README/build outputs. Original archives were preserved; v2 was implemented in a separate project.

Supporting inputs inspected were `HELP4CERN(3).zip`, `DIS_2026_Slides_LHmuC.zip`, and `Ultra-cold-muons_2026_TwoPhoton_LHmuC.zip`. The DIS2024 source manuscript was also read for the EPA/charged-pair context. ZIP CRC checks passed for these archives and v1. The active v2 specification governs the later table choices and eight-page allowance; no claim is made to have re-read an unavailable earlier HTML decisions report in this run.

The exact title, sole named author, HELP4CERN attribution, affiliation, publication email, and PoS speaker convention are preserved. Official workshop information confirms the 33rd DIS workshop, Bologna, 4–8 May 2026. No new simulation, event generation, fit, or sensitivity forecast was performed.

## Principal changes

- Rewrote the abstract, transitions, and conclusions around supported physics results and comparisons; corrected grammar and removed duplicated fit material.
- Preserved the author-adopted four-column production table and first-option/nominal-baseline/second-option machine table. The original five-energy-column HELP4CERN table was not reinstated. Captions distinguish fb from pb, lepton beam energies, source polarization information, and study-specific exposures.
- Explained the adopted single-top and top-pair gains over the 50 GeV LHeC entries. Nominal produced counts are explicitly before decays, acceptance, and selection.
- Kept the dedicated Higgs rate/coupling extraction separate from the combined fit, retained the external input and statistical formulae, and avoided assigning its second precision to the generic 1 ab⁻¹ machine sample.
- Combined the Higgs-fit discussion into one paragraph, with selected explicit LHeC comparisons, all three original panels, SMEFiT attribution, statistical-component rescaling, the κV ≤ 1 condition, and the definition 1 − κV(68%). Absolute branching-fraction constraints are distinguished from coupling uncertainties.
- Qualified the HL-LHC comparison using the specific primary report's explicit SM-width and zero-BSM-branching assumptions. This statement was checked independently; it was not inferred from BRBSM = 0 alone. No improvement factor was read from an unlabelled dashed line.
- Restored the absolute elastic WW rates before their approximately 4.5- and 7-fold comparisons. Preserved the tau-pair rates, EPA normalization, threshold/virtuality conditions, and all requested heavy/BSM channel names. Removed the claim about absent anomalous-deformation curves.
- Added compact EW/top and resonant μq/μg interpretation with a detector qualification. No unsupported numerical BSM reach was imported.
- Kept both editable Higgs diagrams and the source-supported CC charge conventions already adopted in v1. Removed conflicting redundant package loading, used ordinary float barriers to improve paragraph continuity, and rewrote the README from the actual v2 files. No style, page geometry, font-size reduction, scientific graphic redraw, or requested display omission was used.

## Provenance and numerical checks

| Content | Selected source and treatment |
|---|---|
| Production table and machine stages | Author-edited v1, checked against the DIS2026 presentation; values and units unchanged |
| Dedicated h→bb | HELP4CERN Higgs section and presentation; 1.19/0.69% rate precision, 0.77/0.60% coupling precision, and 0.985% external relative R uncertainty retained |
| Combined fit | Actual HELP4CERN fermion/vector/loop PDFs and fit text; all numerical statements checked against those panels |
| Coverage figure | Actual HELP4CERN `dis_eta_acceptance.pdf`; original 20/50 GeV electron and 1/2 TeV muon labels and acceptance conventions retained |
| Photon panels/rates | Original v1 panels are byte-identical to the DIS2026 and workshop versions; numerical rates checked against HELP4CERN and the presentation |
| EW/top and resonant BSM mechanisms | Relevant HELP4CERN text; qualitative statements retained with their assumptions |
| Reference metadata | Primary publication/arXiv records; HELP4CERN remains an in-preparation supplied draft with no invented identifier |

All six scientific graphics are byte-identical to v1; the coverage and three fit PDFs also match the selected HELP4CERN archive. The paired diagrams remain editable in `higgs_diagrams.tex`. Identically named graphics from other packages were not substituted.

Simple arithmetic was checked: single-top ratios 7.356 and 12.723, top-pair ratios 31.889 and 69.040, and WW ratios 4.486 and 6.973, rounded as stated. At 1 ab⁻¹, 36.77 and 2.23 pb imply 36,770,000 and 2,230,000 produced events. These are bookkeeping comparisons, not experimental precision forecasts. The adopted table cells, quoted coupling values, Higgs uncertainties, and photon rates were checked individually; no source-reported result was recalculated or replaced.

## Build, visual review, and distribution

The README documents the exact command:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error DIS2026_LHmuC_HET_Proceedings_v2.tex
```

The manuscript compiled successfully with pdfTeX 1.40.25 (TeX Live 2023/Debian) and latexmk 4.83, using the supplied PoS style and the documented standard TeX dependencies. No bibliography processor is required. Final references and labels stabilized: 13 bibliography entries, all cited; no missing citations, unresolved references, missing-character diagnostics, or overfull boxes. A benign underfull-vbox message remains on the coverage/diagram page; that page was visually inspected. Main-document fonts are embedded. The unchanged coverage PDF retains standard Base-14 font resources; no PDF/A certification is claimed.

**Measured PDF length: 8 pages**, including front matter and references. All eight pages were rendered and individually inspected for title/author metadata, readable panels, tables, diagram arrows/charges, equations, citations, headers, paragraph continuity, and clipping. No physical plot content is clipped. Pixel comparisons confirmed the final rebuild matches the visually reviewed rendering.

The distributed ZIP was extracted into a clean directory and built with the README command, using only the bundled project and documented TeX dependencies. The clean build succeeded with eight pages; extracted page text and all eight rendered pages matched the delivered PDF. The PDF embedded in the ZIP is byte-identical to the separate PDF. The archive has one v2 project directory, all required assets, and no old build products or input archives.

## Deferred scientific matters — unchanged policy

1. **Higgs/top benchmark metadata:** source versions differ in reference electron energies, polarization, and calculation assumptions. The selected v1 table is preserved. In particular, the 500 GeV Higgs values corresponding to 438 and 135 fb are explicitly unpolarized in HELP4CERN; a universal antimuon polarization is not assigned to the remaining entries. The differences have not been reconciled.
2. **Dedicated Higgs exposure:** the earlier arithmetic observation associates the quoted second h→bb precision approximately with 500 fb⁻¹ rather than the general 1000 fb⁻¹ benchmark. This remains a deferred issue, not an approved replacement exposure. The reported 0.69% result and other selected numerical results are unchanged.
3. **Same-named fit graphics:** other source packages contain different values in files with the same names. The HELP4CERN versions remain selected and their values are retained; no scientific resolution of the version differences is claimed.

The leptogluon source also has differing HL-LHC luminosity labels in prose and plot (1 versus 3 ab⁻¹). V2 uses a qualitative production-mechanism comparison and does not silently reconcile or quote that mass-reach comparison. Empty source placeholders for self-couplings or toponium were not imported as results.

## External qualifications

The [public DIS2026 proceedings instructions](https://dis2026.infn.it/workshop-proceedings/), rechecked on 15 October 2026, specify **seven pages for contributed talks**, including authors/abstract and bibliography. The delivered eight-page manuscript follows the author's current instruction; an organizer waiver has not been established, and compliance with the seven-page rule is not claimed. No administrative statement is inserted in the scientific article.

The supplied `pos.sty` (v2.2, 21 September 2021) and logo are unchanged. The private conference-specific template/instructions sent to speakers were not accessible, so equivalence to an unseen package cannot be certified. The talk title/date follow the supplied current project and its verified reference record; the Indico contribution page was blocked by an anti-bot wall during this run. The official public conference identity was accessible and checked.

For the HL-LHC width qualification, see [arXiv:2504.00672, Section 2](https://arxiv.org/html/2504.00672v1): the coupling extraction explicitly uses a SM width and vanishing BSM branching fraction. The retained André reference has DOI [10.1088/1367-2630/ae2e31](https://doi.org/10.1088/1367-2630/ae2e31) and [arXiv:2503.20475](https://arxiv.org/abs/2503.20475). No placeholder HELP4CERN arXiv identifier or unrelated photon-paper DOI was used.

This is a polished manuscript with the stated production checks, not evidence of collaboration approval, an external page waiver, or resolution of deferred source issues. Nothing was submitted and nobody was contacted.
