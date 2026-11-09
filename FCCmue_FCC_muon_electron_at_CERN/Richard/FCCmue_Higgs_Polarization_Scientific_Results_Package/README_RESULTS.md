# FCC–μe inclusive Higgs polarization results — independent numerical audit

**Dataset:** The user-provided `FCCmue_Higgs_PolScan_full_exact_REVIEW.zip`, processed 2 November 2026.

## Files

- `FCCmue_Higgs_Polarization_Results_Audit.pdf`: 5-page technical/scientific report with process definitions, main cross sections, both publication figures, all 48 results, linearity fits and caveats.
- `FCCmue_Higgs_Polarization_Results_Audit.tex`: editable LaTeX source. Compile with `pdflatex FCCmue_Higgs_Polarization_Results_Audit.tex` twice from the same directory as the figure PDFs.
- `Figure_1_absolute_cross_sections.pdf` / `.png`: four panels of absolute inclusive LO cross sections at exact 1 and 2 TeV, 300 dpi PNG.
- `Figure_2_polarization_ratios.pdf` / `.png`: four panels of normalized polarization enhancements, 300 dpi PNG.
- `cross_sections_48.csv`: full 48-point table including Monte Carlo integration errors, seeds and job identifiers.
- `linear_fits.csv`: weighted linearity fits (intercept, slope, relative slope, errors, chi-square and p-value).
- `independent_audit.json`: explicit checks and source checksums.

## Scientific definitions

- Electron is beam 1, unpolarized; positive muon is beam 2, with `polbeam2=0,20,40,60,80,100`.
- Exact `sqrt(s)=1 TeV`: `E_e=125 GeV, E_mu+=2000 GeV`.
- Exact `sqrt(s)=2 TeV`: `E_e=200 GeV, E_mu+=5000 GeV`.
- Stable Higgs bosons and full tree-level SM final-state matrix elements, no imposed kinematic cuts, and no Higgs branching ratios.
- Run cards use a 125 GeV fixed renormalization scale. MG5 version 3.6.4.
- 48 complete job records, each indicating 30,000 generated events.

## Caveats before publication

The review ZIP does not contain full LHE event samples. The original CERN worker validated event counts and final states, and this review independently checked all provided process cards, run cards, audit metadata, and logged seeds. The report does not certify independent numerical convergence or forward-region/cut-regulator stability. Quoted uncertainties are Monte Carlo integration errors only, not theory uncertainties. Existing numerical results are marked `COMPLETED_UNVALIDATED` by the original workflow. Run additional independent-seed / forward-region checks before publication.

The original attached v1.1 package and the review ZIP contain byte-identical `scan.py`, `card_utils.py`, `plot_results.py`, and `CONFIG.json`.

## Authorship and provenance

Derived entirely from the uploaded CERN review archive. This results package does not change the source event-generation files or modify any source cross sections; fits and figures are new postprocessing results.
