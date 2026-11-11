# CERN unpolarized Higgs-pair coupling scan

The CERN collector reported 88 validated new jobs, each with 30,000 events, and four reused HHVBF SM closure points. The supplied tables contain 92 channel rates and 46 CC+NC sums. The grid, seeds, beam settings, SM inputs and agreement between CSV and JSON were checked. The sums and their independent MC errors agree with a recalculation from the channel rates.

The samples describe inclusive LO stable-Higgs production at exact 1 and 2 TeV, with both beams unpolarized and CV = C2V = 1. Cross sections are in fb and the reported uncertainties are MC integration errors.

| κ₃ | CC+NC at 1 TeV [fb] | CC+NC at 2 TeV [fb] |
|---:|---:|---:|
| -10 | 12.032 ± 0.01542 | 39.72475 ± 0.04012 |
| 0 | 0.272797 ± 0.0004967 | 1.13532 ± 0.001454 |
| 0.1 | 0.2456888 ± 0.0004412 | 1.04034 ± 0.00127 |
| 1 | 0.0838932 ± 0.0001349 | 0.4744543 ± 0.0006595 |
| 1.5 | 0.0563612 ± 0.000101 | 0.361946 ± 0.0005493 |
| 5 | 1.117294 ± 0.001298 | 3.642722 ± 0.003478 |
| 10 | 6.441509 ± 0.005444 | 20.69758 ± 0.02712 |

The fits use σ(κ₃) = A + B κ₃ + C κ₃². The total coefficients and covariance are sums of the independent CC and NC fits. The inferred minima and their MC uncertainties are below.

| √s | A [fb] | B [fb] | C [fb] | κ₃ at minimum | σ at minimum [fb] |
|---:|---:|---:|---:|---:|---:|
| 1 TeV | 0.27332692 | -0.27903145 | 0.08954159 | 1.55811 ± 0.00036 | 0.055946 ± 0.000038 |
| 2 TeV | 1.13606330 | -0.95243059 | 0.29065771 | 1.63841 ± 0.00046 | 0.355829 ± 0.000215 |

All four weighted channel fits use 23 points and have 20 degrees of freedom. An independent quadratic through κ₃ = 0, 1, 2 was compared with the other 20 points, including uncertainty from the anchor points. The largest absolute pull over the four channel checks is 1.81.

| √s | CC χ²/20 | NC χ²/20 |
|---:|---:|---:|
| 1 TeV | 13.38/20 | 11.73/20 |
| 2 TeV | 15.82/20 | 17.50/20 |

The negative interference term produces a minimum above the SM coupling at both energies. The shaded band on each figure is the observed ATLAS+CMS one-parameter 95% interval from [arXiv:2602.23991](https://arxiv.org/abs/2602.23991).

To regenerate the PDF and PNG plots with NumPy and Matplotlib installed, run the following from the unpacked directory.

```bash
python3 plot_scan.py --report tables/scan_report.json --outdir plots
```

Source ZIP SHA-256 `f8b895ad04f584e3e15b10af0f6ecb617e034daef209af0ceb31d48c7f4f6ca0`.
CERN run manifest SHA-256 `6b0954b8d84e11d2d8ae0039d0f158f21ea163d292431b0c7dfd411b8c106e15`.
