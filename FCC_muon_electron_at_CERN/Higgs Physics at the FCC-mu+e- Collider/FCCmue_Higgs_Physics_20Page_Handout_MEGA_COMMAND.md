# FINAL MEGA COMMAND — PRODUCE A 20-PAGE FCC-μ⁺e⁻ HIGGS-PHYSICS RESEARCH HANDOUT

## OPERATION: PRODUCE_FCCMUE_HIGGS_PHYSICS_20_PAGE_RESEARCH_NOTE

**EXECUTE_RESEARCH_AND_DOCUMENT_PRODUCTION_NOW = YES**  
**DELIVER_ACTUAL_EDITABLE_TEX_AND_COMPILED_PDF = YES**  
**TARGET_LENGTH = EXACTLY_20_A4_PDF_PAGES_INCLUDING_REFERENCES**  
**DOCUMENT_TYPE = ADVANCED_SCIENTIFIC_HANDOUT / PHENOMENOLOGY_RESEARCH_NOTE**  
**NO_SLIDES, NO_GENERIC_SUMMARY, NO_FABRICATED_RESULTS, NO_PLACEHOLDERS = YES**

You are acting as a senior collider-phenomenology researcher, electroweak/Higgs theorist, scientific editor, numerical-source auditor, professional LaTeX author, and PDF quality-control specialist. **Execute the entire task in this session.** Do not generate yet another prompt or only a chapter outline. Author a substantial, coherent, research-level 20-page physics note, compile it, inspect the finished PDF, correct errors, and provide separately downloadable `.tex` and `.pdf` files and a portable source ZIP. If files essential to a requested claim are missing, document the limitations and perform the best verifiable work possible; do not invent access or data.

### Document identity

- **Title:** *Higgs Physics at the FCC-μ⁺e⁻ Collider: Production Mechanisms, Polarization, Self-Couplings and a Collaborative Research Roadmap*
- **Subtitle:** *A scientific handout for the first FCC-μ⁺e⁻ Higgs-physics collaboration meeting*
- **Prepared by/presenter:** Hamzeh Khanpour, AGH University of Krakow.
- **Discussion participants:** Hamzeh Khanpour, Krzysztof Piotrzkowski, Richard Ruiz, Piotr Kotko. Do not automatically list these participants as publication coauthors.
- **Date:** November 2026; do not invent an exact meeting date.
- **Audience:** expert HEP phenomenologists and accelerator/collider physicists, including collaborators familiar with MadGraph, electroweak fusion, Higgs self-couplings, and effective field theory.
- **Genre:** standalone explanatory mini-review / internal collaboration scientific note. It must be useful independently of the slides; do not copy slide bullet points or frame formatting.

## A. EXACT FINAL FILES AND REPRODUCIBILITY CONTRACT

Create these verified files:

1. `FCCmue_Higgs_Physics_Research_Handout_20pages.tex` — complete, editable main LaTeX source.
2. `FCCmue_Higgs_Physics_Research_Handout_20pages.pdf` — genuinely compiled and visually checked PDF with **exactly 20 physical A4 pages, references included**.
3. `FCCmue_Higgs_Physics_Research_Handout_20pages_COMPLETE.zip` — complete portable project, containing the two main files, `figures/`, `data/`, `scripts/`, `references.bib` or equivalent, and `README_BUILD.md`, `SOURCE_MANIFEST.md`, `SCIENTIFIC_QA_REPORT.md`.

Use the exact filenames. Provide clickable download links **only after confirming those files actually exist**. Keep all graphics/inputs on relative paths so the ZIP rebuilds offline. Include source-data CSVs and plotting scripts needed for numerical figures. Include original MG5 vector-diagram assets when their source files are available and permission permits. If the PDF ends up not exactly 20 pages, revise responsibly by editing content and layout and compile again: no blank padding, artificial oversized text, microscopic unreadable text, hidden content, or falsified PDF page count. Count the title/abstract and bibliography in the 20 pages. Avoid extra uncounted appendix pages; use concise appendices within the same limit if needed.

**Layout:** A4 portrait, single-column, preferably 11-pt `article` or `scrartcl`, professional AGH-compatible academic identity (modest green/red accents, not a Beamer slideshow), comfortable margins (~20–23 mm), legible figures/tables, page numbers, running headers, numbered sections/equations, `hyperref`, `cleveref` if available, `booktabs`, `siunitx`, `amsmath`, `mathtools`, `microtype`, `graphicx`, and bibliography. Use traditional printed-scientific-paper typography, not a decorative brochure. If the supplied AGH theme is Beamer-specific, DO NOT force `beamerthemeAGH.sty` into an article document; use the AGH identity appropriately without compromising article compilation.

## B. READ THE REAL MATERIALS; USE A STRICT EVIDENCE HIERARCHY

**Mandatory available-input audit before writing:** Search attached current chat files, project files, and the supplied complete slide-package ZIP; inspect original contents rather than relying on previous conversational assertions. The two attached physics-roadmap Markdown documents are background guidance, not independent proof of the numerical simulations (they may be duplicates). Inventory and compare:

- `FCCmue_Higgs_Physics_Kickoff_2026_COMPLETE.zip` and/or the compiled 48-slide deck and its `SOURCE_MANIFEST.md`, `SCIENTIFIC_QA_REPORT.md`, `SLIDE_CONTENT_MAP.md`, diagram/CSV source assets.
- `FCCmue_Higgs_PolScan_full_exact_REVIEW.zip`, `cross_sections_48.csv`, `FCCmue_Higgs_Polarization_Results_Audit(1).pdf`, and the publication-figures/source-data ZIP.
- `FCCmue_Original_MadGraph_Diagrams_Verified_All4.zip`, `FCCmue_All4_Original_MadGraph_Diagrams_LaTeX_Source.zip`, original `CC_H`, `CC_HH`, `NC_H`, `NC_HH` `matrix.pdf` and process cards.
- `FCC_ue_MuC_1TeV_2TeV_80Pol_Review_20261025.zip` and the earlier CC HH→4b/complete 4b reports.
- `FCCue_MuC_4b_Process_Inventory_20261028.pdf`, `FCC_ue_NC_ThreeProcess_Validation_Package_20261027.zip`, `FCC_ue_NC_4b_continuum_50k_preliminary_20261028.pdf`, and associated-Higgs results.
- `MuC_ZH_to_4b_1TeV_2TeV_Wide80_130_for_Krzysztof_20261029.pdf` and related verified outputs.
- The user-provided physics-review/roadmap Markdown files (including `Pasted markdown(4).md` / `Pasted markdown (2).md` if attached).

**Primary public collider source:** K. Piotrzkowski, *FCC-μe: High Energy, High Luminosity Muon-Electron Collider & Neutrino Factory at CERN*, **arXiv:2610.40451v2** (revised 5 November 2026), https://arxiv.org/abs/2610.40451, INSPIRE https://inspirehep.net/literature/3220545. Read the real v2 paper, tables and captions; cite proposal page/table and differentiate v1 from v2.

**Public context:** official FCC-ee Feasibility Study Reports (2025, check errata), Higgs-factory 240/365-GeV physics, original single- and double-Higgs VBF theory/HEFT/SMEFT, the published electron–muon `hhWW` study of Cao, Cheng, Liu and Wang (*Measuring hhWW coupling at lepton colliders*, Phys. Rev. D 109 (2024) 073005; verify bibliographic metadata), relevant collider Higgs self-coupling studies and reliable H→bb branching-ratio references. Prefer primary journal/arXiv/CERN sources; verify titles, authors, DOI, dates and publication status. Cite each nontrivial externally derived result in the text with numbered references.

Priority: **original run cards, source CSV and logs > audited reports > existing presentation > earlier chat summaries > unsourced general statements**. Record source status explicitly in `SOURCE_MANIFEST.md`: `AVAILABLE AND VERIFIED`, `AVAILABLE BUT UNVERIFIED`, `PUBLIC SOURCE`, or `NOT AVAILABLE`. Do not present summaries as original machine results if primary inputs are absent. Clearly tag `[our MG5 calculation]`, `[derived from our data]`, `[collider proposal]`, `[literature]`, `[illustrative assumption]`, or `[proposed future calculation]` where confusion might arise.

## C. PHYSICS QUALITY STANDARDS — A REAL RESEARCH NOTE

The note must contain coherent *paragraph-level derivations and explanation*, not 20 pages of tables or slide bullets. Each major process subsection MUST answer:

1. What is the exact partonic process and final state, collider benchmark and polarization?
2. Which electroweak amplitudes/couplings generate it, and what are the leading diagrams and interference terms?
3. Why is this channel interesting for specific Higgs couplings or electroweak tests?
4. What cross sections do our completed calculations actually give, with numerical integration uncertainty and source?
5. Which cuts, phase-space regions, decays and branching ratios apply?
6. Which experimentally accessible observables and realistic backgrounds matter?
7. What can we **not yet conclude** about coupling measurement precision?
8. What targeted next calculations would turn this channel into a quantitative measurement projection?

Avoid formula-only paragraphs. Derive key formulas with defined conventions, check dimensions, and distinguish illustrative reasoning from exact SM predictions. Include original Feynman-diagram graphics when available. All numerical predictions not yet simulated (especially HHH, κ3/κ4 scans and projected bounds) MUST remain labeled as proposals or transparent examples. Never pretend source-generated `HH→4b` samples are the same as inclusive stable-Higgs cross sections.

### Essential definitions and theoretical derivations

Derive the electroweak Higgs sector from

\[
\mathcal L \supset (D_\mu\Phi)^\dagger(D^\mu\Phi)-V(\Phi),
\qquad V(\Phi)=-\mu^2\Phi^\dagger\Phi+\lambda(\Phi^\dagger\Phi)^2,
\qquad \Phi=(0,(v+h)/\sqrt2)^T,
\]

then derive the physical potential (ignoring an additive constant)

\[
V(h)=\tfrac12m_h^2h^2+\frac{m_h^2}{2v}h^3+\frac{m_h^2}{8v^2}h^4.
\]

State the self-coupling *definition convention* explicitly: if \(\mathcal L\supset-\lambda_3 h^3/3!-\lambda_4 h^4/4!\), then \(\lambda_3^{\rm SM}=3m_h^2/v\) and \(\lambda_4^{\rm SM}=3m_h^2/v^2\). Show the SM relationship between gauge boson masses and the \(hWW\), \(hhWW\), \(hZZ\), \(hhZZ\) interactions, taking care with identical-field factors and Feynman-rule conventions. Explain electroweak symmetry breaking, longitudinal weak-boson fusion, threshold versus high-energy behavior, and the role of gauge cancellations/unitarity. Do not make separately gauge-invariant claims about individual MG5 diagrams.

Define physically transparent coupling modifiers
\[
\kappa_W=g_{hWW}/g_{hWW}^{\rm SM},\quad
\kappa_Z=g_{hZZ}/g_{hZZ}^{\rm SM},\quad
\kappa_{2W}=g_{hhWW}/g_{hhWW}^{\rm SM},\quad
\kappa_{2Z}=g_{hhZZ}/g_{hhZZ}^{\rm SM},\quad
\kappa_3=\lambda_3/\lambda_3^{\rm SM},\quad
\kappa_4=\lambda_4/\lambda_4^{\rm SM}.
\]

Only use a common \(\kappa_{2V}\) if the chosen model assumes linked WW/ZZ modifications. Explain HEFT vs gauge-invariant SMEFT, SU(2)×U(1) relations, correlations, truncation/order, and EFT validity; do not treat all modifiers as unconstrained independent observables without a model. For \(VV\to hh\), explain the SM amplitude content (contact, exchanged vector boson and off-shell \(h^*\to hh\)) and that \(\sigma_{hh}(\kappa_3)\) is quadratic at fixed other couplings at tree level, while the high-\(m_{hh}\) spectrum can probe modifications of \(hhVV\). Derive/interrogate the leading longitudinal high-energy amplitude and its SM cancellation *within declared conventions*, avoiding unsupported isolated-diagram fits.

For the two-polarization beams derive the massless-lepton CC relation
\[
\sigma_{\rm CC}(P_{e^-},P_{\mu^+})/\sigma_{\rm CC}(0,0)
\simeq(1-P_{e^-})(1+P_{\mu^+}),
\]

and for unpolarized electrons \(R_{\rm CC}(P_{\mu^+})\simeq1+P_{\mu^+}\) when polarizations are fractional. Clearly explain right-*helicity antimuons* versus left-chiral charged current. For NC pure-Z-dominated production derive the leading approximate slope
\[
A_{\rm NC}\simeq\frac{g_L^2-g_R^2}{g_L^2+g_R^2},\qquad
 g_L=-\tfrac12+s_W^2,\quad g_R=s_W^2,
\]

with a warning that exact full-process slopes and a numerical weak-angle evaluation depend on the actual MG5 electroweak input scheme and possible subleading contributions; never present an LO fit error as attainable experimental weak-mixing-angle precision.

Include basic lepton collider kinematics:
\[
s\simeq 4E_eE_{\mu},\quad \sqrt s\simeq2\sqrt{E_eE_{\mu}},\quad y_{\rm CM}\simeq\tfrac12\ln(E_{\mu}/E_e)
\]

for ultrarelativistic head-on beams and a clearly stated axis convention. Discuss why asymmetric boost/forward acceptance changes physical reach. Compare design-like vs exact-energy points: FCC-μe `(E_μ,E_e)=(2 TeV,120 GeV)` ⇒ \(\sqrt s\approx0.9798\) TeV; `(5 TeV,183 GeV)` ⇒ \(1.9131\) TeV. Exact-energy scan `(2 TeV,125 GeV)` ⇒ 1 TeV and `(5 TeV,200 GeV)` ⇒ 2 TeV. Muon–muon benchmarks are distinct symmetric √s=1 and 2 TeV. For v2 machine luminosities, **verify the revised proposal table** (the prior slide-package QA records 0.98-TeV peak luminosity \(0.63\times10^{34}\,\mathrm{cm}^{-2}\mathrm{s}^{-1}\), not a preliminary older value). State instantaneous vs integrated luminosity units clearly.

## D. REQUIRED COMPLETED PROCESSES AND REFERENCE RESULTS

### D1 — Richard's complete four-channel, 48-run inclusive study

Exact MadGraph commands (each an unrestricted full tree-level SM process, not a separately isolated gauge-invariant fusion graph):

```text
import model sm
generate e- mu+ > ve vm~ h QCD=0
```

```text
import model sm
generate e- mu+ > ve vm~ h h QCD=0
```

```text
import model sm
generate e- mu+ > e- mu+ h QCD=0
```

```text
import model sm
generate e- mu+ > e- mu+ h h QCD=0
```

Use the correctly conjugated \(e^-\mu^+\to\nu_e\bar\nu_\mu h(h)\) CC final states, \(e^-\mu^+\to e^-\mu^+h(h)\) NC states, beam 1 unpolarized electron, beam 2 positive muon, six \(P_{\mu^+}\) = 0,20,40,60,80,100%, two exact energies 1,2 TeV, 30,000 events/configuration, no generator-level kinematic cuts, stable Higgs bosons, complete LO SM matrix elements. This is **48 individual CERN jobs**, not 48 different processes. Original source uncertainty is integration Monte Carlo only.

Use full 48-row original CSV in all source plots and provide a readable selected-results table in text; a complete machine-readable CSV belongs in ZIP. The values below are cross-checks (fb), NOT a substitute for inspecting the CSV:

| Channel | √s | P=0% | P=+80% | P=+100% |
|---|---|---:|---:|---:|
| CC h | 1 TeV | 210.540 | 378.570 | 421.150 |
| CC hh | 1 TeV | 0.0743838 | 0.1332298 | 0.1482390 |
| NC h | 1 TeV | 20.835 | 24.476 | 25.402 |
| NC hh | 1 TeV | 0.00962012 | 0.01130777 | 0.01172286 |
| CC h | 2 TeV | 386.010 | 695.000 | 772.690 |
| CC hh | 2 TeV | 0.418510 | 0.754495 | 0.839521 |
| NC h | 2 TeV | 38.991 | 45.829 | 47.642 |
| NC hh | 2 TeV | 0.0547116 | 0.0642989 | 0.0667703 |

Verify all eight numerical fits \(\sigma(p)=a(1+Ap)\) against the audit or recompute from the 48 data points, correctly propagating the shared unpolarized denominator when fitting ratios:

| Channel | A at 1 TeV | A at 2 TeV |
|---|---:|---:|
| CC h | 0.9982 ± 0.0020 | 1.0007 ± 0.0018 |
| CC hh | 0.9934 ± 0.0040 | 1.0053 ± 0.0039 |
| NC h | 0.2181 ± 0.0012 | 0.2208 ± 0.0011 |
| NC hh | 0.2186 ± 0.0022 | 0.2204 ± 0.0022 |

Scientific conclusions to explain, not merely assert: CC ≈10× NC for single Higgs and ≈7.7× for double Higgs at zero polarization; at +80% CC increases ≈1.8× and NC ≈1.175×; at fixed P=0%, H energy growth 1→2 TeV is ≈1.83–1.87× and hh ≈5.63–5.69×. Discuss weak-boson luminosity, multi-Higgs phase space, interference and energy dependence without claiming already measured coupling sensitivity.

### D2 — Exact original MG5 diagram verification (Krzysztof's question)

Include authentic CERN-generated original vector figures for all four inclusive processes if available: `CC_H/matrix.pdf` (one), `NC_H/matrix.pdf` (one), `CC_HH/matrix.pdf` (four), `NC_HH/matrix.pdf` (four). Confirm original diagram labels against the source rather than guessing. For each HH export, earlier audit identifies diagram 1 = \(hhWW/hhZZ\) contact; diagrams 2 and 3 = separate \(hVV\) emissions; diagram 4 = \(VV\to h^*\to hh\) containing \(\lambda_3\). Explain why the full LO amplitude includes coherent interference and why individual topology rates are neither separately calculated nor necessarily gauge invariant. Treat the internal \(h^*\) as off shell. Distinguish diagrams from **actual MG5 export** and theory-motivating schematic VBF subamplitudes.

### D3 — Charged-current HH→4b and complete neutrino-associated 4b comparisons

State exact resonant processes and complete \(\nu\bar\nu b\bar b b\bar b\) final states for both FCC-μe and symmetric muon collider. Do not silently extend neutrino flavor sums or invent MadGraph syntax; obtain from original cards. Fiducial parton-level requirements: 4 bottom/antibottom partons \(|\eta_b|<5\), two *distinct opposite-charge* \(b\bar b\) pairs both with \(110<m_{b\bar b}<130\) GeV; no minimum b-parton \(p_T\). Preserve the pairing algorithm from source. Historical results (fb):

| Collider and √s | Resonant hh→4b, P0 / P80 | Complete νν̄4b, P0 / P80 |
|---|---|---|
| FCC-μe, 0.9798 TeV | 0.04912 / 0.08816 | 0.05355 / 0.09195 |
| μ⁺μ⁻, 1.000 TeV | 0.07047 / 0.11582 | 0.07530 / 0.12472 |
| FCC-μe, 1.9131 TeV | 0.26478 / 0.47611 | 0.28157 / 0.50745 |
| μ⁺μ⁻, 2.000 TeV | 0.30624 / 0.54606 | 0.32480 / 0.57873 |

**Critical warning:** Earlier resonant hh→4b used model-card \(\mathrm{BR}(h\to b\bar b)=0.844640\), not conventional modern precision-SM \(\sim0.58\). The integrated luminosity and decay-normalization assumptions need reconciliation before realistic projections. Do not scale complete interfering 4b amplitudes as though all contributions are simply \(\mathrm{BR}^2\); do not subtract the resonant sample from the complete one and describe the remainder as a physical independent background. Include this in the main text, not only a footnote.

### D4 — Neutral-current 4b, bbH and continuum

Consider \(e^-\mu^+\to e^-\mu^+hh\to e^-\mu^+4b\), associated \(e^-\mu^+\to e^-\mu^+b\bar b h\to e^-\mu^+4b\), complete \(e^-\mu^+\to e^-\mu^+4b\), and a Higgs-excluded diagnostic sample. Earlier fiducial generation uses \(p_{T,\ell}>1\) GeV on outgoing charged leptons plus the 110–130-GeV bb-pair windows and b acceptance (check original cards). Preliminary FCC-μe, √s≈0.9798 TeV, P=0 results (fb): NC hh 0.006382; associated bbH 0.012925; full NC 4b 0.007713; Higgs-excluded continuum 0.0008253 (only 88/50,000 accepted events).

**Known open issue:** The complete-NC-4b rate (0.007713 fb) is smaller than separately generated associated-bbH (0.012925 fb). This is **not automatically explained by interference**; the old scientific audit flags an unresolved process-definition/normalization/phase-space consistency issue. Demand a targeted regeneration and cut-level audit. Do not add the overlapping NC samples or quote validated background estimates. Higher-energy associated bbH examples: FCC-μe 1.913 TeV +80% ≈0.081843 fb; μ⁺μ⁻ 2 TeV +80% ≈0.094913 fb; use only if exact provenance, cuts, and uncertainty can be checked.

### D5 — Muon collider ZH→4b

Use explicit resonant \(\mu^+\mu^-\to Zh\to(b\bar b)(b\bar b)\), √s=1,2 TeV, unpolarized. Before/after fiducial cross sections (fb): 1 TeV = **1.56450 → 1.52716**; 2 TeV = **0.37888 → 0.36929**. Cuts: four b-partons \(|\eta_b|<5\), both assigned \(m_{b\bar b}\in[80,130]\) GeV, no minimum b-parton \(p_T\). This **wider window differs** from the hh→4b 110–130-GeV window. Explain why the flavour-diagonal s-channel \(\mu^+\mu^-\to Z^*\to Zh\) topology has no analogous ordinary tree-level \(\mu^+e^-\) annihilation process, and why its final state differs from neutrino-associated hh.

## E. REQUIRED 20-PAGE NARRATIVE: PAGE-BUDGET BLUEPRINT

Write continuous scholarly prose, numbered sections and equations. The mapping below gives a **content/page budget**, not permission to start each section on a fresh page or pad pages. Adjust pagination to obtain exactly 20 A4 pages **without dropping any subject**.

**Page 1 — Front matter and executive scientific abstract.** Title/author/meeting participants carefully labeled, 200–300-word abstract, keywords, concise synopsis of established results and unsolved physics aims. No empty cover page.

**Pages 2–3 — Collider proposal, scientific motivation and FCC-ee complementarity.** Read revised arXiv v2, discuss source/acceleration/ring concept, neutrino-factory connection, actual machine working points and luminosities, energy/boost formulas, FCC-ee 240/365-GeV precision Higgsstrahlung vs polarized high-energy VBF H/HH, machine status versus aspiration, detector/forward challenges.

**Pages 4–5 — Standard Model Higgs sector and weak-fusion theory.** Derive potential and couplings, symmetry breaking, gauge vertices, trilinear and quartic normalizations, spacelike electroweak boson exchange, VBF helicity/longitudinal behavior, interference and unitarity, full vs topology-limited matrix elements.

**Page 6 — CC single Higgs physics.** Exact process, CC helicity, \(hWW\) measurement interpretation, rates, polarization derivative, decay/acceptance and future differential observables.

**Page 7 — NC single Higgs physics.** Exact process, \(hZZ\) and \(Z\ell\ell\) chirality, forward leptons, approximate NC asymmetry, EW input scheme and practical reconstruction.

**Pages 8–9 — CC and NC double Higgs and original diagrams.** Four MG5 graphs per process, \(h^*\to hh\), contact \(hhVV\), separate emissions, interference, \(\kappa_3,\kappa_{2W},\kappa_{2Z}\); why different \(m_{hh}\) regimes probe different couplings and what a rigorous measurement would require.

**Pages 10–11 — The 48-run inclusive scan and interpretation.** Full scientific method, beam energies and six polarizations, an appropriately formatted all-channel data table (selected points in the main text, all 48 values available in CSV), source-derived absolute and ratio plots, fit slopes and numerical errors, 1→2 TeV energy scaling, explicit numeric calculations and fitting caveats.

**Pages 12–13 — Four-bottom case and collider comparisons.** Resonant/complete CC \(\nu\bar\nu4b\) calculations, old fiducial cuts and BR normalization, muon-collider comparison, NC hh/bbH/continuum, sample overlap and unresolved mismatch, muon-collider Zh channel and its different cuts.

**Page 14 — Event yields and experimental observables.** \(N=\mathcal L\sigma\sum\mathrm{BR}\epsilon\), decay channels, 4b pairing/tagging combinatorics, boosted geometry, missing-pT/lepton tagging, expected physical backgrounds, luminosity/polarization/calibration requirements. Numerical demonstrations may use explicitly hypothetical \(\mathcal L=3\,\mathrm{ab}^{-1}\) and clearly identified tagging assumptions, never present them as an established machine scenario.

**Pages 15–17 — Higgs coupling measurements and EFT.** Define \(\kappa_W,\kappa_Z,\kappa_{2W},\kappa_{2Z},\kappa_3\), discuss HEFT vs SMEFT, gauge-consistent scan grids, template morphing/interference, normalized and absolute observables, threshold vs high-\(m_{hh}\) discrimination, polarization and CC+NC combinations; construct a transparent likelihood \(\mu_i(\boldsymbol\kappa,\boldsymbol\theta)=\mathcal L\sum_c\sigma_{c,i}(\boldsymbol\kappa)\mathrm{BR}_c(\boldsymbol\kappa)\epsilon_{c,i}(\boldsymbol\theta)+b_i(\boldsymbol\theta)\), specify Poisson likelihood with nuisance parameters and realistic systematics. Explain expected precision conceptually but **quote no fabricated projected limits**.

**Page 18 — Triple-Higgs and quartic Higgs potential.** Proposed CC/NC \(hhh\) processes and exact MG5 commands, tree-level \(\lambda_3,\lambda_3^2,\lambda_4\) amplitude content, threshold, phase-space and vector-boson luminosity suppression, illustrative yield feasibility criterion, 6b,4b2τ,4b2γ, initial P0/P80/P100 and 1/2 TeV runs. State unequivocally: **No HHH cross section has yet been computed in this project**.

**Page 19 — Proposed collaborative work plan, validation and distinctive publication question.** Ordered Phase I baseline independent-seed/NC forward/BR reconciliation; Phase II \(\kappa_3\)-\(\kappa_{2V}\) model & differential analyses; Phase III detector level and backgrounds; Phase IV HHH feasibility/\(\kappa_4\); Phase V realistic machine + FCC-ee inputs. Define deliverables, acceptance tests, scenario assumptions and decision points for the four collaborators **without inventing assigned roles**. Benchmark against published electron–muon hhWW literature and explain genuine novelty.

**Page 20 — Conclusions and references.** Scientific findings and clearly ranked unanswered questions, prioritized next calculations, compact fully verifiable bibliography. Balance reference coverage and substantive conclusions within page 20; citations throughout are mandatory.

The page budget must remain readable. If a substantial bibliography cannot fit on the last page without overcrowding, rebalance preceding sections; do not quietly generate 21 pages or omit references.

## F. MUST-HAVE FORMULAS, FIGURES AND TABLES

**Equations:** collider CM energy and boost; EWSB and potential; gauge/Higgs vertices and trilinear/quartic Feynman-rule conventions; polarized helicity cross sections; NC chiral asymmetry; coherent hh amplitudes/interference; relative sigma energy growth; event-yield formula; \(\kappa\)-parameter definitions; HH coupling-polynomial or amplitude dependence; differential cross sections in \(m_{hh}\) and angular variables; b-tagging/branching fractions; Poisson likelihood with nuisance parameters; optional basic Fisher-information/sensitivity argument if explained and appropriately bounded.

**Graphics (source-derived; approximately 5–8 carefully chosen):** original proposal's layout or properly attributed schematic; beam-energy/boost figure; actual CC and NC HH MG5 vector-diagram montage; four-channel absolute polarization cross sections; normalized polarization enhancement plot; rate-growth comparison; transparent process/coupling dependency diagram; optional staged roadmap. Use captions that identify source, conditions, cuts, scheme and numerical status. Do not use unrelated web diagrams instead of the user's genuine MG5 exports.

**Tables:** benchmark energy/beam/polarization table; four-channel process and relevant couplings map; selected/all 48 inclusive results (maintain the full CSV); eight fitted slopes; old CC νν4b fiducial comparisons; NC 4b status table; Zh before/after table; couplings-versus-observables; prospective work packages and validation checklist. Avoid breaking tables badly across pages; use `longtable` or landscape only if necessary and preserve A4 readability.

**References:** in-text numbered citation at each relevant claim, full bibliography with arXiv/journal/source IDs verified. Internal collaboration numerical reports should be labeled unpublished/preliminary internal calculation packages, not peer-reviewed studies. Check licensing/attribution of any external figure. Do not fabricate DOI, accepted journal status, parameter values or luminosity.

## G. STRICT PHYSICS QA — THESE ARE NOT OPTIONAL

Perform and record explicit PASS / FAIL / NOT VERIFIED for each:

1. Collider proposal **v2** actually read; its Table 1 values and publication/revision dated accurately; instantaneous vs integrated luminosity distinguished.
2. Exact 1 and 2 TeV scan not confused with older 0.9798 and 1.9131 TeV FCC-μe benchmarks.
3. All four process commands scientifically and syntactically accurate; \(\nu_e\bar\nu_\mu\) charges correct; stable H vs decayed 4b separated.
4. All 48 data points and uncertainties reproduced from original source, not screenshot/OCR; all eight fitted slopes and statistical interpretation checked; correlations handled if ratios refitted.
5. MG5 original diagrams verified for complete HH amplitudes: contact, separate emissions, off-shell self-coupling and coherent interference; no separately gauge-invariant-diagram assertion.
6. Historical BR(H→bb)=0.844640 issue prominently stated; no unjustified global scaling of full four-bottom amplitudes.
7. Cuts: four b \(|\eta_b|<5\), 110–130 GeV windows for older HH, 1 GeV outgoing-lepton generation cut for NC four-bottom, **80–130 GeV** for muon-collider Zh, no bottom pT minimum as stated.
8. Unresolved NC full-4b versus associated-bbH rate inconsistency explicitly identified; no unsupported 'interference solved it' explanation.
9. NC forward lepton and regulator/acceptance physics properly distinguished; absence of cuts not automatically called a mathematical divergence.
10. Monte Carlo integration uncertainty not confused with QCD/EW uncertainty, detector uncertainty or experimental coupling precision.
11. No HHH rates or \(\kappa_3/\kappa_4\) limits invented; source data and proposed calculations segregated.
12. Current literature and FCC-ee complementarity correctly sourced, including prior eμ hhWW work (avoid claiming first-ever study).
13. All math symbols, units, charge conjugations, branching fractions, citations and captions checked.
14. Exactly 20 genuine A4 PDF pages; article layout, no invisible overflow, no missing figures, no very small text.
15. TeX compiled in current session; references resolved; source ZIP independently rebuildable if toolchain permits.

`SCIENTIFIC_QA_REPORT.md` must document what was actually checked and any outstanding conditions, with verifiable evidence such as exact command used, page count, input CSV row counts and citation inventory.

## H. PRODUCTION EXECUTION PHASES

**Phase 0: Source audit.** Inspect attached roadmap files, the FCC-μe kick-off deck ZIP, original CERN numerical archives/diagrams and external primary proposal. Create `SOURCE_MANIFEST.md`; list missing inputs honestly.

**Phase 1: Scientific reconciliation.** Confirm exact beam configurations, matrix-element definitions, counts, original CSV numbers, proposal v2 machine table, old generation cuts, Higgs BR, diagram IDs and literature. Compute source-derived ratios in code and log calculations.

**Phase 2: Scholarly manuscript.** Write genuine research-level paragraphs with numbered sections, equations, interpretation, limitations, references and self-contained methodology for every channel. Target ~7,000–9,000 **substantive** words if compatible with 20 A4 pages plus figures/tables; prioritize content and legibility over arbitrary word count. Add short abstract and concluding research agenda.

**Phase 3: Figures and tables.** Reuse original MG5 vector assets, regenerate numerical plots from the 48-row CSV and document all derived data with Python source. Produce vector PDF charts, clear tables, captions and source notes.

**Phase 4: Professional LaTeX.** Create an A4 article source with all relative paths, bibliography and reproducible scripts. Ensure text/math clarity, citations, figure cross-references and clean typography.

**Phase 5: Compile and visual review.** Use `latexmk -pdf` (or `pdflatex`/BibTeX/Biber passes as applicable). Check `.log`, `pdfinfo`/PDF page count, fonts, table/figure placement, equations, citations and page margins; render a contact sheet and inspect representative pages. Remove overfull/underfull problems that affect legibility. Revise until **exactly 20** pages with no scientific omissions or blank padding.

**Phase 6: Scientific QA and portability.** Execute acceptance checklist, compare numbers with records, ensure result statuses, reproduce PDF from a clean extracted ZIP if feasible, include `README_BUILD.md` instructions, and verify file existence/hash/ZIP integrity.

**Phase 7: Delivery.** Provide verified separate download links for `.tex`, `.pdf`, and complete ZIP, confirm actual page count and what's included, and briefly state scientifically material unresolved limitations. No promises of later completion.

## FINAL INSTRUCTION — EXECUTE; DO NOT WRITE A NEW PROMPT

**EXECUTE_PRODUCTION_NOW = YES**

**AUTHOR_COMPLETE_20_PAGE_RESEARCH_NOTE = YES**

**DERIVE_AND_EXPLAIN_HIGGS_PHYSICS_AND_ALL_PROCESSES = YES**

**VERIFY_CERN_CROSS_SECTIONS_FITS_FIDUCIAL_CUTS_AND_ORIGINAL_DIAGRAMS = YES**

**COVER_HIGGS_COUPLING_MEASUREMENTS_EFT_TRIHIGGS_AND_RESEARCH_ROADMAP = YES**

**NO_UNSOURCED_SENSITIVITIES_OR_HHH_NUMBERS = YES**

**COMPILE_AND_VISUALLY_VALIDATE_PDF = YES**

**EXACT_PAGE_COUNT = 20_A4_PAGES_INCLUDING_BIBLIOGRAPHY**

**FINAL_DELIVERY = EDITABLE_TEX + COMPILED_PDF + COMPLETE_SOURCE_ZIP**

**DO_NOT_RETURN_OUTLINE_OR_NEW_MASTER_PROMPT_IN_PLACE_OF_DOCUMENT = YES**
