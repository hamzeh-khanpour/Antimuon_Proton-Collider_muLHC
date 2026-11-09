# FCC-ue / muon-collider HH -> 4b comparison — consolidated final setup v3.0.0

**Prepared: 23 October 2026. Supersedes both earlier starter/revised packages.**

> **NO MADGRAPH PHYSICS RUNS HAVE BEEN EXECUTED HERE. NO NUMERICAL COLLIDER CROSS
> SECTIONS ARE INCLUDED.** This is a consolidated, locally tested calculation setup,
> not a validated production result. Real MG5 process generation, adapter compatibility,
> integration and convergence remain to be checked on the target installation.

## 1. Task and confirmed configurations

Krzysztof requested **only four integrated cross sections after cuts**. His clarification
fixes mu+e- to **2000 GeV mu+ on 120 GeV electrons**, with **no minimum jet-pT cut**.

| Setting | mu+e- (FCC-ue) | mu+mu- (comparison) |
|---|---|---|
| Positive-z beam | mu+ at 2000 GeV | mu+ at 500 GeV |
| Negative-z beam | e- at 120 GeV | mu- at 500 GeV |
| sqrt(s), neglecting incoming lepton masses | **979.795897 GeV** | **1000 GeV** |
| COM boost rapidity in the lab | **+1.406705** | **0** |
| Polarization | Unpolarized (assumption) | Unpolarized (assumption) |
| Final bottom acceptance | All four abs(eta_lab) < 5 | All four abs(eta_lab) < 5 |
| Minimum bottom pT | **None** | **None** |
| Minimum DeltaR | None added | None added |
| Higgs-candidate windows | Both disjoint b-bbar masses in **[110,130] GeV** | Same |
| Missing-neutrino species | nu_e anti-nu_mu | Sum over e, mu, tau same-flavor pairs |

**The mu+mu- 500+500 GeV split is the symmetric interpretation of the original 1 TeV
request, not a separately confirmed statement in the clarification.** Lab-frame cuts,
unpolarized beams, the two-candidate pairing prescription, and the neutrino-flavor sum
are explicit calculation conventions. They are not additional quoted instructions.

The full table with confirmation status is in `docs/CONFIRMED_COLLIDER_CONFIGURATIONS.md`.
The machine-readable source of settings is `configuration.json`.

## 2. Four requested outputs; eight internal flavor components

| Output label | Process definition | Internal components |
|---|---|---|
| mue_HH | mu+ e- -> nu_e anti-nu_mu HH, followed by HH -> 4b | 1 |
| mue_4b | mu+ e- -> nu_e anti-nu_mu b bbar b bbar | 1 |
| mumu_HH | mu+ mu- -> sum_i nu_i anti-nu_i HH, followed by HH -> 4b | 3 |
| mumu_4b | mu+ mu- -> sum_i nu_i anti-nu_i b bbar b bbar | 3 |

Each flavor is integrated separately so its normalization, statistics and uncertainty
can be audited. The three orthogonal neutrino final states are summed as cross sections,
not amplitudes. Missing components are never silently treated as zero.

The stable-HH production cards use `QCD=0 QED=4`. The direct-4b cards use
`QCD=2 QED=6`. In MG5 single `=` supplies amplitude-order **upper bounds**, not exact
orders (`==`). These explicit bounds retain the tree electroweak and QCD-mediated
contributions for this SM final state, rather than relying on MG5's automatic leading
coupling-order preference. No Higgs exclusion, required internal Higgs, VBF-only
selection, or resonant subtraction is imposed on the direct-4b amplitude.

**The direct-4b rate is NOT a pure background.** It includes HH resonances, singly
resonant Higgs contributions, non-Higgs amplitudes and their allowed interference.
Do not add the separate NWA HH signal to it. Subtracting the NWA result is not a
unique gauge-invariant definition of a background-only cross section.

## 3. Exact acceptance and pairing algorithm

For two b partons b1,b2 and two antipartons a1,a2, the only two opposite-charge,
nonoverlapping assignments are:

    A = (b1,a1) + (b2,a2)
    B = (b1,a2) + (b2,a1)

The event passes if all four have `abs(eta_lab) < 5` AND either assignment has BOTH
masses in the closed interval [110,130] GeV. Each event counts once, even if both
assignments pass. A parton may not be reused in two candidates.

No “correct Higgs parent” is assigned to direct-4b events. This is an existence test
on measured parton four-vectors. The full matrix element need not admit a unique
Higgs-pair history. The rule does not require all four opposite-charge combinations,
or all six arbitrary pairs, to lie in the window.

At parton level, b versus bbar is known from PDG IDs +5 and -5. Detector b-tagging
alone is not charge identification: a charge-blind four-b-jet analysis would have
three unordered jet partitions and needs a separate selection definition. That is
not the observable implemented here.

A best-distance pairing diagnostic using sum((m-125)^2) is also reported, but **does
not define the primary acceptance**. It is not always equivalent to the existence
rule. No invented detector mass resolution is needed.

### Laboratory frame and generator cuts

Incoming LHE four-vectors are checked against the configured PDGs, invariant energy,
orientation and beam energies. Already-laboratory events are not boosted again. If
an otherwise consistent sample is stored in the COM frame, all four-vectors are
boosted to the specified laboratory. Massive bottom pseudorapidity is evaluated as
`asinh(pz/pT)`; it is not approximated by adding the COM rapidity to eta.

**All registered generation cuts are disabled using the installed MG5 run-card schema.**
This includes hidden cuts, missing-pT cuts, sorted jet cuts and PDG-specific cuts.
Eta and the two-pair mass window are applied only in the LHE analysis. In particular,
`mmbb=110, mmbbmax=130` is NOT a valid replacement for the disjoint-pair test.

This strategy is simple and auditable, but not guaranteed to be efficient for the
rare accepted region of an uncut 2->6 continuum. If selected statistics or integration
convergence are inadequate, the same exact pairing predicate should be ported into
an independently validated integration-level cut. This version does not pretend to
contain such a production-optimized integrator.

## 4. Higgs decays and an important normalization correction

HH production is generated with two stable on-shell scalars. Each H is decayed
isotropically into a massive b and bbar, conserving four-momentum. The NWA signal is

    sigma_fid(HH -> 4b) = sigma(nu nu HH) * B_card(H -> bbbar)^2 * A_4b.

The true on-shell decay pairs have mass mH=125 GeV, so the wide [110,130] window does
not itself remove ideal NWA signal events. The bottom-parton eta acceptance remains
nontrivial. This is not a finite-width/showered/detector signal simulation.

**Correction to the earlier packages:** their signal used B=0.582 independently of
the bottom Yukawa and Higgs total width in the direct-4b matrix element. That can
create inconsistent normalization between the two reported quantities.

The primary v3 signal instead derives its branching factor from the SAME actual
SM parameter card used for the direct process:

    Gamma_LO(H -> bbbar)
      = 3 GF ymb^2 mH / (4 pi sqrt(2)) * (1 - 4 mb^2/mH^2)^(3/2)
    B_card = Gamma_LO(H -> bbbar) / Gamma_H.

Here `ymb` is the SM UFO's Yukawa mass input; `mb` is the kinematic bottom mass.
They are conceptually distinct. All masses, Yukawas and widths are recorded.

For illustration, the published default SM restriction card checked during this
audit has mb=ymb=4.7 GeV, mH=125 GeV, GF=1.16639e-5 GeV^-2, and
Gamma_H=0.00638233934 GeV. These inputs imply **B_card ≈ 0.844640**, NOT 0.582.
This is a consequence of that tree-model/fixed-width input convention, **not a claim
that the precision Standard Model branching fraction is 84%**.

`reference_only_sigma_fb`, using B=0.582, is supplied separately for the signal
components. It NEVER replaces the model-consistent four-rate table. Before quoting
precision-phenomenology results, explicitly choose and document the common Higgs
Yukawa/width scheme. A custom common `PARAM_CARD` can be supplied, but it must respect
the restricted `sm` model and be used for every component. The scripts do not silently
retune a Yukawa or width merely to force a desired branching fraction.

## 5. Other baseline conventions

- Tree-level matrix elements in restricted `sm`; initial e/mu masses and Yukawas are
  zero, diagonal CKM. No claim of retaining tiny lepton-Yukawa contributions.
- mH=125 GeV and nonzero kinematic mb=4.7 GeV are required for this baseline.
- No pT or separation regulator is introduced. Finite mb regulates the final-bottom
  collinear limit; numerical enhancements and convergence still require attention.
- Unpolarized monochromatic beams, no ISR/beamstrahlung/lepton PDFs.
- Fixed renormalization reference scale mu_R=125 GeV, an explicit adopted convention.
- No shower, hadronization, jet clustering, detector effects, b-tag efficiencies,
  luminosity factor, event-yield calculation or distribution production.
- LO four massive partons are called “b candidates”; they are not a resolved-jet prediction.

## 6. Run on an existing MadGraph installation

Requires Python 3.9+ compatible with your installed MadGraph5_aMC, a complete MG5
installation and a working Fortran build toolchain. No NumPy, ROOT, LHAPDF or pip
installation is needed for these helper scripts. Do not rebuild a working environment.
No code in this package downloads or installs software.

First run local tests:

```bash
unzip FCC_ue_MuC_HH4b_Final_v3.zip
cd FCC_ue_MuC_HH4b_Final_v3
bash run_tests.sh
```

Set the path to an existing MG5 executable and run:

```bash
MG5=/absolute/path/to/MG5_aMC/bin/mg5_aMC \
NEVENTS=10000 NDECAYS=50 \
bash run_all.sh
```

More events improve selection statistics; they are not by themselves a proof of
phase-space integration convergence. `NEVENTS` is PER FLAVOR COMPONENT. Eight
internal runs feed four totals. `NDECAYS` is the number of trial HH decays per
production event, not an increase in independent hard-event statistics.

For an initial source-generation/configuration check without physics integration:

```bash
MG5=/absolute/path/to/MG5_aMC/bin/mg5_aMC \
bash run_all.sh --only mue_HH --prepare-only
```

For a single requested group (all three flavors for a muon-collider group):

```bash
MG5=/absolute/path/to/MG5_aMC/bin/mg5_aMC \
bash run_all.sh --only mumu_4b
```

For an independent statistics/convergence comparison, use a different seed and a
NEW output directory:

```bash
MG5=/absolute/path/to/MG5_aMC/bin/mg5_aMC \
NEVENTS=30000 NDECAYS=100 SEED=2302026 \
WORK=/absolute/path/to/a/new/nonexistent/run_directory \
bash run_all.sh
```

Default output is a new timestamped `work/run_...` directory. An explicitly existing
WORK directory is rejected. Process cards do not use destructive `output -f`.
Partial results, logs and MG debug files are preserved on failure.
`PYTHON=/path/to/python` selects the interpreter for the existing environment.
`PARAM_CARD=/absolute/path/to/common_param_card.dat` is an optional advanced override.
A parameter card cannot restore interactions that the `sm` restriction already removed.

## 7. Results, errors and reproducibility

Each run stores effective configuration, source-script checksums, the MG version,
process/run/parameter cards, full generator and analysis logs, component JSON reports,
and four-row `results.csv`/`results.json` summaries. The reports are in fb (1 pb=1000 fb).
All eight component errors are explicit; distinct neutrino-flavor integrals are combined
in quadrature under the independent-run assumption.

For a component, A=sum(w_i f_i)/sum(w_i), where f_i is a binary pass for direct 4b
or the accepted fraction of decay trials for an HH hard event. The selection MC
standard error uses a positive-weight ratio estimator with the **hard event as the
statistical cluster**. Integration normalization error and acceptance-sampling error
are shown separately. Their quadrature is an approximate diagnostic: covariance
between integration and event generation is neglected. No scale, model, branching,
finite-width or detector systematic uncertainty is included.

For zero selected direct-4b events, the primary rate is **null**, not a claimed zero.
For equal-weight events an exact one-sided 95% binomial acceptance upper bound is
reported, conditional on the generated normalization. It is not a replacement for
a converged cross-section measurement. A missing flavor also makes a total incomplete.
Negative-weight/NLO samples, unexpected final states, ambiguous files, truncated LHE,
wrong beams and incompatible model parameters cause explicit errors.

## 8. Validation status and what remains

See `VALIDATION_REPORT.md` and `validation/unit_tests.log` for the executed local tests.
The synthetic fixtures used by tests are mathematical/software checks, never physics
predictions. They are created in temporary directories and are not delivered as events.

Before sending numbers to CERN: check real MG5 process generation and diagram content,
all saved parameters/cuts, integration warnings and unweighting efficiency; inspect
accepted counts; repeat with independent seeds and increased statistics; compare
signal decay sampling; document the Higgs normalization and reference scale. Retain
the labels “LO, parton-level, unpolarized, no ISR/shower/detector” and the different
actual sqrt(s) values. Do not describe the full 4b rate as background only.

## 9. Contents and references

- `configuration.json`, `docs/CONFIRMED_COLLIDER_CONFIGURATIONS.md`: exact setup and status.
- `cards/*.mg5`, `processes.py`: eight flavor-resolved process cards and their four totals.
- `configure_run.py`: full MG5-schema cut reset, model checks and audit output.
- `physics.py`, `lhe_io.py`, `analyze_lhe.py`: explicit kinematics, LHE input, cuts and errors.
- `run_all.sh`, `run_workflow.py`, `collect_results.py`: safe execution and four-row summaries.
- `tests/`, `run_tests.sh`, `VALIDATION_REPORT.md`: reproducible offline validation.
- `RESULTS_NOT_YET_COMPUTED.csv`: deliberately empty numerical template, not results.
- `docs/CHANGELOG.md`, `docs/SOURCES.json`, `SHA256SUMS.txt`: audit trail and references.

Primary source provenance is recorded in `docs/SOURCES.json`. Sources were used to
check MG5 syntax/schema, default SM inputs, the scalar partial-width convention and
the LHE structure. They do not certify this package's real MG5 execution.
