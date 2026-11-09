# MEGA COMMAND — GENERATE THE FINAL FCC-μe HIGGS-PHYSICS BEAMER PRODUCTION MASTER PROMPT

**MISSION:** Produce a rigorous, fully executable, file-aware **MEGA MASTER PROMPT** that I can paste into a new, artifact-capable ChatGPT/model session to generate my complete scientific presentation. This request is a **prompt-engineering stage only**: write the FINAL MASTER PROMPT, **not** the slides now. The master prompt must subsequently cause the executing model to **produce the actual presentation files in the same session**, not merely explain how one might make them.

**Proposed presentation title:**
**Higgs Physics Potential of the FCC-μ⁺e⁻ Collider at CERN: From Standard Model Benchmarks to Higgs Self-Couplings**

**Meeting:** First scientific collaboration kick-off, November 2026 (exact date to be inserted only when provided).
**Presenter:** Hamzeh Khanpour, AGH University of Krakow.
**Meeting participants:** Hamzeh Khanpour, Krzysztof Piotrzkowski, Richard Ruiz, Piotr Kotko. Do not falsely represent everyone as a coauthor or speaker; show them as participants/collaborators until formal authorship is agreed.

## A. Required final outputs of the future production execution

The MASTER PROMPT you write **must** command production of all the following, not just a proposal or outline:

1. A complete and scientifically verified, **exactly 40-main-slide plus 8-backup-slide** AGH Beamer presentation, 16:10, with the required content below, substantive scientific details, actual cross-section results, appropriate equations and graphics, and clearly marked backup slides. If content density requires adjustment, use compact layouts and concise exposition without discarding requested results; report any true impossibility rather than passing off a partial deck as complete.
2. Separately downloadable, editable `FCCmue_Higgs_Physics_Kickoff_2026.tex` and compiled `FCCmue_Higgs_Physics_Kickoff_2026.pdf`.
3. `FCCmue_Higgs_Physics_Kickoff_2026_COMPLETE.zip` containing the `.tex`, `.pdf`, local AGH themes, all licensable/available required figures, original MG5 vector diagrams, numerical data, Python figure-generation scripts, a `README_BUILD.md`, a `SOURCE_MANIFEST.md` with citations/provenance, a `SCIENTIFIC_QA_REPORT.md`, and optional slide speaker notes.
4. Fully portable relative asset references (e.g. `figures/`, `data/`, `styles/` as appropriate) and a working TeX build command. No links to temporary absolute paths in the TeX itself. Preserve the original vector PDF figures where possible.
5. A verifiable PDF rendering: compile twice or as required, check log for errors and missing figures, confirm actual slide count and correct inclusion of backup frames, render/sample-inspect the opening, numerical tables, diagram slides, conclusion, and backups; fix overflow, tiny type, clipping, bad TeX symbols, and figure collisions. Do not claim tests that were not performed.
6. Actual, verified sandbox download links for the three main outputs. Do not fabricate paths. When a file is unavailable, make that limitation explicit and deliver as much as possible.

**NON-NEGOTIABLE:** No empty slide placeholders, no fake graph screenshots, no invented references, no fabricated scientific numbers, no simulated PDFs, no generic replacement theme, no mere text outline as the final deliverable. The complete source must compile offline with the provided local supporting files where technically possible.

## B. AGH Beamer style: reproduce the uploaded reference, not an approximation

The executing model must inspect, reuse and adapt these attached/reference files:

- `Hamzeh_Khanpour_Ultra-cold-muons-for-the-LHC.tex`
- `Hamzeh_Khanpour_Ultra-cold-muons-for-the-LHC.pdf`
- `beamerthemeAGH.sty`
- `beamercolorthemeAGH.sty`

The reference source explicitly contains:

```latex
\documentclass[aspectratio=1610,english]{beamer}
\usetheme[parttitle=rightfooter]{AGH}
\graphicspath{{figures/}{./}}
```

Retain the authentic AGH theme and visual language: section title bar, AGH green/red/black/white identity, institutional mark if actually provided, footer and slide numbering, distinctive blocks, readable typography, concise scientific captions, two-column layouts, exact proportions, and an AGH-style title page. Reuse source-level macros where appropriate, removing unrelated LHμC/γγ text. Do not silently substitute another Beamer template. Verify whether the reference source requires a separate `HELP4CERN.jpg`, AGH logo, or other assets; use them only when supplied or legitimately retrievable. Never claim a missing logo is included.

## C. Primary scientific sources and hierarchy

In the FINAL MASTER PROMPT instruct the executing model to inspect actual files and verify all external facts, giving priority to:

1. **Collider primary proposal:** INSPIRE `https://inspirehep.net/literature/3220545` and its linked paper `https://arxiv.org/pdf/2610.40451`. Read the text, figures, proposed machine parameters, luminosity assumptions and limitations; cite exact source/page in the presentation. Do not treat tentative projections as simulations already done by our team.
2. **Inclusive H/HH polarization:** `FCCmue_Higgs_Polarization_Results_Audit(1).pdf`, `FCCmue_Higgs_PolScan_full_exact_REVIEW.zip`, `FCCmue_Higgs_Polarization_Figures_v2_Source_Data.zip`, the 48-point `cross_sections_48.csv`, plotting code and the Figure 1/2 vector PDFs. The exact-energy scan uses `(E_e,E_{μ+})=(125,2000),(200,5000)` GeV and √s=1,2 TeV.
3. **MG5 original diagrams:** `FCCmue_All4_Original_MadGraph_Diagrams_LaTeX_Source.zip`, `FCCmue_All4_Original_MadGraph_Diagrams_Annotated.pdf`, and `FCCmue_Original_MadGraph_Diagrams_Verified_All4.zip`. Prefer unmodified original vector graphics over illustrative stock images. Preserve diagram numbering; attach source identification.
4. **Earlier FCC-μe/μ⁺μ⁻ HH→4b:** `FCC_ue_MuC_1TeV_2TeV_80Pol_Review_20261025.zip`, original LO cross-section reports, process/run cards and any other source files available in this project.
5. **NC 4b and associated H:** `FCCue_MuC_4b_Process_Inventory_20261028.pdf`, `FCC_ue_NC_ThreeProcess_Validation_Package_20261027.zip`, `FCC_ue_NC_4b_continuum_50k_preliminary_20261028.pdf`, and associated-bbH reports.
6. **Muon collider ZH→4b:** `MuC_ZH_to_4b_1TeV_2TeV_Wide80_130_for_Krzysztof_20261029.pdf` or the corresponding verified report.
7. **FCC-ee complementarity:** current FCC-ee design and Higgs-factory documents, reliable references on 240/365 GeV modes, and peer-reviewed related eμ/di-Higgs phenomenology, searched and cited with dates.
8. User-supplied reference slide deck/theme above.

If any referenced file is unavailable in the execution context, the MASTER PROMPT must direct the executing model to search the current Project files and conversation attachments, and then explicitly list any still-missing input; do not invent its contents or falsely say it was reviewed. The new model should use the attached files, not infer numerical content from old chat summaries if the primary records disagree. Distinguish **measured/generated**, **derived**, **literature-projected**, and **proposed/future** items.

## D. Physics facts and benchmarks that the master prompt must preserve and verify

### D1. Collider beam configurations

- FCC-μe earlier machine benchmarks: `(E_{μ+},E_e)=(2 TeV,120 GeV)` → √s≈0.9798 TeV; `(5 TeV,183 GeV)` → √s≈1.9131 TeV. Mention possible crossed combinations only when sourced in the proposal and label accurately.
- Exact-energy inclusive scan: `(2 TeV,125 GeV)` → exactly 1 TeV; `(5 TeV,200 GeV)` → exactly 2 TeV.
- Muon-collider comparisons: symmetric μ⁺μ⁻ beams at √s=1,2 TeV.
- At ultra-relativistic energies use `s≈4 E_e E_μ`. Do not silently conflate the two FCC-μe benchmark families.

### D2. The four inclusive processes and the 48-run campaign

Exact unrestricted MG5 commands:

```text
generate e- mu+ > ve vm~ h QCD=0
generate e- mu+ > ve vm~ h h QCD=0
generate e- mu+ > e- mu+ h QCD=0
generate e- mu+ > e- mu+ h h QCD=0
```

- Define **CC H**, **CC HH**, **NC H**, and **NC HH** unambiguously.
- Full LO SM tree-level amplitudes, stable H, unpolarized e⁻ beam, muon beam is MG5 **beam 2**, `P_{μ+}=0,20,40,60,80,100%`; no imposed generation kinematic cuts; two energies × four channels × six polarization settings = **48** real CERN HTCondor runs, 30,000 requested/generated events each.
- These numbers are **inclusive production** cross sections, not H→bb decay rates or detector-level signals.
- All 48 jobs completed, but internal MC integration errors are not a full theoretical/detector uncertainty, and independent-seed/forward-region studies remain necessary.

Principal verified cross sections, fb (show full 48-row CSV in numerical slides/backups):

| Channel | sqrt(s) | P=0% | P=80% | P=100% |
|---|---:|---:|---:|---:|
| CC H | 1 TeV | 210.540 | 378.570 | 421.150 |
| CC HH | 1 TeV | 0.0743838 | 0.1332298 | 0.1482390 |
| NC H | 1 TeV | 20.835 | 24.476 | 25.402 |
| NC HH | 1 TeV | 0.00962012 | 0.01130777 | 0.01172286 |
| CC H | 2 TeV | 386.010 | 695.000 | 772.690 |
| CC HH | 2 TeV | 0.418510 | 0.754495 | 0.839521 |
| NC H | 2 TeV | 38.991 | 45.829 | 47.642 |
| NC HH | 2 TeV | 0.0547116 | 0.0642989 | 0.0667703 |

The 8 fitted polarization slopes A defined by `σ(p)=a(1+A p)` with `p=P(%) / 100`:

| Process | A at 1 TeV | A at 2 TeV |
|---|---:|---:|
| CC H | 0.9982 ± 0.0020 | 1.0007 ± 0.0018 |
| CC HH | 0.9934 ± 0.0040 | 1.0053 ± 0.0039 |
| NC H | 0.2181 ± 0.0012 | 0.2208 ± 0.0011 |
| NC HH | 0.2186 ± 0.0022 | 0.2204 ± 0.0022 |

Theoretical check: CC `σ(P)/σ(0)≈1+p`; NC `σ(P)/σ(0)≈1+A_NC p`, with a weaker asymmetry governed mainly by the chiral Z couplings. The approximated `A_NC≈(g_L²−g_R²)/(g_L²+g_R²)` is scheme-dependent; verify weak-angle input before giving a numerical derivation. At +80% P, CC enhancement ≈1.8; NC ≈1.175. H→HH H* is **off-shell**.

### D3. Original MadGraph Feynman diagrams and Krzysztof's question

Krzysztof asked explicitly whether CC/NC HH matrix elements include **both** (i) H*→HH via λ3 and (ii) two Higgs bosons coupling separately to weak gauge bosons. The actual generated full LO matrices show **four diagrams per HH process**, including:

- Diagram 1: HHWW or HHZZ four-point contact vertex.
- Diagrams 2 and 3: separate Higgs emission with two HWW or HZZ couplings.
- Diagram 4: intermediate off-shell Higgs H*→HH and the trilinear Higgs self-coupling.

For the selected full SM process exports, CC H and NC H each show one tree-level fusion diagram. Diagrams are confirmed from **original generated CERN MadGraph files**, not external generic internet images. Stress that all contributions interfere in `|M_total|²` and that separate diagram cross sections have **not** been calculated. Diagram identification must be checked directly against the attached originals. Do not imply the listed four diagrams are a gauge-invariant decomposition individually.

### D4. Older CC HH→4b / full νν4b comparison

Fiducial: 4 bottom partons with `|η_b|<5`, two distinct opposite-charge bb pairs in `110<m_bb<130 GeV`, **no minimum b-parton pT cut**, parton-level (no detector). Verify pairing and treatment of flavour sums from source run cards.

| Collider | √s | HH→4b, P0/P80 (fb) | full νν4b, P0/P80 (fb) |
|---|---|---|---|
| FCC-μe | 0.980 TeV | 0.04912 / 0.08816 | 0.05355 / 0.09195 |
| μ⁺μ⁻ | 1 TeV | 0.07047 / 0.11582 | 0.07530 / 0.12472 |
| FCC-μe | 1.913 TeV | 0.26478 / 0.47611 | 0.28157 / 0.50745 |
| μ⁺μ⁻ | 2 TeV | 0.30624 / 0.54606 | 0.32480 / 0.57873 |

Important: Earlier HH→4b uses MG5 model-card `BR(H→bb)=0.844640`, **not** conventional SM ≈0.58. Must flag normalization issue before any realistic projection. Full 4b amplitude includes resonant/nonresonant diagrams and interference; **do not simply subtract** resonant sample from complete sample and claim physical background.

### D5. NC associated Higgs and four-bottom channels

Include explicit process definitions and cuts for `e−μ+→e−μ+HH→e−μ+4b`, `e−μ+→e−μ+bbH→e−μ+4b`, full `e−μ+→e−μ+bb bb`, and Higgs-excluded continuum diagnostic. Earlier NC fiducial samples include a **1 GeV outgoing-charged-lepton generation pT cut**, as well as the 110–130 GeV bb-pair windows; do not describe these as no-cut inclusive. Representative unpolarized √s≈0.980 TeV cross sections in fb: NC HH 0.006382; associated bbH 0.012925; complete 4b 0.007713; Higgs-excluded continuum 0.0008253, limited by 88/50,000 passing events. Verify all from archived source. Also cover the later +80% higher-energy associated-Higgs runs (FCC-μe ≈0.081843 fb at 1.913 TeV; μ+μ− ≈0.094913 fb at 2 TeV) only when process/cut definitions can be established. Do not add overlapping samples.

### D6. Muon-collider ZH→4b

`μ+μ−→ZH→(bb)(bb)` at √s 1,2 TeV (unpolarized), resonant decay-chain computation. Before/after fiducial cuts, fb:

- 1 TeV: **1.56450 → 1.52716**.
- 2 TeV: **0.37888 → 0.36929**.

Cut: `|η_b|<5` and **both** assigned bb masses in the wider **80–130 GeV** window; no minimum b-parton pT cut. Explain different topology from neutrino-associated HH and why flavour-off-diagonal μ+e− beams lack ordinary same-flavour s-channel ZH annihilation. Do not mix with 110–130 GeV selection tables.

### D7. Scientific rigor and what is NOT yet done

- Do **not** present Standard Model cross sections as an extraction of λ3, κ3, κ2V or λ4.
- Do **not** claim an HHH cross section exists. Both `e−μ+→νe ν̄μ HHH` and `e−μ+→e−μ+HHH` are proposed next-step calculations.
- Do **not** promote preliminary literature λ3 sensitivity figures as results of our MadGraph simulation.
- Higgs `HH` amplitudes contain H*→HH, HHVV and separate HVV contributions; interferences are central. For anomalous couplings require explicit HEFT/SMEFT assumptions and gauge-consistency checks.
- State the difference between pure theoretical 1+P rate enhancement and achievable gain given actual beam luminosity and polarization.
- Include independent random-seed tests, physical regulator/cut and forward-region review, electroweak model-card parameters, branching-ratio normalization, and detector simulation as future validation.

## E. REQUIRED slide plan — exactly 40 main + 8 backups

For every item below, the FINAL MASTER PROMPT must direct production of **a fully populated slide** containing the listed physics, mathematically correct notation, and a suitable original figure/table when valuable. No title-only slide or fake data. Every graph/table/important numerical claim should carry a concise source note within the slide or a consistent reference system.

### Part I: Collider concept (slides 1–9)

1. **Title slide** — Title, accurate presenter/participants, AGH, kick-off meeting, date only if known.
2. **Why this collaboration / meeting objectives?** — Scientific objectives and decisions needed; distinguish existing computations from future research.
3. **Outline** — Seven-section roadmap and what we will decide.
4. **Why FCC-μ+e−?** — Asymmetric lepton beams, multi-TeV reach, clean initial state, VBF, polarized μ+, complementary to e+e−/μ+μ−.
5. **The actual 2026 FCC-μe CERN proposal** — Layout, machine concept and correctly attributed original figure from arXiv/INSPIRE.
6. **Beam energies and √s: actual versus exact benchmarks** — All stated energy combinations, relation `√s≈2√(Ee Eμ)`, no conflation.
7. **Luminosity and staged running** — Values and design uncertainties from original proposal, instantaneous versus integrated luminosity explicitly separated.
8. **FCC-ee and FCC-μe complementarity** — FCC-ee precision (240/365 GeV etc.) versus high-energy VBF H/HH; coupling overlap and differences.
9. **Detector and operational challenges** — Lab boosts, forward lepton coverage, μ-decay backgrounds, beam-induced effects, 4b tagging and neutrinos.

### Part II: Methods and full channel inventory (slides 10–13)

10. **Portfolio of all completed Higgs processes** — A readable process map with CC/NC, H/HH, resonant and complete 4b, bbH, NC continuum, μ+μ− ZH.
11. **CERN MG5 workflow and reproducibility** — MG5 v3.6.4, original commands, LO, HTCondor 48 runs, seeds/integration uncertainties, actual validation.
12. **Inclusive versus fiducial quantities: never conflate** — Stable H no-cut; decay/cuts; two bb mass-window choices; parton versus detector levels.
13. **Polarization and EW/BR conventions** — MG5 e− beam1 μ+ beam2, 0 to +100%, model parameters and earlier 0.844640 H→bb note.

### Part III: Richard's inclusive H/HH polarization project (slides 14–26)

14. **The four exact inclusive MadGraph processes** — Four commands, full LO matrix elements, CC versus NC.
15. **Actual MG5 single-H diagrams** — Original CC H and NC H vector diagrams, HWW and HZZ.
16. **Actual MG5 CC HH diagrams** — 4 numbered originals, HHWW, separate-H, H*→HH.
17. **Actual MG5 NC HH diagrams** — 4 numbered originals, HHZZ, separate-H, H*→HH.
18. **Answer to Krzysztof: which HH amplitudes are included?** — Coherent `|M_contact+M_separate+M_λ3|²`, off-shell H, contact term, diagram caveats.
19. **Richard's 48-run scan: design and validation** — 4×2×6, beam energies, P values, requested events, quality controls.
20. **Complete 1 TeV inclusive cross-section table** — Six polarizations × four channels with actual errors and proper units.
21. **Complete 2 TeV inclusive cross-section table** — Same plus interpretation of energy scaling.
22. **Original absolute σ(P) figure** — Four-panel fully numerical high-quality vector PDF (not screenshot), legend, errors.
23. **Original enhancement R(P) figure** — Four-panel actual data with SM CC linear expectation and errors.
24. **Fitted slopes and goodness of fit** — All 8 A values, χ²/ndof and p values when sourced; precision caveats.
25. **Chiral weak-current interpretation** — W left-chirality/right-helicity μ+ selection; Z gL,gR; NC A≈0.22 with scheme caveat.
26. **Energy growth and projected raw yields** — Ratio 2 TeV/1 TeV H≈1.8–1.9 vs HH≈5.6–5.7; transparent hypothetical luminosity and no detector claim.

### Part IV: Earlier 4b and μ+μ− comparison portfolio (slides 27–35)

27. **CC HH→4b and full νν4b processes** — Explicit full generated final states, muon-collider neutrino flavours, what is resonant.
28. **4b fiducial cuts and pairing algorithm** — Four b |η|<5, two opposite-sign bb pairs, 110–130 mass windows, no min b pT; inclusive distinction.
29. **Full CC 4b comparison table** — All 4 colliders/energy configurations × P0/P80, HH vs full 4b; normalization warning.
30. **HH signal versus full 4b amplitude** — Resonant/singly/nonresonant/interference, caveat on diagram subtraction, what to simulate next.
31. **NC HH→4b, bbH→4b, full 4b and continuum** — Exact source definitions and NC 1 GeV outgoing-lepton pT cut.
32. **NC 4b benchmark cross-section table** — 0.006382,0.012925,0.007713,0.0008253 fb and statistics/caveats.
33. **Associated bbH at higher polarization/energy** — Verified higher-energy FCC-μe/μ+μ− samples, cuts, rate comparison and numerical limitations.
34. **Muon-collider ZH→4b at 1/2 TeV** — 1.56450→1.52716 and 0.37888→0.36929 fb; 80–130 mass windows.
35. **What the four-bottom studies establish—and what they do not** — Unified channel map, comparison caveats, priority backgrounds, experimental challenges.

### Part V: Higgs couplings and collaboration plan (slides 36–40)

36. **Higgs trilinear coupling and κ3–κ2V** — Higgs potential and HH diagrams, interference, coupling choices and model consistency.
37. **Differential information and EFT** — m_HH, Higgs pT, angular/lepton kinematics, HEFT vs gauge-invariant SMEFT and degeneracies.
38. **Proposed HHH production: feasibility and κ4** — CC/NC HHH MG5 commands, no existing rates, 1/2 TeV first tests, possible 6b/4b2τ/4b2γ, sensitivity threshold.
39. **Work packages and responsibilities to agree** — Validation, coupling scans, differential studies, detector/4b backgrounds, HHH, machine assumptions, milestones. Do not assign people unilaterally.
40. **Summary and decisions for the kick-off** — Top quantitative findings; 4–6 explicit decisions and next deliverables.

### Backup slides B1–B8 (not replacements for main slides)

B1. Exact FCC-μe machine parameters and sourced proposal figures.
B2. Exhaustive MadGraph process list, generation syntax and relevant model settings.
B3. 1 TeV complete data table: 24 inclusive values with errors/seeds.
B4. 2 TeV complete data table: 24 inclusive values with errors/seeds.
B5. Original all-four-process MG5 diagrams and diagram identifiers.
B6. Four-bottom pairing, cuts and normalization detail incl. BR(H→bb) and interference warnings.
B7. Reproducibility, integration, seed, card and forward-region checks.
B8. Full cited references, including FCC-μe proposal, FCC-ee, and prior eμ Higgs papers.

## F. Production quality specifications

- Each main slide must answer a clear scientific question, not simply repeat slide title in prose. Provide structured, readable content and a compact bottom-line statement when appropriate.
- Source all third-party figures; original collaboration plots/diagrams should carry `Our LO MadGraph calculations (preliminary)` rather than misleading journal attributions.
- Prefer high-quality vector images. Reproduce supplied plots from their 48 numerical values, not OCR or screenshots, with vector PDF exports; preserve scientific errors and honest uncertainties.
- Equations must be correctly normalized, units consistently in fb/pb and GeV/TeV, particle labels exactly correct (νe, anti-νμ; μ+), and polarization sign consistent with the positive antimuon convention.
- Avoid overfilled slides; use readable font sizes and AGH-safe 16:10 margins. Avoid tables with microscopic text or image clipping.
- Distinguish studies at √s≈0.980/1.913 from exact 1/2 TeV, and CC/NC inclusive versus fiducial or explicitly decayed samples.
- Strict references: sourced numbers, original figure origin, concise footnotes, and a bibliography. Do not fabricate DOI, publication status, authorship, or beam/luminosity specifications.
- Unresolved scientific issues are clearly flagged. Do not use unsupported Higgs self-coupling precision claims or turn preliminary HH→4b results into experimental sensitivities.
- Verify title/header/footer on rendered deck. Preserve the institutional style of the attached AGH slide source.

## G. Production execution, self-tests, and output contract

The MEGA MASTER PROMPT must instruct the executing model to perform, **in order**:

**Phase 0: Input audit.** Inventory attachments; locate primary proposal, Beamer template, actual diagrams, inclusive CSV and historical cross-section outputs; create a `SOURCE_MANIFEST.md` identifying which are actually available. Clearly label unavailable items.

**Phase 1: Source reconciliation.** Verify proposal claims against primary PDF and reliable outside sources, verify cross-section tables and run cards against original artifacts, check all process cuts and polarization schemes, and produce a numerical provenance table for each source figure and historical result.

**Phase 2: Figure preparation.** Copy original CERN diagrams, retain diagram IDs, regenerate both 48-point polarization figures from numerical CSV, prepare an accurate beam-energy figure and a cautious FCC-ee complementarity diagram, and prepare charts for older 4b/μ+μ− results if reliable data permit.

**Phase 3: Full AGH Beamer authoring.** Create real `.tex` and relative asset directory in a clean project. Implement exactly 40 main+8 backup substantive frames and relevant citations; cover with Hamzeh as presenter and four participants as participants; no false coauthorship.

**Phase 4: Compile and inspect.** Use `pdflatex`/`latexmk` or available suitable TeX engine; track logs; inspect rendering of full slide deck especially 16:10 aspect, diagrams, legends, tables, title page, logos, footers, source notes. Correct all compilation errors, missing graphics, illegible elements and overfull boxes. Include final PDF page count.

**Phase 5: Final scientific QA.** Verify process count, 48 numerical rows, 8 fit slopes, 4 CC/NC diagrams for each HH process, every cut and beam energy, every future-versus-completed statement, labels, units, and citation provenance. Provide a pass/fail checklist, noting genuine remaining caveats.

**Phase 6: Final deliverables.** Provide verified links for separately downloadable `.tex`, `.pdf`, and the complete ZIP; confirm its contents and that the PDF was actually compiled. Optionally include a short executive summary and slide-by-slide notes. Work must be completed in that same executing response; no promises of background work, no empty shell zip, no substituting uncompiled TeX for a PDF.

## H. Your ONLY task RIGHT NOW: write the master prompt

Write the **final, self-contained, copy-paste-ready** production prompt titled:

`FCCmue_Higgs_Physics_Kickoff_FINAL_PRODUCTION_MEGA_PROMPT`

Use strong operational instructions, clear file names, exhaustive accepted source and numerical constraints, phase-by-phase execution rules, slide titles and content, physics correctness requirements, failure handling, quality gates, and explicit output contracts. This output must be usable even when pasted into a new chat, provided the listed input files are attached or accessible.

**Do not actually generate the presentation in this step**. Do not ask me to reconfirm the number of slides or the deck style. Do not shorten the instructions to a generic prompt. Do not respond with only advice or an outline. Produce the **complete MASTER PROMPT** directly, with a closing instruction in it equivalent to `EXECUTE_PRODUCTION_NOW = YES` that triggers final slide production when I later paste that master prompt into an artifact-capable model.
