# Validation report — v3.1.0 energy update

**Date:** 24 October 2026. The 56 offline tests passed on this updated source package.
These are NOT MG5 physics runs. The v3.0.0 record below is included for historical context.
The previous energies' numerical results remain archived in the uploaded original ZIP;
no new-energy cross sections or MadGraph-generated LHE files are included here.

---

# Validation report — v3.0.0

**Date:** 23 October 2026.

## Executed locally

| Check | Outcome |
|---|---|
| Python unit/regression tests | **56 passed** |
| Pairing: direct-only, crossed-only, both, neither | Passed |
| Disjointness and exclusion of same-charge assignments | Passed |
| No double counting when both pairings pass | Passed |
| Permutation invariance and mass-window boundaries | Passed |
| Strict eta acceptance and undefined-eta handling | Passed |
| Scalar-decay masses and four-momentum conservation | Passed |
| Incoming-beam/frame validation and no double boost | Passed |
| Massive-particle eta versus rapidity distinction | Passed |
| Common-card branching normalization and invalid inputs | Passed |
| Hidden-cut reset logic and beam settings | Passed against local schema test doubles |
| Plain/gzip LHE, optional event attributes and metadata | Passed |
| Truncated events and missing document closing tag | Rejected as required |
| Weighted acceptance and clustered signal MC uncertainty | Passed |
| Zero accepted events, negative weights, wrong modes/beams | Correct safeguards |
| Flavor completeness and independent-error combination | Passed |
| Fatal-log detection despite potential zero process exit | Passed |
| Existing output-directory protection | Passed in mock workflow |
| CLI analysis and full workflow | Passed with explicitly synthetic/mock inputs |
| Python source syntax and shell syntax | Passed; see `validation/syntax_checks.log` |
| ZIP integrity/checksums | Checked when packaging; `SHA256SUMS.txt` lists payload files |

The full test log is `validation/unit_tests.log`. Synthetic test fixtures are generated
in temporary directories and removed. Their cross-section fields are test constants,
not measurements or MadGraph estimates; no such event files are packaged as results.

## Not executed here

- Real MadGraph model import, diagram generation or source export.
- The run-card adapter against an actual locally installed MG5 release.
- Fortran compilation of a generated process.
- MadEvent integration, unweighting, or the four physical cross sections.
- Integration-level custom cuts, phase-space efficiency optimization, or numerical
  convergence comparisons across seeds and event counts.
- Gauge/width-scheme checks, scale uncertainties, finite-width signal corrections,
  showering, detector studies or validation against a second generator.

**No MadGraph installation was available in this working environment.** The local
software checks establish the tested bookkeeping and mathematics only. In particular,
the mock workflow tests orchestration interfaces, not MG5 physics behavior.

## Required validation on the target installation

Generate/configure a small component first and inspect its saved audit. Confirm the
full installed MG5 version and model restriction, all process content, massive b,
actual Higgs width/Yukawa/branching convention, fixed reference scale, beam energies
and zero generation cuts. Then inspect integration warnings, unweighting efficiency,
accepted counts and the separate MC errors for every component. Repeat independently
with increased integration/event statistics and decay trials. A reported Monte Carlo
error alone does not demonstrate correct convergence or control a theory uncertainty.

**Release status: AUDITED SETUP; PHYSICS EXECUTION AND NUMERICAL VALIDATION PENDING.**
