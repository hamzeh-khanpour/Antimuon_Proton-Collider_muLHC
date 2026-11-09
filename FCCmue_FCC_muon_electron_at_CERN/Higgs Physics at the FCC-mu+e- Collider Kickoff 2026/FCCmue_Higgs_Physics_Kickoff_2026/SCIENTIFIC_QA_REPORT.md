# Scientific and build quality assurance — FCC-mue Higgs Kick-off

**Status:** Compiled scientific presentation (preliminary LO phenomenology, not a peer-reviewed physics sensitivity study).

## Actual execution checks

| Acceptance check | Status | Evidence / limitation |
|---|---|---|
| Authentic AGH Beamer theme and aspect ratio | **PASS** | Exact supplied `.sty` files, `aspectratio=1610`, `\usetheme[parttitle=rightfooter]{AGH}`; rendered opening and content pages checked |
| Main and backup frames | **PASS** | 40 substantive main frames + 8 substantive backups; PDF 48 pages |
| TeX actually compiled | **PASS** | `pdflatex`/`latexmk -pdf`, with real PDF output; `pdfinfo` checked |
| Missing image/font/file TeX errors | **PASS** | Final LaTeX log has zero fatal errors and no missing graphics |
| Vertical content clipping warnings | **PASS** | Final `Overfull \\vbox` check: zero; representative rendered pages inspected |
| Source CSV completeness | **PASS** | 48 unique combinations = 4 processes × 2 energies × 6 polarizations |
| Original source matching | **PASS** | 48/48 data rows matched CERN `reports/cross_sections.csv`: seeds, job IDs, counts, sigma, MC errors |
| Original generated MG5 vector diagrams | **PASS** | Four `matrix.pdf` exports copied; diagram mapping checked; CC H/NC H each one diagram, CC HH/NC HH each four diagrams |
| Two actual vector source-data plots | **PASS** | 48-row numerical plot script run; PDFs included and embedded |
| Polarization convention | **PASS** | e- beam 1 unpolarized; positive muon beam 2 scan; CC expected 1+P comparison |
| Older benchmark energies and cuts | **PASS** | 0.9798/1.9131 TeV historical distinguished from exact 1/2 TeV; NC pT_l cut; different 110--130 vs 80--130 mass windows |
| Proposal luminosity revision | **PASS** | arXiv:2610.40451v2 Table 1 checked; 0.98 TeV peak luminosity 0.63 × 10^34, not older-version 3.2 value |
| Older H->bb normalization | **PASS (flagged)** | Historical model card BR=0.844640; not silently replaced with standard ≈0.58 |
| Full NC four-bottom inconsistency | **OPEN PHYSICS ISSUE** | 0.007713 fb complete NC4b below 0.012925 fb bbH sample; original audit says not explained; slide 32 flags validation |
| Independent Monte Carlo reruns | **NOT PERFORMED** | Existing logs and QA inspected; no CERN jobs run in this slide-production task |
| Forward NC lepton and regulator study | **NOT PERFORMED** | Needs realistic charged-lepton acceptance and stability tests |
| Anomalous Higgs coupling scans | **NOT PERFORMED** | Proposed only; no kappa3/kappa2V limits claimed |
| HHH inclusive and detector-level rates | **NOT PERFORMED** | Proposed only; no numeric HHH claims |
| FCC-mue proposal original accelerator diagram | **SCHEMATIC SUBSTITUTE DISCLOSED** | Figure redrawn after primary Fig.1 with attribution, not an original proposal raster/vector extraction |

## Numerical context

- At +80% positive-muon polarization, charged-current rate enhancement ≈1.8; neutral-current ≈1.175.
- Unpolarized energy ratios are ≈1.83 (CC H), ≈1.87 (NC H), ≈5.63 (CC HH), ≈5.69 (NC HH), from the 48-row CSV.
- Fit uncertainties are **numerical** only; no detector/statistical projection implied.
- Historical four-bottom results carry their native cuts, accepted-event statistics, branching convention and process overlap.

## Remaining limitations for collaborators

1. Re-run representative CERN points with independent seeds; scan NC forward cuts and generator regulators.
2. Resolve the NC4b/associated bbH mismatch with resonance-aware integration and event re-analysis.
3. Standardize electroweak parameters and Higgs branching fractions before combining data or quoting Higgs self-coupling sensitivities.
4. Agree on realistic luminosities/polarization fractions, shower/detector assumptions, and background definitions.
5. Choose a consistent HEFT or SMEFT model before varying κ3 and κ2V, and treat HHH separately as a feasibility study.
