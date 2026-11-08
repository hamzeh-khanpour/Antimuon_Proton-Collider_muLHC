# v3.0.0 audit changes — 23 October 2026

This package supersedes `FCC_ue_MuC_HH4b_1TeV_Starter.zip` and
`FCC_ue_MuC_HH4b_2TeVx120GeV_NoPt.zip`. Prior archives have not been modified.

## Physics definitions retained

The mu-e beam energies remain 2000 and 120 GeV. The mu-mu baseline remains
500 and 500 GeV. There is no pT or DeltaR cut. Every final bottom must satisfy
abs(eta_lab)<5. Either of the two disjoint opposite-charge assignments may pass,
provided both candidate masses are in [110,130] GeV. The direct-4b calculation
is not changed into a Higgs-subtracted background.

## Corrections and clarifications

1. **Confirmation status:** the mu-mu symmetric energy split, unpolarized beams,
   laboratory-frame convention, both-candidate window, and neutrino-flavor sum
   are now explicitly labeled as adopted conventions rather than quoted confirmations.
2. **Branching normalization:** the primary NWA signal now uses the tree partial
   width divided by the total width from the actual common parameter card. The old
   independent 0.582 factor is only a separate reference result. This can materially
   change a number, so it is prominently documented rather than silently patched.
3. **No hidden cuts:** a narrow text substitution was replaced by an audit of all
   cuts registered in the installed MG5 schema. Generation cuts are disabled;
   eta and the two-pair requirement are imposed in analysis only.
4. **Flavor bookkeeping:** eight independent flavor components produce the same four
   requested totals. A missing flavor makes a total incomplete, not smaller by fiat.
5. **Frames:** the incoming LHE momenta now determine whether a lab boost is needed.
   Incoming species, orientation, invariant energy and outgoing momentum conservation
   are checked. A lab sample cannot accidentally receive the boost twice.
6. **Statistics:** integration and selection MC errors are separate. HH decay trials
   are clustered by the hard production event. Approximate combined errors and their
   covariance limitation are stated. Zero selected events are not reported as a
   measured zero; a conditional binomial upper bound is provided when applicable.
7. **Robust input:** plain/gzipped LHE, event attributes, Fortran exponents, truncation,
   process IDs, masses, final-state content and positive LO weights are checked.
8. **Safe execution:** new run directories, no destructive process overwrite,
   process-artifact checks, detection of fatal MG messages even with exit code zero,
   exact fresh LHE selection, hashes, configuration audits and logs.
9. **No secondary stages:** active shower/MadSpin/detector/reweight/MA5 cards in a
   freshly exported process are archived under `.disabled_by_baseline` rather than run.
10. **More validation:** 56 offline tests, including an explicitly mocked end-to-end
    workflow. This does not replace real MG5 process generation or integration.

## Deliberately not implemented or claimed

No integration-level custom pairing cut, no experimental charge-blind jet algorithm,
no detector mass smearing, no best-chi2 selection as the default, no diagram-subtracted
background, no polarization assumption beyond unpolarized beams, no ISR, no shower,
no numerical cross sections, and no real-MadGraph compatibility/convergence certification.
