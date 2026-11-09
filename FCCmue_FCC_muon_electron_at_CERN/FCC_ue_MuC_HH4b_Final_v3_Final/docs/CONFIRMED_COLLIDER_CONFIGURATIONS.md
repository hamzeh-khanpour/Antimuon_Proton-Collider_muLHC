# Final collider configurations and their confirmation status

**Request:** four integrated cross sections after cuts, not distributions or event yields.
**Source:** Krzysztof Piotrzkowski's email thread supplied by Hamzeh, 23 October 2026.

| Quantity | FCC-ue: mu+ e- | Muon collider: mu+ mu- | Status / interpretation |
|---|---|---|---|
| Beam 1 along +z | mu+, 2000 GeV | mu+, 500 GeV | mu-e energy explicitly confirmed; mu-mu split is the symmetric baseline |
| Beam 2 along -z | e-, 120 GeV | mu-, 500 GeV | mu-e energy explicitly confirmed; mu-mu split is the symmetric baseline |
| sqrt(s), massless beam approximation | 979.795897 GeV | 1000 GeV | Derived from the stated energies |
| COM rapidity in the laboratory | +1.406705 | 0 | Derived; +z is chosen along the positive muon |
| Beam polarization | Unpolarized | Unpolarized | Adopted; no polarization was specified |
| Fiducial frame | Laboratory | Laboratory = COM | Adopted laboratory interpretation of the acceptance |
| Bottom-parton pseudorapidity | abs(eta) < 5 for all four | abs(eta) < 5 for all four | Threshold explicitly requested |
| Minimum bottom pT | None (0 GeV) | None (0 GeV) | Explicitly confirmed: “no cut for now” |
| Minimum parton separation DeltaR | None | None | Not specified; no additional cut is introduced |
| Pair-mass window | 110 <= m1,m2 <= 130 GeV | 110 <= m1,m2 <= 130 GeV | Window requested; applying it to two candidates is the adopted interpretation |
| Pairing rule | Either valid disjoint b-bbar assignment | Same | Adopted; truth-level b versus bbar identification |
| Neutrino content | nu_e anti-nu_mu | Sum of nu_e anti-nu_e, nu_mu anti-nu_mu, nu_tau anti-nu_tau | Adopted inclusive missing-neutrino definition |
| Requested output | HH->4b signal and complete nu nu 4b rate | Same | Four totals, in fb with MC errors |

The clarification does **not** explicitly replace the muon-collider energy. Consequently,
the original nominal 1 TeV mu+mu- request is retained as 500+500 GeV. Do not describe this
symmetric split as a separately confirmed email instruction. Do not silently reset it to
489.897949+489.897949 GeV to match the mu-e invariant energy.

For massless head-on beams:

    sqrt(s) = 2 sqrt(E1 E2)
    y_COM,lab = 0.5 log(E1/E2)

The mu-e configuration is approximately, but not exactly, 1 TeV. Label the results
979.80 GeV and 1000 GeV respectively.

## Shared calculation conventions (not extra instructions from Krzysztof)

- Leading-order/tree-level, parton-level calculation in the default restricted `sm` UFO.
- Required bottom kinematic mass 4.7 GeV; required Higgs mass 125 GeV.
- Massless incoming e and mu, zero e/mu Yukawa couplings, and diagonal CKM under the
  default `sm` restriction. Keep the corresponding restricted entries zero.
- Common electroweak inputs, Yukawas and widths read from, checked, and archived with
  the actual generated parameter cards. No silently imported PDG branching fraction.
- Fixed renormalization reference scale 125 GeV. With no beam PDFs, factorization
  scales have no PDF-convolution role. No scale-variation/theory error is claimed.
- NWA scalar decays for the separately generated on-shell HH signal; full direct 4b
  amplitude includes all generated Higgs and non-Higgs diagrams and their interference.
- No ISR, beamstrahlung, shower, hadronization, jet clustering, detector simulation,
  b-tagging efficiencies, or luminosity normalization.

**“Four b jets” is implemented here as four massive final-state b partons.** No
resolved-jet observable is claimed with this no-pT/no-DeltaR parton-level selection.

**Status:** configuration and local software tests only. No MadGraph physics runs or
numerical collider cross sections have been produced in this package.
