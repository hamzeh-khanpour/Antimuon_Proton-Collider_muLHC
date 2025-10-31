
---

# Antimuon–Proton Collider (μLHC): γγ → W⁺W⁻ (SM & EFT)

This repository contains inputs, logs, and analysis code for **photon–photon production of W-boson pairs** at a **μLHC-style** collider configuration (**proton ⊗ antimuon**). It provides:

* MG5_aMC@NLO generation cards/logs for **SM** and **EFT** samples,
* an analysis script to build **dσ/dM_{WW}** and **counts** distributions with a **CMS-style overlay + ratio** plot,
* a light validation checklist for beam/EPA settings and normalization.

## Physics scope

We study the elastic/collinear EPA process:
[
\gamma\gamma \to W^+W^-
]
generated at LO in MG5_aMC@NLO. We compare the **Standard Model (NP=0)** against an **EFT benchmark (NP>0)** by modifying `anoinputs` (e.g. a non-zero **FM2** Wilson coefficient) and plotting the **M_{WW}** spectrum:
[
M_{WW} \equiv m!\left(p_{W^+}+p_{W^-}\right) \quad\text{(equal to }\sqrt{\hat s_{\gamma\gamma}}\text{ at parton level).}
]

## μLHC collider configuration (generation)

* **Beams**: `lpp1 = 2` (elastic photon from **proton/ion**), `lpp2 = 4` (photon from **muon** EPA).
* **Energies**: `ebeam1 = 7000.0 GeV` (p), `ebeam2 = 1000.0 GeV` (μ).
* **EPA models**: `pdlabel1 = iww`, `pdlabel2 = iww` (Improved Weizsäcker–Williams on both beams).

  * Optional refinement: for **strict proton elastic form factors**, set `pdlabel1 = chff` (or `edff`) consistently for **both SM and EFT** productions.
* **Process**: `a a > w+ w-`

  * **SM**: `NP=0`
  * **EFT**: `NP>=1` with specific `anoinputs` (e.g. **FM2 = 1.0e−12**, others 0).
    Decide whether you want **interference-only** or **full (interference + EFT²)**; this depends on `CouplingOrders` in the UFO. Keep the choice documented.
* **Version**: MG5_aMC@NLO **3.6.4**
* **Normalization**: `event_norm = average`; with unweighted LO events, per-event weight is **XWGTUP** if present, otherwise **σ_int / N**.
* **Example (from headers)**:
  SM: **σ_int ≈ 0.28838 pb** (N=1,000,000)
  EFT: **σ_int ≈ 0.30292 pb** (N=1,000,000)

## Repository layout

```
.
├── muLHC_dsig_dMWW_v2.py   # main analysis & plotting script (overlay + ratio)
├── ... (MG5 logs/LHE files)  # SM/EFT LHE files and generation headers
└── README.md               # this file
```

## Environment

* Python ≥ **3.10**
* **NumPy**, **Matplotlib**
* **mplhep** (optional; used for “CMS” plotting style; script falls back gracefully if missing)
* Standard library: `argparse`, `gzip`, `re`, `csv`

Install (example):

```bash
pip install numpy matplotlib mplhep
```

## Input samples

Update the paths below to point to your LHE files:

* **SM**: `/home/.../muLHC_SM_aa_ww/Events/run_01/muLHC_SM_aa_ww.lhe`
* **EFT**: `/home/.../muLHC_EFT_aa_ww/Events/run_01/muLHC_EFT_aa_ww.lhe`

The script reads the LHE header for `Number of Events` and `Integrated weight (pb)`, and for each event reads:

* **XWGTUP** (if present) → used as weight,
* **W⁺ (PDG=24)** and **W⁻ (PDG=−24)** four-vectors (status==1).

## Usage

The script creates a **two-panel figure** (overlay + EFT/SM ratio) and a matching **CSV**. You can plot either **dσ/dM** (pb/GeV) or **expected events/bin** at a chosen luminosity.

```bash
# dσ/dM_WW (pb/GeV), 100 bins from 160–6000 GeV, log-y
python muLHC_dsig_dMWW_v2.py \
  /path/to/muLHC_SM_aa_ww.lhe \
  /path/to/muLHC_EFT_aa_ww.lhe \
  --bins 100 --range 160 6000 --yield-mode dsig --logy \
  --out-prefix mww_compare_muLHC_SM_vs_EFT_dsig_logy

# expected counts (events/bin) at 100 fb^-1, same binning
python muLHC_dsig_dMWW_v2.py \
  /path/to/muLHC_SM_aa_ww.lhe \
  /path/to/muLHC_EFT_aa_ww.lhe \
  --bins 100 --range 160 6000 --yield-mode counts --lumi-fb 100 \
  --out-prefix mww_compare_muLHC_SM_vs_EFT_counts_100fb
```

### Key options

* `--bins N` — number of M_{WW} bins (default: 80)
* `--range Mmin Mmax` — M_{WW} range in GeV (default: 160–5000)
* `--yield-mode {dsig,counts}` — differential cross section or expected events/bin
* `--lumi-fb L` — luminosity (fb⁻¹) when `--yield-mode counts`
* `--logy` — log scale on the main panel
* `--title "..."` — custom plot title
* `--eft-text "..."` — custom EFT label in the on-plot info panel
* `--out-prefix NAME` — base name for outputs (`.png`, `.pdf`, `.csv`)

### Outputs

* **Figure**: `<out-prefix>.png`, `<out-prefix>.pdf`
  Top: **SM** (dashed) vs **EFT** (solid) with step-style & last-bin plateau; small info box with σ_gen/σ_fid and an EFT tag.
  Bottom: **EFT/SM** ratio with stat band (from weighted histograms).
* **Table**: `<out-prefix>.csv`
  Bin edges, SM/EFT yields (either dsig or counts), ratio, ratio stat-uncertainty.

## Validation checklist (recommended)

1. **Beam sanity**: `<init>` shows `2212` (proton) and `13` (μ⁻) with 7 TeV and 1 TeV — matches `lpp1=2`, `lpp2=4`.
2. **EPA models**: `iww` is a sensible baseline. If targeting strict **elastic proton** photons, use `chff`/`edff` on the proton and **regenerate both** SM & EFT for apples-to-apples.
3. **EFT mode**: Decide **interference-only** vs **full (incl. EFT²)** and keep it consistent (depends on UFO `CouplingOrders`).
4. **Normalization**: Sum **XWGTUP** over all events and compare to header **σ_int** (should agree within integration precision).
   The script also prints the header σ and (if available) the σ(EFT)/σ(SM) ratio.
5. **No cuts**: Generation is inclusive; σ_fid = σ_gen in the panel by default (you can later add fiducial selections if needed).
6. **Reproducibility**: Record `iseed`, `nevents`, MG version, beams, EPA labels, and `anoinputs`.

## Troubleshooting

* **Overlapping x-labels between main & ratio panels**:
  In `plot_overlay_and_ratio`, hide the top x-labels:

  ```python
  ax.tick_params(axis="x", which="both", labelbottom=False)
  ```

  or increase the vertical spacing:

  ```python
  gs = gridspec.GridSpec(2,1, height_ratios=[3,1], hspace=0.18)
  ```
* **`tight_layout` warning**: harmless; can be safely ignored (or suppressed with `warnings.filterwarnings`).
* **Header σ ratio print error**: fixed by guarding against `None`/zero values and removing stray whitespace in format specifiers.

## Roadmap

* Optional **overflow→last-bin folding** flag (to exactly mimic some CMS macros).
* Alternative EPA models (chff/edff) comparison study.
* Fiducial selections and detector-level studies (Delphes).

## Acknowledgments

* **MadGraph5_aMC@NLO 3.6.4** for event generation.
* Collaborators and colleagues for discussions on μLHC and photon-initiated processes.

---

*Feel free to adapt paths, titles, and the EFT label to match your study. PRs welcome!*
