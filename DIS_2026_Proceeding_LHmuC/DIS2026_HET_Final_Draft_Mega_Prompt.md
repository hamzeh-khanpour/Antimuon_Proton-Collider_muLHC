# DIS2026 HET Proceedings — Final-Draft Execution Mega-Prompt

Version 1.0 · Author decisions incorporated: 15 October 2026

**BEGIN ACTIVE MANUSCRIPT EXECUTION PROMPT**

## 1. Execution contract and completion objective

Act as a senior collider phenomenologist, scientific editor, and LaTeX proceedings author. Read this entire prompt and the supplied materials, then produce the complete final author-review draft of the DIS2026 proceedings contribution specified below. Carry the work through source selection, writing, LaTeX implementation, compilation, visual inspection, revision, and delivery of the actual manuscript files.

This is a manuscript-production request. Do not stop after proposing an outline, returning another prompt, summarizing the sources, or offering to draft later. Resolve routine editorial and implementation choices autonomously and continue until the requested deliverables are complete, subject to genuine input or environment limitations.

Use the HELP4CERN numerical results unchanged for this draft. Numerical corrections have explicitly been deferred by the author. The source discrepancies described below are recorded for later revision and are not permission gates for drafting.

“Final draft” means a complete, polished manuscript for the author's review under that numerical policy. Do not imply that deferred scientific corrections, collaboration approval, current submission compliance, or publication have been completed unless separately established. Do not submit the article, contact anyone, or seek account credentials.

The article must occupy **no more than seven PDF pages in total**, counting the title/abstract page, every figure, table, caption, acknowledgment, and reference. Deliver the source project and the compiled PDF when compilation is possible, together with a separate validation and deferred-corrections note. That note is not part of the proceedings PDF.

## 2. Fixed identity and audience

Use these details exactly:

| Field | Required content |
| --- | --- |
| Title | Perspectives for HET physics studies at a muon-hadron collider at CERN |
| Sole named author | Hamzeh Khanpour |
| Study-group attribution | (on behalf of HELP4CERN Study Group) |
| Affiliation | AGH University of Krakow, Faculty of Physics and Applied Computer Science, Al. Mickiewicza 30, 30-055 Kraków, Poland. |
| Publication email | hamzeh.khanpour@cern.ch |

Keep the study-group attribution distinct from a list of named coauthors. Use the appropriate PoS speaker designation for Hamzeh Khanpour. Do not add academic titles, copy other authors from the template, or replace the publication email with an account email.

Write in English for a DIS/HEP researcher who has not seen the presentation. Define HET as Higgs, electroweak, and top physics. Build a coherent Higgs-led argument for the proposed CERN muon-hadron programme, with concise photon-induced physics and BSM perspectives. Retain a clear connection to the DIS2026 talk while identifying any later workshop material used as supplementary context.

## 3. Inputs, source roles, and precedence

Locate these inputs by their actual contents and filenames:

| Input | Role |
| --- | --- |
| `HELP4CERN.zip` | Primary scientific source; numerical authority for retained HELP4CERN results and authority for its versions of conflicting same-named graphics. |
| `DIS_2026_Slides_LHmuC.zip` | Record of the DIS2026 presentation; determines the connection to the conference contribution and supports presentation-specific context. |
| `Ultra-cold-muons_2026_TwoPhoton_LHmuC.zip` | Supporting source for photon-induced physics and explicitly identified later developments. |
| `DIS2024_Proceeding.zip` | Supplied LaTeX formatting and structural starting point. A readable `DIS2024_Proceeding(1).zip` duplicate is acceptable after checking its identity. |
| `DIS2026_HET_Source_Review_and_Content_Decisions.html` | Source review and content handoff; use the author-updated REVISION 2 dated 15 October 2026 when supplied. |

Apply explicit current author instructions first. Otherwise follow the settled decisions embedded in this prompt and the active author-updated report. Use HELP4CERN for its retained numbers and graphics; use the talk and workshop sources for their assigned contextual roles. Use official conference instructions for current formatting and primary bibliographic records for reference metadata. Neither an external paper nor a newer slide deck silently overrides the frozen HELP4CERN numbers.

The report's collapsed historical audit contains useful evidence and source pointers. Its old requirements to resolve numerical discrepancies before drafting, earlier display selection, and earlier page allocation are superseded. If an old review command or the command that created this mega-prompt is attached, treat it as workflow history; its instruction to stop before manuscript writing does not apply to this execution run.

This prompt embeds the decisions needed to work in a fresh conversation. The HTML report supplements them. If the report is absent, proceed using these embedded decisions and record that limitation; do not invent report contents. The scientific archives and required assets still need actual access.

## 4. Source access and focused inspection

Preserve the original archives. Extract separate working copies and identify the entry points, included sections, bibliography, figures, and supporting notes. Keep archive provenance in the working directory structure so identical filenames from different packages cannot overwrite one another.

Verify readability and inspect the content used, rather than assuming access from an attachment label or old path. Follow relevant LaTeX `\input` and `\include` dependencies. Distinguish active source from commented includes, abandoned drafts, editorial markup, backup material, and text after the active `\end{document}`. Review the presentation context needed to describe selected results accurately.

Use the existing review to focus inspection rather than repeat the whole source audit. Prioritize:

- HELP4CERN's executive-summary benchmarks, rate table, first active figure, Higgs analysis, coupling fit, retained EW/top discussion, photon section, and selected BSM outlook.
- The actual axes, legends, captions, and benchmark labels of every included graphic.
- The DIS presentation sections corresponding to the article's main narrative and any workshop pages supporting a selected supplementary statement.
- The DIS2024 main document, `pos.sty`, bibliography mechanism, conference block, and build requirements.

Useful HELP4CERN locations in the reviewed copy are `main.tex` around lines 145–147 for the nominal benchmark, 205–219 for `tab:i`, 239–245 for the first figure, 296–350 for the dedicated Higgs study, 356–379 for the global fit, and 624–625 for leptogluon exposures. Line numbers are navigation aids; locate the actual labels and content if they move. The 500 GeV machine table may be in an included section.

If a required archive or asset is genuinely unavailable, name it precisely, continue independent work, and distinguish the incomplete result from a fully verified manuscript. Do not substitute a different physical plot or fabricate missing data. Ask only for genuinely necessary missing material after making all useful progress.

## 5. Numerical policy and the three deferred issues

**Use the numbers already present in the supplied HELP4CERN draft. Do not correct, average, refit, or replace them during this run.**

Preserve source values, significant digits where practical, units, uncertainty definitions, and necessary qualifications. Selective inclusion is allowed: the policy does not require reproducing every result in the white paper. It does require that every retained HELP4CERN result use its HELP4CERN value and that the manuscript avoid stronger scientific claims than the evidence supports.

| Deferred issue | Required drafting treatment | Companion-note treatment |
| --- | --- | --- |
| Higgs/top benchmarks and polarization differ across sources | Reproduce HELP4CERN Table 1 completely with its stated polarization assumptions and unpolarized entries. Do not claim all calculations have been reconciled. | Record the conflicting benchmark, reference-energy, and polarization questions for later review. |
| Quoted h→bb̄ precision versus exposure | Preserve 1.19%/0.69% rate precisions and 0.77%/0.60% coupling precisions. Keep the study distinct from the general machine luminosity table. Do not assert independent validation of 0.69% at 1 ab⁻¹. | Record that the previous arithmetic check corresponds approximately to 500 fb⁻¹ for the second result, rather than the general 1000 fb⁻¹ benchmark. This is an audit observation, not a newly approved exposure assignment. |
| Different same-named Higgs-fit figures | Use the HELP4CERN files and values, with captions and discussion matching those files. | Preserve the version difference for a later correction/provenance review; no new fit-run record is required to draft now. |

Do not substitute the audit's recomputed h→bb̄ values, import another package's coupling bars, or silently set every analysis to the generic luminosity. Do not turn an inferred 500 fb⁻¹ interpretation into a corrected manuscript benchmark. If a local study exposure remains incompletely specified, describe the values as source-reported study projections, retain their known assumptions, and avoid an unsupported exposure claim.

Scientific limitations needed to interpret a result belong in the article. The detailed discrepancy register, editorial questions, and requests for later corrections belong in the separate companion note. This separation must not conceal a material assumption or make a known ambiguity appear resolved.

Correct grammar, spelling, citation-key case, LaTeX syntax, and obsolete metadata as needed. These are authorized editorial repairs. Do not transform such repairs into changes to the physics. Record a genuinely new substantive inconsistency if found, use qualified source-faithful wording where possible, and continue without reopening settled decisions.

## 6. Article structure and writing objectives

Use this primary structure, adjusting heading wording or merging short subsections only when it improves the limited space:

1. **Introduction, collider benchmarks, and HET rates:** establish the proposed machine, the three muon-energy options, high-Q² motivation, and inclusive HET rates; introduce both required tables and the first figure.
2. **Higgs production and precision prospects:** connect CC/NC production to the dedicated h→bb̄ study and then to the exploratory combined coupling fit; include the HELP4CERN vector panel.
3. **Electroweak and top physics:** explain mechanisms and source-supported opportunities, using the required rate table rather than another quantitative display.
4. **Photon-induced physics:** introduce the EPA description and selected τ-pair/W-pair opportunities; include the optional two-panel display only if it fits legibly.
5. **BSM perspectives and conclusions:** give a compact μq/μg outlook and the principal supported conclusions; acknowledgments, if justified, remain within this allocation.

Use an abstract of approximately 140–180 words as a starting point, subject to the actual title-page layout. State the proposal, the selected physics programme, representative source-supported findings, and their projection status. Write the final abstract after the body is stable. Do not introduce claims or precision numbers in the abstract that are absent from the main text.

For each major result, explain the question, the mechanism, the relevant assumptions, the result, and its scientific implication in connected prose. Avoid a catalogue of slide bullets, a general collider review, or textbook-level background. The physics message should remain understandable if the reader has neither the talk nor the white paper open.

## 7. Required cross-section table — HELP4CERN Table 1

Reproduce the complete numerical content of `HELP4CERN/main.tex`, table label `tab:i`. Prefer to make it proceedings **Table 1** by introducing it before the separate benchmark table. Retain all five beam-energy columns and all four processes.

All values below are in **pb**. These shortened row labels are transcription checks; use the source process definitions in the article.

| Process | LHeC 20 GeV | LHeC 60 GeV | LHμC 500 GeV | LHμC 1 TeV | LHμC 2 TeV |
| --- | ---: | ---: | ---: | ---: | ---: |
| CC Higgs + jet | 0.052 | 0.197 | 0.656 (unpol. 0.438) | 1.092 | 1.744 |
| NC Higgs + jet | 0.0056 | 0.024 | 0.150 (unpol. 0.135) | 0.245 | 0.383 |
| NC top–antitop | 0.0015 | 0.0323 | 1.03 | 2.23 | [blank] |
| CC single top | 0.55 | 2.89 | 21.26 | 36.77 | [blank] |

The source process definitions are the generic lepton–proton expressions for νₗH+jet+X, lH+jet+X, ltt̄+X, and νₗt+X. Transcribe them from the source without silently changing charge conventions or claiming a different perturbative calculation. `[blank]` is an instruction to leave the corresponding scientific entry empty, not literal manuscript text. A blank does not mean zero.

Retain the source caption's 80% electron polarization and 50% antimuon polarization. Do not invent their signed convention. Preserve the explicitly unpolarized 500 GeV Higgs entries. Remove blue editorial formatting and author comments from the presentation; improve caption grammar and mention the existing 2 TeV column without changing physics.

Do not implement the source's pending 50-to-60 GeV numerical update, fill the 2 TeV top cells, or substitute old slide rates. Do not infer that NLO PDFs or the name of a simulation package establishes NLO accuracy of the hard process. Use restrained descriptions of source-reported rates when the calculation metadata remain under review.

Make the table legible through sensible column headings, line breaks, and normal proceedings table conventions. Do not solve width problems by deleting information, distorting the table, or making it unreadably small. Cite it in the prose and explain its role as the rate basis for the HET discussion.

## 8. Required LHμC beam-energy and luminosity table

Add a separate compact benchmark table, preferably proceedings **Table 2**, with the following explicit distinctions:

| Option | Muon beam energy | Proton beam energy | √s_μp | Integrated-luminosity statement |
| --- | --- | --- | --- | --- |
| Initial | 500 GeV | 7 TeV | 3.74 TeV, approximately 3.7 TeV | 250 fb⁻¹ is explicitly used for the 500 GeV leptogluon study; identify it as study-specific. |
| Nominal | 1 TeV | 7 TeV | 5.3 TeV | 1 ab⁻¹ ultimate LHμC sample; the executive summary also states a 250 fb⁻¹ case. The leptogluon analysis separately uses 500 fb⁻¹. |
| Higher energy | 2 TeV | 7 TeV | 7.5 TeV | 1 ab⁻¹ under the executive summary's ultimate LHμC luminosity assumption. |

Use concise column entries and a short note for the alternative exposures if that improves layout. Preserve the distinction between a general ultimate target and an analysis-specific sample. Do not promote the 500 GeV 250 fb⁻¹ exposure to a universally reconciled design assumption, and do not impose a universal 250/1000/1000 fb⁻¹ assignment from the slide decks over these source distinctions.

The head-on high-energy relation is

\[
s_{\mu p}\simeq4E_\mu E_p,\qquad
\sqrt{s_{\mu p}}\simeq2\sqrt{E_\mu E_p}.
\]

Use it only if useful for explanation or a simple units check, retaining the source's quoted rounding. Distinguish beam energy from collision energy and μp energy from photon-photon invariant mass. State luminosities as projected study assumptions, not delivered measurements.

Integrated luminosity is sufficient for this required table. If instantaneous luminosity is discussed, distinguish cm⁻²s⁻¹ from fb⁻¹/ab⁻¹. The nominal executive-summary estimate is approximately 10³⁴ cm⁻²s⁻¹; the 500 GeV performance table gives 4.3×10³³ cm⁻²s⁻¹ with a “Peak(?)” source qualification. Do not turn that uncertainty into a definitive peak/average claim. Omit this nonessential detail if it consumes space without helping interpretation.

## 9. Required first figure — kinematic coverage

Use the original vector PDF `HELP4CERN/dis_eta_acceptance.pdf`, the first active figure in `main.tex`, labelled `fig:xbj_vs_q2_phase_space`. The nearby `xbjq2_diagram.pdf` include is commented out and is not the selected asset. The later Higgs-fit graphic is not the requested Figure 1.

Keep this as the first proceedings figure where feasible. Reuse the original PDF without scientific alteration. Preserve the plotted beam configurations, axes, data regions, acceptance information, and legend. In particular, the LHeC reference plotted at 50 GeV must not be relabelled as 60 GeV to agree superficially with the cross-section table. Preserve the plotted 20/50 GeV electron options and 1/2 TeV muon options as actually shown.

The source caption uses the inelasticity range \(4\times10^{-3}<y<1\). Inspect the graphic for configuration-specific acceptance details and keep the caption consistent with them. Explain that the plot locates the high-Q² reach relevant to the HET programme while keeping the wider QCD discussion brief.

Use the original vector asset in the LaTeX project, not a screenshot of the review's embedded preview. Scale uniformly and verify the axes and legends at the final print size. Caption editing may improve readability and attribution; it must not change the physical content.

## 10. Dedicated Higgs study and uncertainty interpretation

Explain CC and NC Higgs production with their appropriate final-state signatures and connect the source rates to the dedicated charged-current h→bb̄ study. The source study uses the μ⁺p channel with a jet, an antineutrino, and a Higgs decaying to bb̄. Preserve the actual charge convention; do not import the μ⁻ setups of a related external paper as though they were the HELP4CERN benchmark.

Distinguish inclusive Higgs cross sections in Table 1 from cross sections including a branching fraction, accepted event counts, statistical precision, and extracted coupling precision. Retain the two source-reported rate uncertainties **1.19% and 0.69%** and coupling uncertainties **0.77% and 0.60%** in source order. Identify the studies consistently; if the energy mapping is supplied by the talk rather than explicit local HELP4CERN labels, preserve that provenance in the companion map. Do not infer a luminosity assignment from the size of an error bar.

The source defines statistical rate precision by

\[
\frac{\Delta\sigma}{\sigma}=\frac{\sqrt{N_s+N_b}}{N_s}.
\]

State that this is a statistical estimate. Do not describe it as a complete experimental uncertainty including all detector, theory, normalization, and background-systematic effects. Describe the dominant CC multijet and Z→bb̄ backgrounds and only the source-supported selection assumptions needed for interpretation.

The reviewed source includes an LHeC-like detector treatment, a stated 75% b-tagging factor, exactly two selected b-jets, and a mass window \(|m_{bb}-m_h|<25\,\mathrm{GeV}\). Confirm those details against the actual source before using them. Do not silently decide whether a tagging factor has already been applied to an efficiency or multiply it again. Keep detailed generator versions and cut tables out of the short article unless they materially clarify the result; retain their provenance in the companion note where useful.

The coupling extraction uses the external combination \(R=g_{hWW}^{2}/\Gamma_h\), with the source-reported relative uncertainty **0.985%**. Explain its role and cite its actual methodological provenance. The source relation is

\[
\sigma(\mu^+p\to j\bar\nu_\mu h)\,\mathrm{BR}(h\to b\bar b)
\propto R\,g_{hbb}^{2},
\qquad
\frac{\Delta g_{hbb}}{g_{hbb}}
=\frac12\sqrt{\left(\frac{\Delta\sigma}{\sigma}\right)^2+
\left(\frac{\Delta R}{R}\right)^2}.
\]

Include only the equation or compact relation needed by the final exposition. If the uncertainty-propagation equation is shown, identify its source assumptions, including the external input and the treatment implicit in adding uncertainties in quadrature. Do not present a fresh fit or claim that the coupling precision is model-independent or obtained from LHμC data alone.

Keep the approximately 500 fb⁻¹ audit interpretation in the deferred record. The manuscript may describe the quoted projections with their known assumptions and exposure caveat where necessary, but must not certify 0.69% at 1 ab⁻¹ or silently adopt a corrected exposure. Do not replace the frozen precisions with newly calculated values.

## 11. Exploratory global Higgs fit and selected vector panel

Retain **`HELP4CERN/LHmuC_vector.pdf`** as the selected Higgs-coupling figure. Copy that asset from HELP4CERN, even if another package contains a file with the same name. Inspect the actual legend and bars before writing the discussion. The selected HELP4CERN combined-stage κ_W values are **0.28%, 0.19%, and 0.16%** for its three LHμC-stage combinations; use the actual legend to identify their datasets.

Explain the distinction between the dedicated h→bb̄ analysis and this exploratory combined fit. The source rescales LHeC signal-strength information using rate changes while retaining assumptions about systematic factors, acceptance, efficiency, and background effects. Do not describe that procedure as an independently established detector-level sensitivity for every channel.

Preserve the following interpretation:

- The κ-3 framework and the stated SMEFiT implementation/context.
- The actual combinations of HL-LHC, LHeC, and LHμC stages shown, including the HL-LHC baseline and the meaning of its improved PDF/α_s treatment.
- The constraint \(\kappa_V(\kappa_W,\kappa_Z)\le1\), its role when the Higgs width is not directly fixed by these collider measurements, and the model dependence it introduces.
- The vector-modifier uncertainty convention \(1-\kappa_V(68\%)\); do not casually reinterpret it as a symmetric Gaussian error.
- The preliminary/exploratory nature of the projections and the distinction between combined and standalone capabilities.

The original white-paper caption describes several panels. Write a caption appropriate to the selected vector panel only, removing obsolete “top/bottom” or fermion/loop-panel references while retaining all qualifications relevant to the vector result. Do not replace it with a caption from the conflicting DIS figure.

Avoid unsupported universal rankings against all proposed colliders. Comparisons require the same observable, fit assumptions, combined datasets, and confidence convention. A concise explanation of complementarity is preferable when the short article cannot support a controlled numerical comparison.

## 12. Electroweak and top discussion

Use the high-Q² reach to motivate electroweak studies and explain the source-supported CC single-top and NC top-pair channels. Refer to Table 1 for their rates. Preserve lepton-charge and neutrino conventions where stated, and distinguish the generic source table notation from a charge-specific subprocess discussion.

Discuss weak-mixing-angle, gauge-coupling, Wtb, CKM, EFT, FCNC, or rare-top opportunities only to the extent supported by the selected sources. Separate an opportunity motivated by kinematics and rates from a completed precision or exclusion study. Do not derive a measurement uncertainty from a large inclusive event sample or invent a numerical reach to make this section appear more quantitative.

Keep detector acceptance and clean-event arguments proportionate and qualified. Do not promote an expectation of low pileup into proof that all backgrounds or systematics are negligible. Avoid a second top-rate table, extra top plots, a long operator list, or broad textbook exposition.

## 13. Photon-induced physics and optional display

Describe the equivalent-photon approximation at the level needed to interpret the retained results. Separate the μp collision energy from \(W_{\gamma\gamma}\), the photon-photon invariant mass. Distinguish the effective photon luminosity from the γγ subprocess cross section and from the resulting μp cross section.

Where useful, a schematic convolution may explain the normalization, but define the luminosity convention actually used before writing an equation. Preserve whether the calculation is elastic, dissociative, or a combination; the relevant photon-virtuality cuts; thresholds and fiducial restrictions; and any stated tagging or survival assumptions. Do not imply detector-level yields when the source gives an EPA production estimate.

Use τ-pair and W-pair production as representative opportunities where supported. If quoting a rate, take its numerical value and associated definition from HELP4CERN. Do not substitute a discrepant workshop value. Keep cumulative \(\sigma(W>W_0)\), differential distributions, and subprocess cross sections distinct, with their actual units.

Treat anomalous-moment or anomalous-coupling curves as illustrative benchmark deformations unless the source supplies a statistical limit construction, uncertainty model, and confidence definition. Do not convert a visible distribution difference into an exclusion or discovery reach. Do not reproduce questionable source formulas merely to fill space; a concise qualitative treatment is sufficient for optional material.

The supporting display may combine the reviewed `Sgg.jpg` photon-luminosity panel and `yytautau.jpg` τ-pair panel from the DIS package. Verified identical workshop copies are acceptable. Locate the actual nested paths and record them. These raster assets are acceptable when no original vector version is supplied; do not invent a vector source, interpolate unseen data, or generate a new physics plot.

If included, the caption must identify each panel, configurations, virtuality/elastic assumptions, and the cumulative or differential meaning. Inspect any μ⁻ versus μ⁺ labels: do not alter the artwork silently. If a pure electromagnetic unpolarized charge-equivalence statement is used, state its limited scope; do not extend it to weak or polarization-sensitive observables without support. Keep intrinsic source-label issues in the companion note and necessary interpretation in the caption.

Retain the optional figure only if both panels, axes, and caption are readable. Otherwise remove it before compressing the required displays and summarize the supported photon physics in prose. Identify workshop additions as later supplementary developments. Do not imply that absent detailed workshop manuscripts have been read.

## 14. BSM outlook, conclusions, and acknowledgments

Use a short, mechanism-led discussion of source-supported μq and μg portals, such as R-parity-violating squarks and color-octet muons. Keep the FCC-based outlook proportionate and separate its beam configuration from LHμC assumptions.

Do not add a detailed BSM reach figure or long current-limit comparison simply because it exists in the source. If a precise reach is retained, preserve its couplings, compositeness scale, luminosity, selection, background treatment, and discovery/exclusion definition. Do not compare the leptogluon source's pp luminosity alternatives as though they were reconciled. The primary plan can state the production mechanism without numerical reach claims.

Conclude with a few supported messages: the energy/rate basis for HET studies; the dedicated versus combined nature of Higgs projections; complementary EW/top and photon opportunities; and the exploratory status and next studies where relevant. Introduce no new results in the conclusion and avoid repeating every number already displayed.

Include acknowledgments only when current, applicable wording is supplied or reliably established. Do not copy obsolete DIS2024 funding or invent a grant, endorsement, or collaboration approval. Omit an unsupported acknowledgment and record any genuinely necessary outstanding detail separately.

## 15. Scientific prose, notation, and captions

Use restrained, precise English and connected paragraphs. Explain the physical meaning of an equation or plot before drawing a conclusion from it. Define abbreviations at first use and keep LHμC, LHeC, μp, HL-LHC, CC/NC, and EPA notation consistent. Define the beam-charge convention once and maintain it where the source supports a specific charge.

Use consistent symbols for Higgs couplings, widths, statistical uncertainties, integrated luminosity, centre-of-mass energy, and invariant mass. Preserve the distinction between σ and σ×BR, parton-level and reconstructed quantities, and inclusive and selected rates. State confidence conventions when needed. Do not create a new convention that changes a frozen result.

Each figure and table must be introduced, cited, and interpreted in the text. Captions must identify the observable, configurations, essential cuts/assumptions, and source attribution, while remaining concise enough for the page budget. Avoid copying editorial comments or unused multipanel directions. Do not transfer qualifying assumptions exclusively to an external note when they are necessary to understand the printed result.

Remove TODOs, contributor names in square brackets, draft-color markup, unverified superlatives, stale references to other sections, and unsupported “exact,” “model-independent,” or “systematics-free” descriptions. Do not reproduce source errors in prose merely because numerical values are frozen. Conversely, do not repair a scientific disagreement by changing a number without authorization.

## 16. Page allocation, display priorities, and compression

Start with this checked allocation:

| Component | Total pages | Approximate body-word guide |
| --- | ---: | --- |
| Front matter, abstract, and conference block | 1.00 | Abstract initially 140–180 words |
| Collider setup, benchmarks, and HET rate overview | 1.65 | 180–240 words plus both tables and Figure 1 |
| Higgs production and precision prospects | 1.40 | 350–450 words plus the vector panel |
| Electroweak and top physics | 0.60 | 230–280 words |
| Photon-induced physics | 0.90 | 170–240 words if the optional display remains |
| BSM outlook, conclusions, and any acknowledgments | 0.45 | 170–210 words |
| References | 1.00 | Initially about 12–16 selective entries |
| **Total** | **7.00** | **All material counted** |

These are allocations, not forced page breaks or proof of fit. Word guides are secondary to the compiled layout. Count all headings, equations, captions, float spacing, and front/back matter. Redistribute space between sections if needed while preserving the scientific priorities and seven-page ceiling.

The display plan is:

| Display | Status | Planning footprint including caption/spacing |
| --- | --- | ---: |
| Complete HELP4CERN rate Table 1 | Required | About 0.40 page |
| LHμC energy/luminosity benchmark table | Required | About 0.25 page |
| `dis_eta_acceptance.pdf` | Required | About 0.55 page |
| HELP4CERN `LHmuC_vector.pdf` | Retain in the primary plan | About 0.45 page |
| Photon luminosity + τ-pair panels | Optional if legible | About 0.50 page |

Resolve excess length in this order: remove the optional photon figure; shorten BSM/FCC and general background; remove repeated motivation and long channel lists; reduce nonessential method/software detail; remove secondary citations only with the associated dispensable content. Preserve the full rate table, benchmark distinctions, first figure, central Higgs interpretation, readable vector legend, and essential references.

Use normal typographic and float-placement choices. Do not shrink official margins, lower the required main font, distort assets, hide content, or use excessive negative spacing. Do not omit required information to meet an estimated footprint. Seven pages is a maximum, not a target to pad.

## 17. Template and conference metadata

Begin with a separate copy of the supplied DIS2024 LaTeX project. The reviewed template uses an A4, 11-point `article` with `pos.sty` and a separate title/abstract page. Inspect its actual structure rather than recreating a different visual style from memory.

Verify current official DIS2026 author instructions and metadata before claiming compliance. Use these starting points:

- [DIS2026 proceedings instructions](https://dis2026.infn.it/workshop-proceedings/)
- [DIS2026 HET contribution](https://agenda.infn.it/event/47074/contributions/289107/)
- [Supporting muon workshop](https://indico.cern.ch/event/1681458/)

Confirm the full conference title, date range, location, and any contribution metadata used. Update the old conference block, obsolete contribution identifiers, coauthors, affiliations, and unrelated acknowledgment content. Do not copy the HELP4CERN placeholder arXiv identifier `1234.56789` into the article or bibliography.

Retain appropriate PoS conventions for title, author, speaker, affiliation, email, abstract, running header, captions, and references. Update the style only when an official requirement justifies it, and document the change. Do not declare the supplied old style current without checking. If official formatting information is unavailable, continue with the supplied template and identify that specific compliance limitation.

The author has fixed the seven-page working ceiling. Do not change it merely because a different generic page limit is discovered. Record any verified conflict for author review while preparing the requested seven-page draft. A historical deadline reminder does not establish a current cutoff time or authorize submission.

## 18. Bibliography and scientific attribution

Build a selective bibliography for claims actually retained. Start from the source bibliographies and verify essential metadata through primary records where possible: publisher records, arXiv, official conference contributions, and original project documentation. Use web verification for current publication information rather than guessing.

Include consistent DOI and arXiv hyperlinks when real identifiers exist. Do not invent an identifier, journal assignment, collaboration author list, or publication status. An unpublished HELP4CERN result should be attributed as a supplied study-group working draft if no public identifier is verified. Its private source status does not make a software paper the primary source of the prediction.

Prioritize the machine proposal, LHeC baseline, actual HELP4CERN/talk results, relevant Higgs methodology, the selected coupling-fit framework and baseline, and essential photon antecedents. Keep generator citations proportionate to the described analysis. Use approximately 12–16 references as a planning guide, not a reason to omit necessary attribution or pad the bibliography.

A useful methodological distinction is that the Cheung–Wang collider study supports aspects of the method/external input; its different μ⁻ benchmark configurations do not by themselves validate the HELP4CERN μ⁺ rates. Likewise, a SMEFiT framework paper supports the method but is not automatic independent validation of unpublished LHμC bars.

Resolve citation-key spelling and case consistently, including any `atlas:2025eii`/`ATLAS:2025eii` mismatch. Do not retain uncited, duplicate, or irrelevant bibliography entries. Keep an in-preparation photon manuscript distinct from a published proceedings contribution even if titles resemble one another. Never assign a published paper's DOI to a different unpublished work.

Use the bibliography mechanism that fits the supplied template—manual entries or a complete `.bib` workflow—and ensure every citation resolves. If metadata verification is unavailable, retain only supported details and state the limitation in the companion note; do not fabricate a complete reference.

## 19. LaTeX project and asset handling

Use `DIS2026_HET_Proceedings.tex` as the main entry point. Produce a self-contained project with relative paths, all selected assets, necessary style files, bibliography inputs if used, and a concise README specifying the actual build command and dependencies.

Preserve the original vector PDFs for the required first figure and Higgs vector panel. Use descriptive names or archive-specific subdirectories if needed to prevent collisions; record any rename in the asset map. Ordinary uniform scaling and a page crop that removes only empty margins are permitted when they preserve all physical content. Do not clip axes, legends, notes, or uncertainties.

Do not redraw scientific graphics, create new event samples, run new simulations or fits, generate substitute imagery, or invent data. An EPS-to-PDF conversion of an actually retained source asset is a technical conversion only; inspect it for faithful rendering. The selected plan should not need additional scientific figure production.

Use automatic figure/table/equation numbering and labels. Keep the rate table as Table 1 and the kinematic coverage as Figure 1 where feasible. If the final float order changes, cross-references and the companion mapping must still identify the correct source assets.

Remove obsolete source sections and unrelated dependencies from the delivery project. Do not package complete input archives, duplicate same-named graphics from other packages, temporary previews, or stale PDFs as if they were final assets. Do not include absolute workspace paths, account identifiers, or dependence on conversation-only content.

The earlier template diagnostic encountered a missing `newtxtext.sty`. Check the actual environment rather than assuming the problem persists. Attempt a routine permitted dependency remedy; do not replace the official font or alter page geometry merely to bypass a missing package. Record the engine and dependencies actually used.

## 20. Ordered writing, build, and validation workflow

Execute these stages without pausing for approval of already settled choices:

1. **Access and decisions:** verify inputs, preserve archives, identify active source versions and mandatory assets, and note any genuine limitation.
2. **Claim and asset mapping:** build a compact working map with an identifier, intended statement, source archive/path/location, benchmark/exposure, qualifier, and final section/display. Give the required rate table, benchmark table, kinematic figure, h→bb̄ results, and vector fit explicit entries.
3. **Outline and layout:** fix the five-block narrative and display order using the page plan. Keep assumptions close to the results they qualify.
4. **Manuscript writing:** write the complete body, captions, conclusions, and selective bibliography; finish the abstract and front matter after the main content stabilizes. Do not leave placeholders in settled fields.
5. **Source assembly:** implement the template, macros, assets, references, and build instructions using relative paths.
6. **Compilation:** run the appropriate build passes until citations and cross-references stabilize. Resolve ordinary LaTeX failures and missing includes. Inspect warnings for content loss, overflow, undefined references, duplicate labels, missing glyphs, and missing assets.
7. **Layout review:** count actual PDF pages and render/view every page. Check title-page balance, table width, figure labels, caption readability, equations, references, whitespace, and clipping. Check final print-scale legibility, not only a zoomed source image.
8. **Targeted revision:** fix concrete content/layout problems, apply the ranked compression plan if over seven pages, and rebuild. Do not change frozen numerical results during layout repair.
9. **Final fidelity check:** compare the table cells and selected numerical statements to HELP4CERN; confirm original asset versions, units, qualifiers, combined-fit labels, and exposure distinctions. A successful transcription check does not resolve the deferred scientific issues.
10. **Package verification:** build the final delivery project from a clean copy of the packaged contents with the documented dependencies. Ensure the delivered PDF corresponds to that source and that no external local files are needed.
11. **Handoff:** deliver the named files and a factual status statement, including actual page count, completed checks, source policy, and genuine limitations.

Stop optional checking when the concrete acceptance conditions are satisfied. Do not spend the run generating new analyses or trying to resolve discrepancies the author has deferred. If tools cannot compile or visually inspect the manuscript, provide the complete source work and report exactly which checks were not performed. Never fabricate a PDF, page count, successful build, or visual review.

## 21. Companion validation and deferred-corrections note

Create `DIS2026_HET_Validation_and_Deferred_Corrections.md` as a separate, concise record containing:

- Actual input access and relevant review coverage; identify the source versions used without exposing temporary private paths.
- The main source/asset map, including the two tables, both retained vector graphics, and any optional photon panels.
- Build engine/command, compile status, actual PDF page count, visual-check status, and any remaining technical limitation.
- Confirmation that selected HELP4CERN numbers were transcribed unchanged, together with the specific checks actually performed.
- The three deferred numerical issues from Section 5 and their unchanged status. Do not describe them as solved merely because the article compiled.
- Any additional consequential issue encountered, such as a retained plot-label ambiguity, unresolved optional comparison, unavailable official metadata, or uncertain bibliographic detail, with its actual treatment.
- Material editorial decisions, including omission of the optional photon figure if needed and any justified template update.

Keep the record proportionate. Do not reproduce the entire historical source review. Separate a scientific issue deferred by author instruction from an access problem or a technical build failure. Do not insert this note, its audit tables, or workflow commentary into the seven-page article.

## 22. Deliverables, acceptance checks, and final response

Deliver these four named artifacts:

| File | Required contents |
| --- | --- |
| `DIS2026_HET_Proceedings.tex` | Complete main LaTeX manuscript with the fixed identity and source-faithful scientific content. |
| `DIS2026_HET_Proceedings.pdf` | Actual compiled, visually checked proceedings PDF, at most seven pages, when compilation succeeds. |
| `DIS2026_HET_Proceedings_Source.zip` | Self-contained build project with the main source, required assets/styles, bibliography content, README, and the companion note. |
| `DIS2026_HET_Validation_and_Deferred_Corrections.md` | Separate validation, provenance, and deferred-correction record, also available directly for author review. |

Before claiming completion, verify the following against the actual outputs:

- [ ] Exact title, sole named author, study-group attribution, affiliation, email, and appropriate speaker designation.
- [ ] HELP4CERN numerical policy applied; the three deferred issues remain documented and have not blocked drafting or been falsely declared resolved.
- [ ] Complete Table 1 with all values, columns, unpolarized entries, source polarization statements, and blank 2 TeV top cells.
- [ ] Separate LHμC benchmark table with beam energies, centre-of-mass energies, integrated luminosities, and general-versus-study-specific exposure distinctions.
- [ ] Correct first figure, `dis_eta_acceptance.pdf`, with unchanged physical labels, acceptance information, and readable axes/legend.
- [ ] Source h→bb̄ rate/coupling precisions and external input preserved, with honest statistical and exposure interpretation.
- [ ] HELP4CERN `LHmuC_vector.pdf` retained, with actual combined-fit labels, exploratory assumptions, κ_V constraint, and 68% uncertainty definition.
- [ ] Connected HET narrative and proportionate photon/BSM content; no unsupported new quantitative claims or new scientific calculations.
- [ ] Correct attribution and supported reference identifiers; no placeholder arXiv number, obsolete DIS2024 conference block, or invented acknowledgment.
- [ ] All citations, cross-references, graphics, and required files resolve; no content lost through overflow, clipping, unreadable scaling, or missing glyphs.
- [ ] Actual PDF page count is no more than seven, including front matter and references, and every page has been visually inspected when tools permit.
- [ ] Final source package builds from its own contents using the documented dependencies; delivered source and PDF correspond.
- [ ] Companion note is separate from the proceedings; no submission, communication, or approval claim has been made.

Report check status honestly. If a genuine missing input or environment limitation prevents an item from being satisfied, deliver all completed work and identify the unmet item precisely. Do not quietly drop a required display or call an overlength/uncompiled output verified.

In the final response, link the actual artifacts, state the measured PDF page count and compilation/visual-review status, and note briefly that HELP4CERN numerical corrections remain deferred as instructed. Keep the response focused on the delivered result rather than a lengthy work log. Do not claim publication or submission readiness beyond the checks actually completed.

**END ACTIVE MANUSCRIPT EXECUTION PROMPT**
