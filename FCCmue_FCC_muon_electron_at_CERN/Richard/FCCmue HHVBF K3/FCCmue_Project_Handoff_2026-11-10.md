# FCC-μ⁺e⁻ Higgs Physics — Complete Project Handoff

**Continuity reference for a new ChatGPT chat within the same project**  
**Prepared:** 10 November 2026 (following the first discussion with Richard Ruiz)  
**People:** Hamzeh Khanpour (presenter / researcher, AGH University of Krakow); Krzysztof Piotrzkowski; Richard Ruiz; Piotr Kotko.  
**Status:** Existing SM LO baselines done; new κ₃–polarization–HH→4b differential study **not yet executed**.

> **HOW TO USE:** Open a **new chat inside the same ChatGPT project**, attach this document and preferably `FCCmue_Continuity_Source_Bundle_2026-11-10.zip`. Ask the new chat to read these first, inspect actual source archives, and **continue** from the status below. Do **not** assume every raw event or unshared CERN run is present in the ChatGPT context.
>
> **Source hierarchy:** original MadGraph process/run cards, numerical CSVs and logs > QA reports > generated presentations/handouts > these notes/chat recaps. Treat all historical numbers as preliminary if their source-specific validation was not completed. No BSM κ₃ scan and no HHH simulation has been performed yet.

---

## A. Primary scientific aim

Investigate Higgs physics at an asymmetric, polarized high-energy positive-muon–electron collider (FCC-μe), emphasizing electroweak vector-boson fusion, single-H and double-H production, the Higgs trilinear self-coupling λ₃, HHVV gauge–Higgs contact couplings, four-b final states, interference, realistic backgrounds, differential angular observables, and FCC-ee complementarity. Eventually consider HHH/quartic λ₄ feasibility. Richard's 10 November 2026 instructions define the **current next calculation**.

## B. Collider benchmarks — **never mix these**

For ultrarelativistic head-on beams, `sqrt(s) ≃ 2 sqrt(E_e E_mu)` and `y_CM ≃ 0.5 ln(E_mu/E_e)` with the +z convention specified.

| Benchmark | E(μ⁺) | E(e⁻) | sqrt(s) | Application |
|---|---:|---:|---:|---|
| FCC-μe design-like low | 2000 GeV | 120 GeV | 979.795897 GeV | earlier 4b studies |
| FCC-μe design-like high | 5000 GeV | 183 GeV | 1913.112647 GeV | earlier 4b studies |
| exact E1 | 2000 GeV | 125 GeV | 1000.000 GeV | 48-run inclusive H/HH polscan |
| exact E2 | 5000 GeV | 200 GeV | 2000.000 GeV | 48-run inclusive H/HH polscan |
| muon collider | symmetric μ⁺μ⁻ beams | — | 1 or 2 TeV | historical 4b / ZH comparison |

**Collider proposal:** Krzysztof Piotrzkowski, *FCC-μe: High Energy, High Luminosity Muon–Electron Collider & Neutrino Factory at CERN*, INSPIRE `3220545`, arXiv `2610.40451`. Previously audited revised **v2** (5 November 2026). The v2 low-energy peak-luminosity figure cited in the slide handout is `0.63×10^34 cm^-2 s^-1`; check the actual paper/table if quoting machine values. Avoid older v1 luminosity claims. FCC-ee around 240 and 365 GeV provides complementary precision Higgsstrahlung/ewk measurements.

## C. Completed inclusive Standard Model MadGraph polarization scan — **48 successful jobs**

MG5_aMC v3.6.4, tree-level SM, unrestricted complete matrix elements, stable Higgs, **no imposed generation cuts**. e⁻ beam 1 (`polbeam1=0`); μ⁺ beam 2 (`polbeam2=0,20,40,60,80,100`), +80 meaning right-helicity antimuon (80% longitudinal polarization). 4 processes × 2 exact energies × 6 muon polarizations = **48 jobs**, requested **30,000 events each**, all result archives collected with no failures. Numerical status `COMPLETED_UNVALIDATED`: independent-seed, regulator/forward-region and higher-order theory checks still outstanding. MC integration errors ≠ theory or experimental errors.

```
import model sm
generate e- mu+ > ve vm~ h QCD=0       # CC H

generate e- mu+ > ve vm~ h h QCD=0     # CC HH

generate e- mu+ > e- mu+ h QCD=0      # NC H

generate e- mu+ > e- mu+ h h QCD=0    # NC HH
```

**Data source:** `FCCmue_results_audit/cross_sections_48.csv` / `FCCmue_Higgs_PolScan_full_exact_REVIEW.zip` within source bundle. The file has `process_id,energy_id,sqrts_GeV,polarization_percent,sigma_fb,sigma_mc_err_fb,... seed,n_events,status` and **all 48 exact values and errors**. Do not transcribe them from a screenshot.

**Selected results (fb):**

| Process | sqrt(s) | P=0% | P=80% | P=100% |
|---|---|---:|---:|---:|
| CC H | 1 TeV | 210.540 | 378.570 | 421.150 |
| CC HH | 1 TeV | 0.0743838 | 0.1332298 | 0.1482390 |
| NC H | 1 TeV | 20.835 | 24.476 | 25.402 |
| NC HH | 1 TeV | 0.00962012 | 0.01130777 | 0.01172286 |
| CC H | 2 TeV | 386.010 | 695.000 | 772.690 |
| CC HH | 2 TeV | 0.418510 | 0.754495 | 0.839521 |
| NC H | 2 TeV | 38.991 | 45.829 | 47.642 |
| NC HH | 2 TeV | 0.0547116 | 0.0642989 | 0.0667703 |

**Weighted fits** `sigma(p)=a(1+A p)` with `p=P_mu+/100`: CC H A=0.9982±0.0020 (1 TeV), 1.0007±0.0018 (2 TeV); CC HH 0.9934±0.0040, 1.0053±0.0039; NC H 0.2181±0.0012, 0.2208±0.0011; NC HH 0.2186±0.0022, 0.2204±0.0022. Physically CC scales approximately `1+p` and NC is a weaker approximately `1+0.22p` at this SM benchmark. CC total rate ~1.8x at +80%; NC ~1.175x. Double-H rises 1→2 TeV ~5.6x, single-H ~1.8–1.9x. Do NOT infer coupling sensitivity from these SM cross sections alone.

### CERN computing work and known execution history

- On Windows PowerShell original package sent with `scp` to `hakhanpo@lxplus.cern.ch` under `/eos/user/h/hakhanpo/MG5_aMC_v3_6_4/`.
- v1 package `FCCmue_Higgs_PolScan_v1_CERN_AUDITED.zip` failed at `scan.py prepare` because it wrongly required an optional MG5 run-card field `ptl`.
- Fixed v1.1 `FCCmue_Higgs_PolScan_v1_1_CERN_PTL_FIX.zip`; all 4 process templates successfully prepared: `templates/CC_H.tar.gz`, `CC_HH.tar.gz`, `NC_H.tar.gz`, `NC_HH.tar.gz`.
- Initial HTCondor pilot cluster `13247189` was held with IWD error: Condor could not access `/eos/home-h/hakhanpo/...` initial working directory. Removed cluster.
- **Working fix:** copy submission package to **AFS**, not EOS IWD. Path `/afs/cern.ch/user/h/hakhanpo/FCCmue_Higgs_PolScan_v1_1_CERN_PTL_FIX_AFS` (shell `$HOME/FCCmue_Higgs_PolScan_v1_1_CERN_PTL_FIX_AFS`). Use AFS for the Condor submit directory and input staging; EOS may hold long-term data when paths are correct. Pilot cluster `13247192`: all 8 pilot jobs completed. Full production clusters `13247196` and `13247197`: 48 successful job archives, 0 failed/corrupt; numerical status initially `COMPLETED_UNVALIDATED`.
- Review ZIP from CERN: `FCCmue_Higgs_PolScan_full_exact_REVIEW.zip`. This selected archive **does not include all complete LHE four-momenta** needed for Richard's new angular analysis. Check CERN original working/output archives before assuming they still exist.
- Files for re-use: `FCCmue_Higgs_PolScan_v1_1_CERN_PTL_FIX.zip`, `FCCmue_Higgs_PolScan_full_exact_REVIEW.zip`, `FCCmue_Higgs_Polarization_Figures_v2_Source_Data.zip`, `FCCmue_Higgs_Polarization_Scientific_Results_Package.zip`.

## D. Original MadGraph diagrams — Krzysztof's verification

Actual CERN MG5 exports of four processes are in `FCCmue_Original_MadGraph_Diagrams_Verified_All4.zip` (and annotated sources); original vector `matrix.pdf` files:
- `CC_H`: 1 fusion diagram (HWW).
- `NC_H`: 1 fusion diagram (HZZ).
- `CC_HH`: 4 diagrams; #1 HHWW contact, #2/#3 two separate Higgs-emission topologies through HWW vertices, #4 `VV→H*→HH` with λ₃.
- `NC_HH`: 4 diagrams; #1 HHZZ contact, #2/#3 separate emissions through HZZ vertices, #4 off-shell H*→HH with λ₃.

All these are included in unrestricted SM **full tree-level coherent amplitudes** with interference. Individual arbitrary diagram subsets are not necessarily gauge invariant; no separate diagram-specific cross sections and no κ₃ coupling scan have yet been computed. Krzysztof explicitly asked whether the self-coupling and separate emission diagrams were present, and this has been confirmed via genuine MG5 exports.

## E. Older resonant / complete 4b studies (distinct from inclusive stable-Higgs scan)

Earlier CC resonant `e- mu+ → ve vm~ HH → ve vm~ 4b` and complete `ve vm~ 4b`; symmetric muon-collider neutrino-flavour variants. Parton level. Four b-partons `|eta_b|<5`, two distinct opposite-charge b bbar pairs each `110<m_bb<130 GeV`; **no b-parton minimum pT**. Some older output entries originated from different source packages; preserve per-row provenance.

| Collider and energy | resonant HH→4b P0 / P80 [fb] | complete νν4b P0 / P80 [fb] |
|---|---|---|
| FCC-μe 0.9798 TeV | 0.04912 / 0.08816 | 0.05355 / 0.09195 |
| μ⁺μ⁻ 1 TeV | 0.07047 / 0.11582 | 0.07530 / 0.12472 |
| FCC-μe 1.9131 TeV | 0.26478 / 0.47611 | 0.28157 / 0.50745 |
| μ⁺μ⁻ 2 TeV | 0.30624 / 0.54606 | 0.32480 / 0.57873 |

**Crucial old-decay normalization:** original resonant HH→4b model card had `BR(H→bb)=0.844640` (not usual SM ~0.58). Do not equate these fiducial 4b rates to conventional SM branching assumptions. Complete interfering 4b amplitude is **not** an independent additive background, and cannot generally be corrected by a global `BR²` factor.

Older unpolarized NC `e- mu+ → e- mu+ (HH, bbH, full 4b, Higgs-excluded 4b)` at 0.9798 TeV, with outgoing charged-lepton `pT>1 GeV` at *generation* level plus 110–130 bb windows:
- NC HH→4b: `0.006382 fb`;
- NC associated bbH→4b: `0.012925 fb`;
- NC complete 4b: `0.007713 fb`;
- NC Higgs-excluded continuum: `0.0008253 fb` with only **88/50,000** events passing (poor statistics).
**Open inconsistency:** complete NC-4b `0.007713 fb` below separately generated associated bbH `0.012925 fb`; cannot claim "interference solved it" without new process/cut normalization audit.

At +80% higher-energy associated bbH: FCC-μe 1.913 TeV `~0.081843 fb`, μ⁺μ⁻ 2 TeV `~0.094913 fb` (source/cuts/statistics must be checked).

Muon collider resonant **ZH→4b** (`μ⁺μ⁻→ZH→bb bb`), P0, windows **80–130 GeV** rather than 110–130: 1 TeV `1.56450 fb` before / `1.52716 fb` after; 2 TeV `0.37888 fb` before / `0.36929 fb` after. `|eta_b|<5`, no minimum b pT. Distinct final-state topology from neutrino-associated HH.

## F. Existing slides, report and code (source artifacts)

Completed:
- `FCCmue_Higgs_Physics_Kickoff_2026_COMPLETE.zip`: 40 main + 8 backup AGH Beamer slides, `.tex`, compiled 48-page `.pdf`, CERN figures, vector diagrams, source and QA.
- `FCCmue_Higgs_Physics_Research_Handout_20pages_COMPLETE.zip`: 20-page A4 physics note, `.tex`, compiled `.pdf`, figures, theory and references.
- `FCCmue_Higgs_Polarization_Figures_v2_Source_Data.zip`: full 48-row cross sections, publication-style plots and Python.
- `FCCmue_Original_MadGraph_Diagrams_Verified_All4.zip`: actual vector diagrams.
These are reference/working artifacts, **not evidence** of calculations beyond data they cite.

## G. NEW — Richard Ruiz's 10 Nov 2026 email and whiteboard (current top priority)

Richard's original email (technical wording retained):

> 0. For the process e-mu+ > hh vv/emu, group together the WW/ZZ fusion channels, so that you model one giant process (incl. all interfering diagrams): `generate e- mu+ > h h xx xx`
>
> 1. For fixed beam configuration (energies, etc.), the cross section depends on (a) beam polarization and (b) Higgs self-coupling. Plot (a) xsec vs muon polarization, (b) xsec vs self coupling, (c) xsec vs (polarization,self-coupling) (SM benchmark).
>
> 2. Generate events with h1→bbx, h2→bbx, initially 100% reconstruction and tagging/ID. Label pb1,pb2 from h1 and pb3,pb4 from h2. Build P4b(lab), take P4bHat. Boost P4b and all pbk to the 4b-rest frame. Define `q12 = pb1(hard)×pb2(hard)/(|pb1||pb2|)` and similarly `q34`. Request `cosPhi=q12·q34`, `cosTheta=q12·P4bHat`, and plot differential cross sections vs both under SM/BSM hypotheses at ~4–6 polarizations.

Photos of Richard's whiteboard are packaged as `Richard_meeting_2026-11-10/photo_*.png` and illustrate these instructions, a Higgs-pair ±10 GeV per-pair mass window, candidate extra-activity vetoes, WW/ZZ/ZZX backgrounds, and lab/hard-frame definitions. Handwritten curves are **sketches, not simulation results**.

### Interpretations and corrections that **must carry over**

1. **CC versus NC do NOT interfere:** `e- mu+ > ve vm~ h h` and `e- mu+ > e- mu+ h h` have different external particles; include as one multiprocess production configuration if desired (using explicit `generate ... @1`, `add process ... @2` syntax) but add incoherently. Within each identical external final state, complete MG5 amplitudes DO include interference among the four diagrams. `xx` in Richard's email is a placeholder, not a predefined MG5 particle alias; don't literally run `generate ... xx xx` without declaring a valid multiparticle set and verifying allowed particle content.
2. **Next physics target is κ₃, not new SM-only rates:** define `κ₃=λ₃/λ₃^SM`, scan with a vetted UFO parameterization (HEFT vs SMEFT), verify κ₃=1 reproduces original SM, avoid gauge-inconsistent arbitrary changes. At fixed other couplings and LO: `M=M0+κ₃ M1`; `σ(κ₃)=c0+c1κ₃+c2κ₃²`. CC should scale approximately `σ_CC(p,κ₃)=(1+p) σ_CC(0,κ₃)`. For NC, use helicity mixture `σ_NC(p,κ₃)=[(1+p)σ_+(κ₃)+(1-p)σ_-(κ₃)]/2`, with electron unpolarized and p fractional. Check numerically before using extrapolation. Choose pilot κ₃ points `-2,0,1,2,5` and representative polarizations; scan 1 and 2 TeV.
3. **Angular quantities from Richard's email are NOT literally cosines:** raw `q12` and `q34` have magnitudes sin(opening angle). `q12·q34=sinα12 sinα34 cosΦ_plane`. To measure proper plane-angle cosines, normalize normals `n12=(p1×p2)/|p1×p2|`, similarly `n34`; `cosΦ_plane=n12·n34`. Compute BOTH the raw requested variable and unit-normal version. In the 4b rest frame, retain a clearly defined boost direction from lab; `cosΘ_plane=n12·betaHat_4b` with declared boost/sign convention. Beam/helicity production angles can be additional observables.
4. **Scalar Higgs decays:** on-shell spin-zero H→bb isotropic in H rest; plane-angle distributions may be insensitive to κ₃ under ideal acceptance, so benchmark against mHH, pT_H, yHH, cosθ_H* and investigate selection-induced structure. For uniform independent plane azimuths, `dN/dcosΦ∝1/sqrt(1-cos²Φ)` (not flat in cosine). Near HH threshold crossed-momentum vectors can vanish, making normals numerically undefined; handle degenerate events with explicit epsilon and counters.
5. **Truth vs reconstruction:** for stage 1 use explicit two H→bb decay chains, mother/daughter assignments, 100% *reconstruction/tagging only*, **not** 100% physical H→bb branching. Reconstruct `P4b(lab)` from all four decay bottom four-vectors; boost all consistently into P4b rest frame; check `P4b^rest=(m4b,0,0,0)`. Separate truth pairing from three possible observable 4b pairings. b/anti-b labels and interchange H1/H2 can flip signs of plane normals; test charge-agnostic `|cosΦ|`, `|cosΘ|`. Fixed mass window candidate `|m_bb−m_H|<10 GeV` for each pair; check resolution assumptions.
6. **S/B vs signal rate:** muon polarization can enhance both CC HH signal and CC backgrounds; evaluate `S/B`, `S/sqrt(B)` or proper likelihood only after consistent cuts, decays, luminosity and uncertainty model. Backgrounds likely include `ZZX→4bX`, `bbH+X`, continuum `4b+X`, with matching recoil states and possible interference. Historic NC 4b inconsistency MUST be resolved first. Any veto on extra central activity needs a precise detector- or parton-level definition and radiation caveats.
7. **Next campaign output:** plots σ vs P at fixed κ₃, σ vs κ₃ at fixed P, σ heat maps P×κ₃; differential `dσ/dcosΦ`/`dσ/dcosΘ` (raw + normalized versions, with bin uncertainties) at SM/BSM points; `mHH` and other benchmark distributions; source cards, LHE, CSVs, plotting code, validation, zipped CERN run package and note; compare CC vs NC, 1 vs 2 TeV; identify interference correctly.
8. **Do NOT treat HHH as done:** triple Higgs and κ₄ are only proposed future feasibility. Possible commands `generate e- mu+ > ve vm~ h h h QCD=0` and `generate e- mu+ > e- mu+ h h h QCD=0`, but NO HHH cross sections or event samples were generated in this work.

### Concrete first-step experimental plan (not yet launched)

- Reuse the successful AFS-based HTCondor workflow as infrastructure, but **new versioned package** with κ₃-enabled UFO, configuration validation, and robust run manifests. First check existing CERN LHE availability.
- First reproducibility pilot: κ₃=1 unpolarized at exact E1/E2 for CC/NC, compare original 48-run data within integration errors; verify widths, EW inputs, beams, cuts and Higgs decays.
- Then pilot `κ₃=[-2,0,1,2,5]` (including SM=1), with `P_mu+` at a few independent values and both energies, watching numerical convergence (small HH cross sections).
- Derive cross-section polynomial coefficients with independent numerical checks and predict/check polarization scaling. Use full range when desired (example signed P values `[-80,-40,0,+40,+80,+100]`; Richard proposed 4–6 points and did not lock exact values).
- Build an independently unit-tested Lorentz-vector/mother-matching/event-analysis script (LHE parsing, 4b rest frame, normalized angular variables, bin weights, guard degenerate plane normals). Compare analytical isotropic scalar-decay expectation without cuts.
- Extend to backgrounds and systematic cut-flow after signal's clean baseline is verified. Keep 20-page handout and kickoff slides as reference, not immutable findings; update with new data only when actually obtained.

## H. Suggested first message in new chat

> **Continue the FCC-μ⁺e⁻ Higgs Physics CERN project from the attached handoff and source bundle.** These documents summarize our completed 48-run inclusive H/HH polarization scan, historical FCC-μe and muon-collider 4b results, original MadGraph diagrams, CERN LXPLUS/AFS/HTCondor workflow, research handout and slides, and Richard Ruiz's **10 November 2026** new calculations. Please read `FCCmue_Project_Handoff_2026-11-10.md` in full and inspect primary ZIP/CSV/diagram files before making numerical claims. **Do not restart earlier SM calculations; do not assume κ₃ scans, angular 4b events or HHH were completed.** Our next task is to design and implement a scientifically audited CERN package for coupled κ₃/polarization scans and `HH→4b` differential angles in CC and NC channels at exact 1 and 2 TeV, including validation of Richard's proposed variables and interference/background conventions. First summarize the verified status, critical unresolved details and a reproducible incremental plan; then proceed with the specific implementation request I give.

## I. Key files to retain in this same project

1. **This handoff markdown** — compact authoritative contextual orientation.
2. `FCCmue_Continuity_Source_Bundle_2026-11-10.zip` — curated primary source bundle with complete numeric source and original diagram exports; includes Richard photos and written email plus finished academic artifacts.
3. Original CERN files still on LXPLUS / EOS / AFS; don't delete them. ChatGPT ZIPs are not a substitute for heavy original full LHE event archives.
4. Keep this original long conversation in the project. In a new chat inside the same project, project memory *may* draw from it, but uploading handoff and source files ensures exact constraints are explicitly available.

**END OF HANDOFF — scientific results up to 10 November 2026; new Richard κ₃ and four-bottom angular campaign is next, not done.**
