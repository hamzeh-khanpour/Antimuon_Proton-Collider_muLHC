# FCCmue_Higgs_Physics_Kickoff_FINAL_PRODUCTION_MEGA_PROMPT

## EXECUTION CONTRACT — THIS IS THE PRESENTATION-PRODUCTION TASK

**Operation:** `PRODUCE_FCCMUE_HIGGS_PHYSICS_KICKOFF_COMPLETE`

You are the scientific editor, collider-phenomenology analyst, LaTeX/Beamer author, numerical-data auditor, figure-production specialist, and final deliverables integrator for an advanced research collaboration kick-off presentation.

**Your assignment is to CREATE the actual finished presentation in this execution, not to write another prompt, give an outline, or propose a future workflow.** Read the entire specification and all available attached files. Act without redundant confirmation questions; resolve nonessential ambiguities by conservative scientific defaults, document them, and deliver the most complete verified result possible in this same response. Do not claim to have verified, compiled, or generated something you have not actually verified, compiled, or generated.

**Presentation:** *Higgs Physics Potential of the FCC-\(\mu^+e^-\) Collider at CERN: From Standard Model Benchmarks to Higgs Self-Couplings*.

**Meeting:** First scientific collaboration kick-off, November 2026; do not invent the specific date, location, or agreed collaboration name.

**Presenter:** Hamzeh Khanpour — AGH University of Krakow.

**Participants for discussion:** Hamzeh Khanpour, Krzysztof Piotrzkowski, Richard Ruiz, Piotr Kotko. Distinguish presenter, participants, and proposed coauthors; do not imply formal authorship was agreed.

**Exact scope:** **40 substantive main frames (including title and outline) plus 8 substantive backup frames = 48 rendered presentation pages**, unless the actual AGH theme uses unavoidable overlays; disable unnecessary overlays and verify 48 PDF pages. No extra title, thank-you, or reference-only frame outside this count. Include bibliography in B8 and concise source notes on substantive slides. Identify backup frames as B1–B8 in visible headers or footers where feasible.

**Required downloadable deliverables, with exact filenames:**

1. `FCCmue_Higgs_Physics_Kickoff_2026.tex` — complete editable LaTeX source, separately downloadable.
2. `FCCmue_Higgs_Physics_Kickoff_2026.pdf` — real compiled and visually checked PDF, separately downloadable.
3. `FCCmue_Higgs_Physics_Kickoff_2026_COMPLETE.zip` — complete, portable, rebuildable project containing both main files, original local AGH `.sty` files, all necessary permitted graphics, original MG5 vector diagrams, all numerical data tables, plotting scripts, references, build instructions, and scientific QA records.

**Mandatory ZIP support files:** `README_BUILD.md`, `SOURCE_MANIFEST.md`, `SCIENTIFIC_QA_REPORT.md`, `data/cross_sections_48.csv`, `data/historical_cross_sections.csv` when the old numbers are independently supported, `figures/`, `scripts/`, and `references/` as appropriate. Include `SLIDE_CONTENT_MAP.md` mapping slide number → scientific claim → source. Include `NUMERICAL_PROVENANCE.csv` if useful, and slide-by-slide speaker notes where practical.

**Absolute prohibitions:** No invented data, cross sections, figures, fit errors, HHH rates, sensitivities, literature dates, machine parameters, collaboration roles, or references. No fake screenshots, blank slides, decorative stock diagrams masquerading as MadGraph diagrams, unrelated collider plots, generic substitute theme, dead asset paths, TeX with failed compilation presented as finished, or empty ZIP shells. Never convert a proposed study into a completed result.

---

## PHASE 0 — INPUT INVENTORY, ORIGINAL STYLE AND SOURCE HIERARCHY

### A. Inspect the actual Beamer template and preserve AGH identity

Locate and inspect these user-supplied files, including their package dependencies and visible rendered design:

- `Hamzeh_Khanpour_Ultra-cold-muons-for-the-LHC.tex`
- `Hamzeh_Khanpour_Ultra-cold-muons-for-the-LHC.pdf`
- `beamerthemeAGH.sty`
- `beamercolorthemeAGH.sty`

The supplied Beamer source uses, or should be reconciled against, the following original conventions:

```latex
\documentclass[aspectratio=1610,english]{beamer}
\usetheme[parttitle=rightfooter]{AGH}
\graphicspath{{figures/}{./}}
```

Preserve the real **AGH University of Krakow** 16:10 aesthetic: section/title bar, green/red/black/white scheme, title-page structure, footer, institutional name, slide numbering, framed blocks, alert blocks, relevant typography, and section navigation. Preserve supplied macros and legitimate local assets. Reuse the actual `.sty` files in the ZIP. Do not substitute Metropolis, Madrid, or a generic theme. Replace only LH\(\mu\)C/\(\gamma\gamma\) subject-specific text and logos not relevant to this meeting. If a reference theme asset such as `HELP4CERN.jpg` or AGH logo is missing, search available project/conversation files and legitimate institutional sources; disclose any unresolved absence. Never pretend a missing logo was supplied, and do not deliver a deck with broken assets.

### B. Investigate every primary physics input, not just chat summaries

Priority order:

1. **Collider proposal**: `https://inspirehep.net/literature/3220545`, linked `https://arxiv.org/pdf/2610.40451` (*FCC-\(\mu e\): High Energy, High Luminosity Muon–Electron Collider & Neutrino Factory at CERN*). Inspect the actual PDF text, machine parameter tables, original proposal schematic, stated beam energies, luminosity assumptions, staged operation and limits. Cite precise pages/captions. Verify all external claims against this source before using them.
2. **48-run inclusive scan**: `FCCmue_Higgs_Polarization_Results_Audit(1).pdf`, `FCCmue_Higgs_PolScan_full_exact_REVIEW.zip`, `FCCmue_Higgs_Polarization_Figures_v2_Source_Data.zip`, `cross_sections_48.csv`, fit tables, process/run cards and two vector PDF polarization figures.
3. **Original Feynman diagrams**: `FCCmue_All4_Original_MadGraph_Diagrams_LaTeX_Source.zip`, `FCCmue_All4_Original_MadGraph_Diagrams_Annotated.pdf`, `FCCmue_Original_MadGraph_Diagrams_Verified_All4.zip`, individual original `matrix.pdf` and process cards.
4. **Older CC \(HH\to4b\)**: `FCC_ue_MuC_1TeV_2TeV_80Pol_Review_20261025.zip`, original MG5 output cards/logs and one-page cross-section summaries.
5. **Older NC/associated/continuum**: `FCCue_MuC_4b_Process_Inventory_20261028.pdf`, `FCC_ue_NC_ThreeProcess_Validation_Package_20261027.zip`, `FCC_ue_NC_4b_continuum_50k_preliminary_20261028.pdf`, bbH records and process logs.
6. **Muon collider ZH**: `MuC_ZH_to_4b_1TeV_2TeV_Wide80_130_for_Krzysztof_20261029.pdf` or matching report/cards.
7. **FCC-ee and literature context**: up-to-date official FCC-ee Higgs-factory/design documentation (particularly 240/365 GeV programme), related electron–muon Higgs papers, and vetted primary phenomenology literature. Verify paper title/authors/publication status/DOIs; include recent dated source context.
8. **Reference AGH deck/theme**, which controls design but must not contaminate this talk with unrelated \(\mu p\) physics figures.

Inspect all mounted attachments and current Project/Library files available in the environment; if a named source is not accessible, log this in `SOURCE_MANIFEST.md` as `MISSING` or `NOT VERIFIED`. Never claim to have inspected a missing source. If previous messages and source data disagree, **source files and original run cards take precedence**. Distinguish `[MG5 generated]`, `[derived from MG5]`, `[proposal estimate]`, `[external literature]`, `[illustrative assumption]`, and `[future/proposed]` in figures, source notes, and scientific QA.

### C. Source provenance rules

For every important number or plot, track: original filename or source URL, page/table or CSV row(s), collider, process, \(\sqrt s\), beam energies, polarization, cuts, branching ratio/decay setup, calculation level, uncertainty kind, and whether independent convergence checks exist. Use short slide-footnote citations and provide full citations in backup B8 and manifest. Source figures are appropriately attributed; reuse or redraw only if permitted, maintaining clear provenance. Do not use arbitrary image-search results for original process diagrams.

---

## PHASE 1 — SCIENTIFIC CONVENTIONS AND VERIFIED INPUT DATA

### 1. Collider kinematics: never mix benchmark families

For ultrarelativistic head-on electron–muon beams,
\[
 s\simeq4E_{e^-}E_{\mu^+}, \qquad \sqrt{s}\simeq2\sqrt{E_{e^-}E_{\mu^+}}.
\]

**Earlier FCC-\(\mu e\) design-like configurations** (use these labels only when compatible with actual source):

- \(E_{\mu^+}=2\,\mathrm{TeV}\), \(E_{e^-}=120\,\mathrm{GeV}\): \(\sqrt{s}=0.979796\,\mathrm{TeV}\).
- \(E_{\mu^+}=5\,\mathrm{TeV}\), \(E_{e^-}=183\,\mathrm{GeV}\): \(\sqrt{s}=1.913113\,\mathrm{TeV}\).

**Exact-energy scan** (different electron energies):

- \((E_{\mu^+},E_{e^-})=(2\,\mathrm{TeV},125\,\mathrm{GeV})\): \(\sqrt{s}=1.000\,\mathrm{TeV}\).
- \((E_{\mu^+},E_{e^-})=(5\,\mathrm{TeV},200\,\mathrm{GeV})\): \(\sqrt{s}=2.000\,\mathrm{TeV}\).

**Muon collider** comparisons: symmetric \(\mu^+\mu^-\) configurations at \(\sqrt{s}=1\) and \(2\,\mathrm{TeV}\). Only show other crossed FCC-\(\mu e\) combinations if the primary proposal explicitly presents them; compute corresponding energies accurately. Do not describe design benchmarks as exact 1 and 2 TeV, or vice versa. Verify any instantaneous luminosity against the original proposal. Never conflate \(\mathrm{cm}^{-2}\mathrm{s}^{-1}\) with integrated \(\mathrm{ab}^{-1}\). Do not assign a meeting date or integrated-luminosity scenario without source or explicit illustrative labeling.

### 2. Four inclusive processes: actual 48-run CERN campaign

Exact MadGraph syntax:

```text
import model sm
generate e- mu+ > ve vm~ h QCD=0            # CC H
```

```text
import model sm
generate e- mu+ > ve vm~ h h QCD=0          # CC HH
```

```text
import model sm
generate e- mu+ > e- mu+ h QCD=0           # NC H
```

```text
import model sm
generate e- mu+ > e- mu+ h h QCD=0         # NC HH
```

The inline comments identify separate process-card examples; preserve valid MG5 syntax in the actual quoted commands. Interpret `ve` as \(\nu_e\), `vm~` as \(\bar\nu_\mu\). Electron = MG5 beam 1, unpolarized; positive muon = beam 2. \(P_{\mu^+}=0,20,40,60,80,100\%\), with +100% denoting right-helicity antimuons. Four channels × two exact-energy benchmarks × six polarizations = **48** jobs, **30,000 events each**, full LO SM tree-level matrix elements, **stable Higgs**, and **no imposed generation-level phase-space cuts**. The results are inclusive production cross sections, **not** \(H\to b\bar b\), \(HH\to4b\), or detector-level predictions. All 48 jobs completed and the archives were collected, but statuses `COMPLETED_UNVALIDATED` and MC integration errors do not constitute independent physics convergence certification.

**Complete machine-readable reference values.** Reproduce from actual `cross_sections_48.csv` when available; the below is a cross-check only. All values are \(\sigma\pm\delta\sigma_{\rm MC}\), in **fb**; \(P\) in percent.

| \(\sqrt{s}\) | \(P_{\mu^+}\) | CC H | CC HH | NC H | NC HH |
|---|---:|---:|---:|---:|---:|
| 1 TeV | 0 | 210.540 ± 0.209 | 0.0743838 ± 0.0001274 | 20.835 ± 0.025 | 0.00962012 ± 0.0000146 |
| 1 TeV | 20 | 252.710 ± 0.158 | 0.0889793 ± 0.0001492 | 21.770 ± 0.015 | 0.01004468 ± 0.0000167 |
| 1 TeV | 40 | 294.730 ± 0.271 | 0.1040162 ± 0.0001885 | 22.660 ± 0.014 | 0.01048684 ± 0.0000160 |
| 1 TeV | 60 | 336.830 ± 0.199 | 0.1188249 ± 0.0002053 | 23.611 ± 0.019 | 0.01089547 ± 0.0000148 |
| 1 TeV | 80 | 378.570 ± 0.243 | 0.1332298 ± 0.0002299 | 24.476 ± 0.015 | 0.01130777 ± 0.0000174 |
| 1 TeV | 100 | 421.150 ± 0.433 | 0.1482390 ± 0.0002357 | 25.402 ± 0.018 | 0.01172286 ± 0.0000180 |
| 2 TeV | 0 | 386.010 ± 0.303 | 0.418510 ± 0.0006568 | 38.991 ± 0.030 | 0.0547116 ± 0.0000851 |
| 2 TeV | 20 | 463.490 ± 0.399 | 0.502952 ± 0.0008456 | 40.760 ± 0.027 | 0.0570892 ± 0.0000871 |
| 2 TeV | 40 | 540.620 ± 0.371 | 0.587089 ± 0.0010043 | 42.460 ± 0.045 | 0.0596361 ± 0.0000859 |
| 2 TeV | 60 | 617.270 ± 0.428 | 0.671917 ± 0.0011516 | 44.171 ± 0.042 | 0.0620664 ± 0.0000868 |
| 2 TeV | 80 | 695.000 ± 0.614 | 0.754495 ± 0.0012769 | 45.829 ± 0.055 | 0.0642989 ± 0.0000957 |
| 2 TeV | 100 | 772.690 ± 0.517 | 0.839521 ± 0.0013969 | 47.642 ± 0.033 | 0.0667703 ± 0.0001033 |

The original dataset contains **48 rows**: each of the 12 lines above has four independent process entries. In the compiled presentation, use the true source precision and include original event numbers and random seeds in B3/B4 if verified from source files.

**Eight weighted linear polarization fits.** Write \(p=P_{\mu^+}/100\) and \(\sigma(p)=a(1+A p)\); errors are fitted numerical errors, not projected experimental precision.

| Channel | \(A\), 1 TeV | \(\chi^2/4\), 1 TeV | \(A\), 2 TeV | \(\chi^2/4\), 2 TeV |
|---|---:|---:|---:|---:|
| CC H | 0.9982 ± 0.0020 | 1.77/4 | 1.0007 ± 0.0018 | 2.38/4 |
| CC HH | 0.9934 ± 0.0040 | 2.84/4 | 1.0053 ± 0.0039 | 0.94/4 |
| NC H | 0.2181 ± 0.0012 | 5.08/4 | 0.2208 ± 0.0011 | 3.40/4 |
| NC HH | 0.2186 ± 0.0022 | 1.93/4 | 0.2204 ± 0.0022 | 3.36/4 |

Source p-values, if validated: 1 TeV [CC H 0.779; CC HH 0.585; NC H 0.279; NC HH 0.749]; 2 TeV [CC H 0.667; CC HH 0.919; NC H 0.493; NC HH 0.500].

**Physics interpretation.** In the ultrarelativistic limit, CC \(R(P)=\sigma(P)/\sigma(0)\simeq1+p\); at \(+80\%\), \(R\approx1.8\). NC \(R(P)\simeq1+A_{\rm NC}p\), \(A_{\rm NC}\approx0.22\), giving \(R(80\%)\approx1.175\). The leading pure-Z fusion approximation gives \(A_{\rm NC}\approx(g_L^2-g_R^2)/(g_L^2+g_R^2)\), with \(g_L=-\tfrac12+\sin^2\theta_W\) and \(g_R=\sin^2\theta_W\); do not substitute a numerical weak mixing angle without checking the MG5 electroweak scheme/parameter card. The CC H and HH enhancement is far stronger than NC. \(\sigma_{HH}(2\,\mathrm{TeV})/\sigma_{HH}(1\,\mathrm{TeV})\sim5.6\), whereas single-H grows \(\sim1.8\)–1.9; derive and label calculations explicitly.

### 3. Original generated MG5 Feynman diagrams — Krzysztof's explicit question

The diagrams must come from original CERN MadGraph diagram exports, not a generic web image.

- **CC H and NC H:** each exported tree-level process shows one \(HWW\) or \(HZZ\) fusion diagram.
- **CC HH and NC HH:** each exported matrix contains **four diagrams**, numbered in the original MG5 output:
  - **Diagram 1:** \(HHWW\) or \(HHZZ\) contact vertex.
  - **Diagrams 2 and 3:** separate Higgs emissions through two \(HWW\) or \(HZZ\) couplings.
  - **Diagram 4:** \(VV\to H^*\to HH\) with **off-shell** \(H^*\), involving the trilinear self-coupling \(\lambda_3\).

Explain on Slide 18 why unrestricted `generate ... QCD=0` includes all diagrams and interference, schematically
\[
 |\mathcal M|^2=\big|\mathcal M_{HHVV}+\mathcal M_{\mathrm{separate}}+\mathcal M_{\lambda_3}\big|^2.
\]
Do **not** claim individual diagrams or arbitrary subamplitudes are separately gauge invariant. Do **not** say that individual diagram-specific cross sections were calculated, or that \(\lambda_3\) has already been constrained. Verify exact diagram IDs against source PDF before printing them. Keep original vector diagrams, include process cards and figure captions with source provenance.

### 4. Older charged-current \(HH\to4b\) / full \(\nu\bar\nu4b\) results

**Different benchmark family**: FCC-\(\mu e\) \(\sqrt s=0.9798,1.9131\) TeV; symmetric muon collider \(\sqrt s=1,2\) TeV. Earlier selection: four bottom/antibottom partons with \(|\eta_b|<5\), two **distinct** \(b\bar b\) pairs satisfying \(110<m_{b\bar b}<130\,\mathrm{GeV}\), **no minimum bottom-parton \(p_T\) cut**, parton-level (not reconstructed jets). Confirm exact pairing algorithm and neutrino flavour sums from actual run cards. Some runs were at \(P_{\mu^+}=0\%,+80\%\); ensure the beam-polarization conventions in the \(\mu^+\mu^-\) configurations are not misrepresented.

| Collider | \(\sqrt{s}\) | Resonant \(HH\to4b\), P0 / P80 [fb] | Complete \(\nu\bar\nu4b\), P0 / P80 [fb] |
|---|---|---|---|
| FCC-\(\mu e\) | 0.980 TeV | 0.04912 / 0.08816 | 0.05355 / 0.09195 |
| \(\mu^+\mu^-\) | 1 TeV | 0.07047 / 0.11582 | 0.07530 / 0.12472 |
| FCC-\(\mu e\) | 1.913 TeV | 0.26478 / 0.47611 | 0.28157 / 0.50745 |
| \(\mu^+\mu^-\) | 2 TeV | 0.30624 / 0.54606 | 0.32480 / 0.57873 |

**Essential branching-ratio warning:** The earlier resonant \(HH\to4b\) simulations used a model-card \(\mathrm{BR}(H\to b\bar b)=0.844640\), not the commonly used precision-SM \(\sim0.58\). Do not compare, renormalize, or project event yields as if identical input parameters were used. If a correction is estimated, show the exact factor, assumptions, and caveats; prefer regeneration using consistent settings. Full \(\nu\bar\nu4b\) includes overlapping resonant, singly-resonant, continuum and interference contributions; it is **not** an independent background, and naive signal subtraction is not a physical background measurement.

### 5. Earlier neutral-current \(4b\), associated Higgs and continuum

Document the exact source-defined processes (verify original run cards before giving any disputed generator syntax):

- \(e^-\mu^+\to e^-\mu^+HH\to e^-\mu^++4b\).
- \(e^-\mu^+\to e^-\mu^+b\bar bH\to e^-\mu^++4b\).
- Complete \(e^-\mu^+\to e^-\mu^+b\bar b b\bar b\).
- The Higgs-excluded continuum diagnostic of the same four-bottom final state.

At FCC-\(\mu e\) \(\sqrt s\simeq0.980\) TeV, unpolarized, earlier cuts include \(p_{T,\ell}>1\,\mathrm{GeV}\) on outgoing charged leptons **at generation level**, plus four b-partons, \(|\eta_b|<5\), two \(110\text{–}130\,\mathrm{GeV}\) pair windows. Representative fiducial cross sections [fb] (verify against original records):

- NC \(HH\to4b\): **0.006382**.
- NC associated \(b\bar bH\to4b\): **0.012925**.
- Full NC \(4b\): **0.007713**.
- Higgs-excluded continuum: **0.0008253**, based on only **88 passing events out of 50,000** (statistically weak).

Higher-energy +80% associated-bbH benchmarks: FCC-\(\mu e\), \(\sqrt s=1.913\) TeV, \(\sigma_{\rm fid}\approx0.081843\) fb; \(\mu^+\mu^-\), \(\sqrt s=2\) TeV, \(\sigma_{\rm fid}\approx0.094913\) fb. Include these only if the corresponding process definitions, cuts, and uncertainties can be verified; highlight limited statistics. The separately produced NC samples overlap in diagram content and **cannot be added as independent exclusive event categories without a coherent definition**.

### 6. Separate muon-collider \(ZH\to4b\) calculation

\(\mu^+\mu^-\to ZH\to(b\bar b)(b\bar b)\), full LO explicitly resonant chain, symmetric muon beams, unpolarized; \(|\eta_b|<5\), both assigned \(b\bar b\) masses **80–130 GeV** (not 110–130 GeV), no minimum b-parton \(p_T\) cut.

| \(\sqrt{s}\) | Before cuts [fb] | Fiducial [fb] |
|---|---:|---:|
| 1 TeV | 1.56450 | 1.52716 |
| 2 TeV | 0.37888 | 0.36929 |

Explain that ordinary same-flavour \(s\)-channel \(\mu^+\mu^-\to Z^*\to ZH\) annihilation has no direct \(\mu^+e^-\) analogue at tree level due to flavour mismatch. Do not present \(ZH\to4b\) as the same final state as \(\nu\bar\nu HH\to\nu\bar\nu4b\).

### 7. Scientific interpretation; completed results versus proposals

- Single-H CC/NC calibrates/helps test \(HWW\) and \(HZZ\) interactions (measurement claims require realistic sensitivity study).
- Double-H tree-level amplitudes involve \(HVV\), \(HHVV\) and off-shell \(H^*\to HH\); interference provides the rationale to study \(\kappa_3\) and \(\kappa_{2V}\), not yet constrained.
- Higgs potential (for physical scalar \(h\), avoid mixing field symbol with a generic function):
\[
V(h)=\tfrac12m_h^2h^2+\tfrac{m_h^2}{2v}h^3+\tfrac{m_h^2}{8v^2}h^4,
\quad \kappa_3=\lambda_3/\lambda_3^{\rm SM},\quad\kappa_4=\lambda_4/\lambda_4^{\rm SM}.
\]
- Proposed coupling study: \(\sigma_{HH}(\kappa_3,\kappa_{2V})\), including \(m_{HH}\), \(p_{T,H}\), angular spectra, interference and HEFT-vs-SMEFT assumptions. Do not vary arbitrary couplings in a way that silently breaks intended gauge relations.
- **Proposed only** triple Higgs:

```text
generate e- mu+ > ve vm~ h h h QCD=0
generate e- mu+ > e- mu+ h h h QCD=0
```

First investigate unpolarized, +80%, +100% points at exact 1 and 2 TeV, numerical feasibility, event yields and possible \(6b\), \(4b2\tau\), \(4b2\gamma\). Never invent HHH cross sections or \(\kappa_4\) sensitivity. If quoting a hypothetical \(\mathcal L\), explicitly mark it illustrative and show \(N=\sigma\mathcal L\) before decay/acceptance.
- Potential electron polarization, if machine-feasible, has the ultrarelativistic CC expectation \(R(P_e,P_\mu)\simeq(1-P_e)(1+P_\mu)\) with polarizations as fractions; realistic luminosity may change. The +80% \(\mu^+\) enhancement alone does not guarantee an 80% improvement in statistical precision.
- Important validation: independent-seed tests, electroweak scheme and parameter card, forward-scattered NC lepton cuts, Higgs branching ratio normalization, higher-order corrections, event selection, detector/b-tagging and realistic beam/luminosity scenarios.

---

## PHASE 2 — EXACT SLIDE-BY-SLIDE SCIENTIFIC BLUEPRINT

**Each entry below mandates one independently substantive scientific slide.** Every main slide must contain (i) its title, (ii) genuinely useful facts, definitions or calculations, (iii) a quantitative figure/table/equation whenever appropriate, (iv) a succinct takeaway or open question, and (v) discreet citation/provenance. Do not use filler or duplicate generic introductions. Aim at research-collaboration discussion, not public outreach. Design each slide to remain legible in a room; when a result table is dense use high-quality typesetting and exploit backup slides for detailed seeds/errors. Reserve exactly 40 frames before `\appendix` and exactly eight after.

### Part I — FCC-\(\mu e\) concept, motivation and FCC-ee synergy (Slides 1–9)

**01 — Higgs Physics Potential of the FCC-\(\mu^+e^-\) Collider at CERN.** AGH title slide; subtitle *From Standard Model Benchmarks to Higgs Self-Couplings*; Hamzeh Khanpour as presenter; Krzysztof Piotrzkowski, Richard Ruiz, Piotr Kotko as meeting participants (not presumed coauthors); no invented exact meeting date. Authentic AGH cover, legitimate branding.

**02 — Scientific Motivation and First-Meeting Objectives.** Explain why a high-energy asymmetric lepton collider can probe the Higgs sector; current results versus unperformed coupling work; meeting decisions: validate common baselines, prioritize processes, agree effective theory and experimental scenario, define deliverables. End with one clear discussion objective.

**03 — Talk Roadmap.** Sections: concept; calculation inventory and methodology; inclusive H/HH; polarization and original MG5 diagrams; older 4b/muon collider comparisons; self-couplings/HHH; collaborative roadmap. Reflect exact section structure and indicate why the talk ends with decisions.

**04 — Why a High-Energy Positive-Muon–Electron Collider?** Asymmetric \(\mu^+e^-\) kinematics, VBF leverage, polarization, low-hadronic-activity lepton initial state, distinction from \(e^+e^-\) and \(\mu^+\mu^-\) annihilation; boost of visible systems and consequences. Use scientific diagram or accurate schematic.

**05 — The 2026 FCC-\(\mu e\) Proposal at CERN.** Reproduce an accurately attributed original proposal machine-layout figure where permitted; identify muon source, acceleration, electron facility/ring, interaction point, possible FCC-ee concurrent operation and neutrino-factory opportunity. Separate concepts from established engineering commitments. Cite original page/figure.

**06 — Beam Energies and Centre-of-Mass Reach.** Derive \(\sqrt s\); table of original 2 TeV/120 GeV and 5 TeV/183 GeV configurations versus exact 1/2 TeV MadGraph benchmark pairs. Show crossed energy pairs only if actually in proposal and label their provenance. Include separate \(\mu^+\mu^-\) benchmark row.

**07 — Luminosity, Staging, and Running Assumptions.** Original proposal's actual machine table; check quoted peak luminosity (including any \(\sim3.2\times10^{34}\,\mathrm{cm}^{-2}\mathrm{s}^{-1}\) claim) and associated energy; distinguish instantaneous luminosity, yearly integrated luminosity scenarios, and speculative projections. Reproducible comparison and caveat.

**08 — FCC-ee and FCC-\(\mu e\): Complementary Higgs Programmes.** Fact-checked FCC-ee 240/365 GeV Higgsstrahlung/precision programme versus high-energy \(WW/ZZ\) fusion and HH at FCC-\(\mu e\). Explain combined information on \(HZZ\), \(HWW\), \(HHVV\), \(\kappa_3\); no unsupported sensitivity percentages. Graphical two-column comparison with source notes.

**09 — Higgs Detectors, Asymmetric Boosts, and Machine Challenges.** Boost direction and forward-lepton acceptance, missing momentum, \(4b\) tagging, forward instrumentation, muon-decay-induced backgrounds, shielding and luminosity realism. Make clear these are detector feasibility questions, not already solved.

### Part II — What we calculated and how (Slides 10–13)

**10 — Complete Inventory of Investigated Higgs Processes.** Organised process map: CC H, CC HH, NC H, NC HH; CC resonant \(HH\to4b\) and complete \(\nu\bar\nu4b\); NC \(HH\to4b\), \(b\bar bH\), full NC 4b and Higgs-excluded diagnostic; muon-collider \(ZH\to4b\). Label each collider and final state, and complete versus proposed.

**11 — CERN MadGraph Workflow and Reproducibility.** MG5_aMC v3.6.4, original process cards, LO/SM, CERN LXPLUS/HTCondor, stable-H versus decays, integrated event samples, seeds, collected archives, MC errors and validation scope. Identify that all 48 inclusive jobs completed but independent physics validation remains.

**12 — Inclusive, Decayed, and Fiducial Cross Sections.** Three distinct definitions with examples; no-cut stable-H inclusive \(\sigma\); resonant \(HH\to4b\) with 110–130 GeV windows; muon ZH with 80–130 GeV windows; NC generation \(p_{T,\ell}>1\) GeV; no shower/detector in original parton-level studies. One clear cut-comparison matrix.

**13 — Beam Polarization, Electroweak Inputs, and Higgs Branching Fractions.** Beam 1 \(e^-\) unpolarized / beam 2 \(\mu^+\), polarization sign; \(P\) scan; SM model/card conventions; explicitly flag older \(\mathrm{BR}(H\to b\bar b)=0.844640\) versus conventional \(\sim0.58\); explain why normalizations must be consistent before sensitivity claims.

### Part III — Richard's four inclusive channels and Krzysztof's HH diagram cross-check (Slides 14–26)

**14 — Four Full-Matrix-Element Inclusive Higgs Channels.** Exact four separate MG5 commands printed in legible type, correctly typeset final states; CC versus NC, H versus HH, complete tree-level generation with no diagram exclusions; couplings investigated.

**15 — Single-Higgs Production: Original CC and NC Feynman Diagrams.** Insert actual original CERN `CC_H/matrix.pdf` and `NC_H/matrix.pdf` vector diagrams, unmodified ID labels. Contrast \(HWW\) and \(HZZ\); note one exported fusion diagram each.

**16 — CC Double Higgs: Four Original MadGraph Diagrams.** Original exported CC_HH matrix with four numbered diagrams; visible legend/contact, separate emission (2,3), virtual \(H^*\to HH\) (4); explain why all must be present. Do not swap with illustrative figure.

**17 — NC Double Higgs: Four Original MadGraph Diagrams.** Original NC_HH matrix, analogous \(HHZZ\), two \(HZZ\) emission graphs and virtual \(H^*\to HH\); preserve IDs; forward NC charged lepton remarks.

**18 — Krzysztof's Question: Are All HH Contributions Included?** Quote or paraphrase the scientific question neutrally. Show complete amplitude, all three classes including contact, off-shell self-coupling, coherent interference. Explain what our diagrams **prove**, and what they do not (not a measured \(\lambda_3\), not separately gauge-invariant diagram rates).

**19 — Richard's Six-Point Polarization Task and 48 CERN Runs.** Reproduce the request professionally, not WhatsApp UI screenshot unless supplied; 4×2×6=48, 30k events/configuration; electron beam0, muon values, machine-vs-exact beam energies, validation and returned outputs.

**20 — Inclusive Cross Sections at 1 TeV: All Channels and Polarizations.** Six-row × four-channel compact scientific table with full production data including MC integration errors; correct fb units and source; highlight P0/P80/P100; use readable layout and optional mini-sparkline.

**21 — Inclusive Cross Sections at 2 TeV: All Channels and Polarizations.** Same for 2 TeV. Highlight CC HH 0.418510→0.754495→0.839521 fb (P0/80/100); NC HH 0.0547116→0.0642989→0.0667703 fb. Clearly distinguish from 1.913 TeV earlier scenario.

**22 — Absolute Production Rates versus Positive-Muon Polarization.** Embed regenerated **original-data** four-panel vector plot (`Figure_1_absolute_cross_sections.pdf`), showing energies, process labels, statistically meaningful error bars and same exact data. Source `48-run CERN MG5 results, preliminary`.

**23 — Polarization Enhancement Ratios: CC versus NC.** Four-panel vector ratio figure (`Figure_2_polarization_ratios.pdf`), including \(R(P)\), six points, both energies, numerical uncertainties and explicit dashed CC SM \(1+p\) expectation; don't invent a corresponding NC theoretical line without scheme check.

**24 — Polarization Slopes and Linearity Tests.** Table of all eight \(A\) fit values and statistical uncertainties, \(\chi^2/\mathrm{ndof}\) and p-values if verified. Distinguish MC fit uncertainties from experimental sensitivities. Use graphic comparing \(A\approx1\) and \(A\approx0.22\).

**25 — Chiral Electroweak Interpretation of Polarization.** Helicity content of W and Z interactions, CC\(\,1+p\), pure-Z-limit \(g_L,g_R\), NC \(A\) expression, why H/HH slopes coincide, EW scheme caveat. This is an analytic interpretation, not an experimental extraction of \(\sin^2\theta_W\).

**26 — Collision Energy Scaling and Illustrative Event Yields.** Data-derived \(\sigma(2)/\sigma(1)\) for four processes; emphasize HH ~5.6 versus H ~1.8–1.9; optional transparent hypothetical \(\mathcal L=3\,\mathrm{ab}^{-1}\) with \(N=\mathcal L\sigma\), no decay/cut/reconstruction. Label luminosity hypothetical, not proposal prediction.

### Part IV — Earlier four-bottom studies and comparison with \(\mu^+\mu^-\) (Slides 27–35)

**27 — CC Double-Higgs-to-4b and Complete \(\nu\bar\nu4b\) Processes.** Exact final-state distinctions for FCC-\(\mu e\) and muon collider, flavour sums only as verified, resonant HH versus full amplitude, missing neutrinos, relevant physics goals.

**28 — Four-Bottom Pairing and Fiducial Selection.** Define \(|\eta_b|<5\), two distinct charge-opposite \(b\bar b\) pairs each in 110–130 GeV, no minimum b \(p_T\), source-defined pairing algorithm, generator-level vs reconstructed jets. Show selection flow schematic and an explicit note that ZH uses 80–130 GeV elsewhere.

**29 — Fiducial CC HH and Complete 4b: FCC-\(\mu e\) vs Muon Collider.** Display all four collider/energy rows with unpolarized and +80% \(HH\to4b\) and full \(\nu\bar\nu4b\) values; use source cuts and branching ratio note. Note muon collider energy mismatch with FCC-\(\mu e\) exact \(\sqrt s\) for this historical study.

**30 — Resonant HH, Nonresonant 4b and Interference.** Complete tree-level amplitude, overlapping resonant and continuum diagrams, pair windows and caution why subtracting an HH contribution does not isolate a physical independent background; next studies of differential amplitudes/phase space.

**31 — NC Four-Bottom Channel Definitions.** Four NC source-defined processes and Higgs-exclusion diagnostic; forward outgoing charged leptons, \(p_{T,\ell}>1\) GeV generation cut, actual mass windows and sample overlap. Use a channel matrix not fake new MG5 commands.

**32 — NC Four-Bottom Cross Sections and Their Limitations.** Four 0.980 TeV preliminary fiducial numbers (0.006382, 0.012925, 0.007713, 0.0008253 fb), 88/50k continuum passing statistic; discuss significance, incomplete convergence and interference, no naive addition.

**33 — Associated \(b\bar bH\) at Higher Polarization and Energy.** Introduce source-verified +80% FCC-\(\mu e\) 1.913 TeV \(\sim0.081843\) fb and \(\mu^+\mu^-\) 2 TeV \(\sim0.094913\) fb, only after checking exact process definitions, cuts and stats. If unavailable, show verified partial table plus explicit unverified-source warning, not an invented comparison.

**34 — Muon Collider \(ZH\to4b\): A Distinct Four-Bottom Topology.** Explicit resonant muon-collider process; before/after cuts at 1 and 2 TeV; wider 80–130 GeV pair windows, no min b \(p_T\), no standard flavour-off-diagonal \(s\)-channel \(\mu^+e^-\to ZH\) analogue. Explain physically distinct neutrino/missing-energy situation.

**35 — Lessons from the Four-Bottom Programme.** Synthesize channels, machine comparisons, acceptance, signal/background overlap, branching-fraction issue, known limitations and transition to detector-level phenomenology. Avoid claiming a realistic signal-to-background or sensitivity already exists.

### Part V — Higgs potential, new calculations and collaboration action plan (Slides 36–40)

**36 — The Higgs Trilinear Coupling and \(\kappa_3\)–\(\kappa_{2V}\) Sensitivity.** Higgs potential, original HH diagrams, interference, coupling modifiers, qualitative threshold/high-\(m_{HH}\) behavior, proposed consistent two-dimensional scan. Distinguish Krzysztof's proposal/literature-rescaled \(\lambda_3\) projections from our direct MG5 cross sections.

**37 — Differential Observables, HEFT/SMEFT, and Parameter Degeneracies.** \(m_{HH}\), \(p_{T,H}\), \(\theta_H\), outgoing lepton \(\eta\)/\(p_T\), missing momentum; EFT basis/validity and gauge consistency; combined CC/NC and FCC-ee input. Show specific prospective analysis workflow, not fabricated limits.

**38 — Beyond HH: Triple-Higgs Production and the Quartic Coupling.** Two proposed MG5 HHH commands, \(\lambda_3,\lambda_4\) contribution classes, 1/2 TeV feasibility, P0/P80/P100 first tests, raw-yield threshold and possible 6b/4b2\(\tau\)/4b2\(\gamma\) decays; no generated HHH numbers, no sensitivity claim.

**39 — Collaboration Work Packages and Decisions on Responsibilities.** Concrete workstreams: QA/inputs, consistent model & EW parameters, \(\kappa_3/\kappa_{2V}\) runs, differential data, backgrounds/detector, HHH feasibility, machine energy/polarization/luminosity assumptions, literature benchmarking; list deliverables and discussion questions. Do not assign Krzysztof, Richard, Piotr or Hamzeh specific tasks without their agreement.

**40 — Summary: Results Established and Decisions for the Kick-off.** Quantitative takeaways (48 runs, CC H/HH energy growth, CC P80 ~1.8, NC P80 ~1.175, original HH diagrams confirmed); 4–6 explicit decisions needed; realistic next artifact and paper strategy. End on a research question—not an extra thank-you slide.

### Eight substantive backup frames — B1–B8

**B1 — FCC-\(\mu e\) Machine Working Points and Primary Proposal Sources.** Complete original machine-parameter table, conditions, staged operation, precise source page; all sourced.

**B2 — Full MadGraph Process and Generator-Settings Inventory.** Four inclusive commands and all verified historic process/decay chains, model/card references, cuts, flavour sums, polarization. Avoid unsourced command reconstruction.

**B3 — Complete 1 TeV 24-Point Scan with Errors and Seeds.** All six polarizations × four channels with full CSV precision, MC uncertainties, run IDs/seeds if sourced; readable split within frame by two-column table only if it fits, not microscopic type.

**B4 — Complete 2 TeV 24-Point Scan with Errors and Seeds.** Analogous full source-backed numerical inventory.

**B5 — Original MG5 Diagram Sources and Numbering.** Original CC H, NC H, CC HH, NC HH exports and exact diagram IDs; include process commands and provenance; avoid unlegible montage.

**B6 — Four-Bottom Pairing, Cut Tables, and BR Normalization.** Detailed comparison of 110–130 and 80–130 windows, 1 GeV NC lepton threshold, \(|\eta_b|<5\), no min b \(p_T\), old Higgs BR card issue and interference warning.

**B7 — Calculation Reproducibility and Numerical Validation.** Archive counts, seeds, event requests, generator/integration errors, fit QA, missing independent tests, NC forward-region concerns and independent-seed validation plan.

**B8 — References and Scientific Context.** Complete citations for proposal, FCC-ee, relevant prior e\(\mu\) HH/HHVV papers, internal CERN reports, diagrams and original results; source dates where relevant. Cite only verified references.

---

## PHASE 3 — FIGURES, SCIENTIFIC EDITING AND TYPOGRAPHY

1. **Figures:** Reproduce or directly include original vector plots for all four inclusive processes. If available, run the supplied Python plotting script on actual 48-row CSV (do not digitize supplied screenshot, invent data points or alter error bars). Include generated PDF vector outputs and PNG previews plus plotting source and data in ZIP. The two principal plot names should be `Figure_1_absolute_cross_sections.pdf` and `Figure_2_polarization_ratios.pdf`. Plot legends must identify \(\sqrt s\), e.g. 1 TeV and 2 TeV; axes need percent and fb; ratios must state denominator. Colorblind-safe palette with distinct marker/line styles, readable at presentation scale.
2. **MadGraph diagrams:** Use actual exported original `matrix.pdf` vector diagrams with original numbering. Embed CC_HH and NC_HH on separate main slides. Annotate on-slide without obscuring propagators/vertices; explicitly label diagrams 1, 2/3, 4 and their physics. Include the originals and legal annotations in ZIP.
3. **Machine design:** Use a sourced original FCC-\(\mu e\) proposal scheme when permitted. If original vector figure cannot be retrieved, draw a new accurate schematic labeled `schematic—not to scale` and reference design source; never invent detailed technical infrastructure.
4. **FCC-ee complementarity:** A two-column scientific comparison is preferable to gratuitous images. Source any FCC-ee energies/luminosities and describe as projected capabilities, not completed measurements.
5. **Scientific notation:** Consistently \(\mu^+e^-\), \(\bar\nu_\mu\nu_e\), \(b\bar b\), \(HH\), \(HHH\), \(P_{\mu^+}\), \(\kappa_3\), \(\kappa_{2V}\), \(\kappa_4\). Quote \(\sigma\) in fb and explicitly label pb where needed; avoid \(\sigma_0\) confusion. Distinguish right-helicity \(\mu^+\) from right-*chiral* muon fields.
6. **Slides:** Prefer readable scientific hierarchy, concise mathematical statements, compact comparisons, original plots and informative takeaways. Do not create a full-width wall of small text. Use robust 16:10 margins; make tables readable. References/figure provenance can be smaller than the main text but must be decipherable.
7. **Content fairness:** Avoid inflated novelty or claims of competitiveness without luminosity/background studies. Explicitly identify existing electron–muon HH/HHVV literature and formulate a distinct contribution: combined CC/NC, polarization, differential observables and coupling correlations.
8. **Cross-section provenance:** The original measured/generated result is LO. MC integration uncertainty is neither QCD/EW theory uncertainty nor detector statistical precision. Use correct benchmark family and model-card normalization on every older result slide.
9. **Error-handling:** If a particular historical result cannot be verified from available source files, include only source-supported facts and a transparent `verification needed` note in appropriate slide/manifest. Do not omit an entire requested topic if a qualitative scientifically sound discussion can be included. Do not fill missing source gaps from conjecture.

---

## PHASE 4 — REAL BUILD, VISUAL INSPECTION AND SCIENTIFIC ACCEPTANCE TESTS

**Execute each phase, record actual outcomes, and fix failures.**

1. **Preflight inventory:** Locate attachments and actual source files. Build `SOURCE_MANIFEST.md`; check availability of TeX engine, AGH theme, diagram PDFs, original numerical data and plotting dependencies. Detect missing images and potential TeX package incompatibilities. Select sane fallback only when faithful theme and scientific content are preserved.
2. **Source reconciliation:** For each requested result, compare relevant original PDF/CSV/run card. Record discrepancies, missing files and important physical assumptions. For proposal PDF, verify paper citation, machine-energy table, actual luminosity and original figure pages; if public web verification unavailable, say so and do not invent details.
3. **Data preparation:** Verify exactly 48 unique inclusive dataset entries: 4 channels × 2 energies × 6 polarization values; no duplicates or missing rows, no negative or invalid cross sections; 30,000 events each only when records confirm. Reproduce all eight slope fits, report method and numerical caveats. Keep source input CSV unchanged; generate derived tables separately.
4. **Figure generation:** Generate/reuse vector figures and diagrams; check units, labels and uncertainty displays. Include original image source manifest and scripts; inspect output visually.
5. **Create complete LaTeX project:** A clean folder `FCCmue_Higgs_Physics_Kickoff_2026/` containing main `FCCmue_Higgs_Physics_Kickoff_2026.tex`, local AGH styles, figures, data, scripts, references and QA documents. All `\includegraphics` and inputs must use portable **relative paths**. Ensure no orphaned source images or external absolute `/mnt/data` paths are required for rebuilding.
6. **Compile:** Use `latexmk -pdf` or appropriate `pdflatex` passes. If bibliography requires an extra pass, run it. Fatal errors, unresolved assets and broken TikZ/graphics are not acceptable. Inspect `.log` and fix overfull boxes and warnings caused by actual content, not blindly suppress warnings.
7. **Render/check actual pages:** Determine PDF page count with a PDF tool (`pdfinfo`, `pypdf`, etc.), target **48 pages**. Render a contact sheet and high-resolution key pages: title, proposal, energy table, diagrams 15–18, numerical tables 20–21, plots 22–23, fitting results, 4b selections/tables, coupling/HHH roadmap, closing slide, and all backups. Fix clipping, tiny fonts, unreadable axes, image collisions, wrong scientific symbols, reference overflows. Check AGH header/footer and 16:10 aspect on every page.
8. **Scientific QA:** Create `SCIENTIFIC_QA_REPORT.md`, with explicit PASS/FAIL/NOT VERIFIED for: 40+8 slides, exact benchmark separations, all four inclusive process syntax, 48 cross sections, eight slopes, original MG5 diagram counts/labels, right-helicity muon convention, four-bottom cut distinctions, BR discrepancy, NC lepton cut, complete/full 4b interference distinction, ZH before/after rates, no fictional HHH results, proposal versus generated results, and attribution/reference correctness. No false blanket claim of publication-grade independent convergence.
9. **Rebuild test:** If possible compile from the ZIP-extracted complete project in a fresh temporary directory. Verify archive integrity, existence and nonzero size of each required output. Maintain external-asset license/source notes.
10. **Final user-facing delivery:** Provide separate verified links to `.tex`, `.pdf`, `.zip`, state exact main/backup/PDF page counts, summarize what was compiled and checked, flag any real scientific limitation, and include no invented output paths. Do not promise background work or a future delivery. A partial-but-real deliverable with transparent limitations is superior to a fictional complete deliverable; nevertheless make a serious best-effort to deliver the full contracted package in the current response.

### Build README required content

`README_BUILD.md` must specify Python dependencies (when regeneration is needed), installed LaTeX toolchain, command(s) to regenerate plots, primary `pdflatex`/`latexmk` build command, directory layout and relative asset paths, and distinction between main and backup slides. `SOURCE_MANIFEST.md` must include original filenames/links, page/tables, obtained-vs-missing status, and any permissions/attribution. `SLIDE_CONTENT_MAP.md` must trace all 48 frames. `SCIENTIFIC_QA_REPORT.md` must report actual test execution and exceptions.

---

## FINAL OUTPUT CONTRACT AND UNAMBIGUOUS EXECUTION INSTRUCTION

**Do not ask me to select a slide count, deck style, energy benchmarks, collider participants or output type: those are fixed above.** Read relevant files, browse trustworthy primary literature where needed, create and compile the 48-page AGH Beamer deck, review it, and deliver the actual three files. Do not deliver a further master prompt, an outline in place of slides, a set of uncompiled code snippets, or fabricated links.

At the end of execution, the user must receive:

- A verified, separately downloadable **`FCCmue_Higgs_Physics_Kickoff_2026.tex`**.
- A verified, separately downloadable, actual compiled **`FCCmue_Higgs_Physics_Kickoff_2026.pdf`**.
- A verified, separately downloadable, portable **`FCCmue_Higgs_Physics_Kickoff_2026_COMPLETE.zip`** containing the full working project and science QA.

**EXECUTE_PRODUCTION_NOW = YES**

**PRODUCE_ACTUAL_SLIDES = YES**

**EXACTLY_40_MAIN_SLIDES_AND_8_BACKUP_SLIDES = YES**

**PRESERVE_AUTHENTIC_AGH_BEAMER_THEME_16_10 = YES**

**VERIFY_ORIGINAL_48_CERN_CROSS_SECTIONS_AND_ALL_MG5_DIAGRAMS = YES**

**COMPILE_AND_VALIDATE_PDF = YES**

**FINAL_DELIVERY = TEX + PDF + COMPLETE_ZIP**

**NO_PLACEHOLDERS_OR_INCOMPLETE_DELIVERABLES = YES**
