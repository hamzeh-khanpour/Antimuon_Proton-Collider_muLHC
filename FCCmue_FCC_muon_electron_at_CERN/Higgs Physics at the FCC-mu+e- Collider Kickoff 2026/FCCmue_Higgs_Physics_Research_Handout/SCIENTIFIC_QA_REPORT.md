# Scientific QA — FCC-mue Higgs 20-page research handout

## Verified during current production

| Check | Outcome |
|---|---|
| Main editable .tex and compiled PDF | PASS — `latexmk -pdf` successful |
| Page size and count | PASS — exactly 20 A4 pages including front matter and bibliography |
| PDF page text content | PASS — 20 pages inspected programmatically; no empty pages |
| 48 CERN inclusive results | PASS — 48 unique combinations of 4 processes, 2 energies, 6 polarizations |
| Original source comparison | PASS — all 48 `sigma_fb` and `sigma_mc_err_fb` values matched `reports/cross_sections.csv` in original review ZIP within floating precision |
| Original MG5 diagram exports | PASS — CC H, NC H, CC HH, NC HH included as original vector assets; cropped HH diagrams retain source IDs |
| Distinct beam configurations | PASS — design-like 0.9798/1.9131 TeV separate from exact 1/2 TeV scan |
| Source manuscript v2 luminosity table | PASS — 0.60 TeV 4.5×10^34; 0.98 TeV 0.63×10^34 cm^-2 s^-1 |
| Charged-current and neutral-current polarization conventions | PASS — definitions and approximate formulas stated |
| All older four-bottom cut distinctions | PASS — 110–130 GeV for earlier HH, NC 1 GeV outgoing lepton generation, 80–130 GeV for muon ZH, |eta_b|<5 |
| Historical H→bb normalization | PASS — 0.844640 explicitly warned; conventional 0.582 sourced |
| NC full 4b vs bbH mismatch | PASS — flagged unresolved, no invented explanation |
| HHH cross sections, κ3/κ2V limits | PASS — explicitly labeled proposed, none invented |
| Reference citations | PASS — numbered entries rendered and source hyperlinks valid LaTeX |
| Serious TeX overfull boxes | PASS — zero `Overfull \\hbox`/`\\vbox` in final `.log` |
| Visual inspection | PASS — contact images and higher-resolution original-diagram/bibliography pages inspected |

## Not independently established during current production

1. Physics convergence under independent random seeds and numerical integration settings.
2. Regulator and forward-charged-lepton fiducial stability for NC processes.
3. Consistent regeneration of historical four-bottom amplitudes with shared parameters, cuts, and physical branching fractions.
4. Higher-order electroweak/QCD effects, beam energy spread, background and detector performance.
5. Quantitative κ3, κ2W/2Z or κ4 bounds; no such results are claimed.

**Status:** Scientific discussion handout; rigorous source-based synthesis of preliminary LO calculations, not a journal paper or validated prospective coupling sensitivity study.
