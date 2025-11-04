#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# python3.10 limits_muLHC_no_bkgs_v2.py  --lumi-fb 1000 --aeps 1.0  --make-plots --make-counting-limits --make-shape-limits --outdir out_muLHC
#

# =============================================================================
# γγ → W⁺W⁻ @ μLHC (semi-leptonic) — SM vs EFT (f = ±1 TeV⁻⁴)
# Ready-to-run with only:
#   python3.10 limits_muLHC_no_bkgs_v2.py --lumi-fb 1000 --aeps 1.0 \
#       --make-plots --make-counting-limits --make-shape-limits --outdir out_muLHC
#
# Features:
#   * Uses your default LHE paths (can override via CLI)
#   * Reads σ(pb) from each LHE banner (<MGGenerationInfo>: Integrated weight (pb))
#     and falls back to a strict <init> parser if the banner is missing
#   * Detects beams (μ, p) from <init> and builds the label (Eμ, Ep)
#   * Correct Δηjj and lepton centrality Cℓ, Cℓ^exp
#   * Robust per-event init of W candidates; jet-pairing near mW
#   * .lhe and .lhe.gz support
#   * Counting (tail σ) and multi-bin SHAPE Asimov limits
#   * CMS/mplhep plotting with log-y
# =============================================================================



import argparse, gzip, io, math, os, json
from typing import List, Tuple, Optional
import numpy as np
import matplotlib.pyplot as plt
import mplhep as hep
import ROOT


hep.style.use("CMS")


MW = 80.4  # GeV
PB_TO_FB = 1e3



# --------------------------
# Paths (defaults to your samples; CLI can override)
# --------------------------
DEFAULT_LHE_SM = "/home/hamzeh-khanpour/MG5_aMC_v3_6_4/muLHC_SM_aa_ww_semi_leptonic/Events/run_01/muLHC_SM_aa_ww_semi_leptonic.lhe"
DEFAULT_LHE_P  = "/home/hamzeh-khanpour/MG5_aMC_v3_6_4/muLHC_EFT_aa_ww_semi_leptonic/Events/run_01/muLHC_EFT_aa_ww_semi_leptonic.lhe"
DEFAULT_LHE_M  = "/home/hamzeh-khanpour/MG5_aMC_v3_6_4/muLHC_EFT_aa_ww_semi_leptonic/Events/run_02/muLHC_EFT_aa_ww_semi_leptonic.lhe"




# --------------------------
# I/O helpers
# --------------------------
def open_any(path: str):
    if path.endswith(".gz"):
        return io.TextIOWrapper(gzip.open(path, "rb"))
    return open(path, "r")

def read_lhe_xsec_and_beams(path: str):
    """
    Robustly return (xsec_pb, (id1,id2,E1_GeV,E2_GeV)).

    Strategy:
      1) Prefer banner <MGGenerationInfo>: a line like "Integrated weight (pb)  :  <value>"
      2) Fallback to <init>:
         - Read header: idbmup1 idbmup2 ebmup1 ebmup2 pdfgup1 pdfgup2 idwtup nprup
         - Sum XSECUP over the next exactly nprup lines (first token), accepting D/E exponents.

    Notes:
      * This addresses the previous bug where unrelated large integers were mixed into σ.
    """
    # 1) Try banner first
    xs_banner = None
    with open_any(path) as f:
        for line in f:
            if "Integrated weight (pb)" in line:
                try:
                    xs_banner = float(line.split(":")[-1].strip())
                except Exception:
                    xs_banner = None
                break  # first occurrence is enough

    # 2) Parse beams and (if needed) <init> σ
    id1 = id2 = None
    E1 = E2 = None
    xs_init = None
    with open_any(path) as f:
        it = iter(f)
        for line in it:
            if "<init>" in line:
                # Next non-empty numeric header: id1 id2 E1 E2 pdf1 pdf2 idwt nprup
                header = ""
                while True:
                    header = next(it).strip()
                    if header and (header[0].isdigit() or header[0] == "-"):
                        break
                parts = header.split()
                if len(parts) >= 8:
                    id1, id2 = int(parts[0]), int(parts[1])
                    E1, E2   = float(parts[2]), float(parts[3])
                    nprup    = int(parts[7])
                    s = 0.0
                    # Exactly nprup subprocess lines: take the first token (XSECUP)
                    for _ in range(nprup):
                        l = next(it).strip()
                        while not l or (not l[0].isdigit() and l[0] != "-"):
                            l = next(it).strip()
                        tok0 = l.replace("D", "E").split()[0]
                        s += float(tok0)
                    xs_init = s
                break

    # Prefer banner σ; otherwise use <init>; error if neither found
    if xs_banner is not None:
        return xs_banner, (id1, id2, E1, E2)
    if xs_init is not None:
        return xs_init, (id1, id2, E1, E2)
    raise RuntimeError(f"Could not find cross section in {path}")

def label_from_beams(info, fallback="μLHC @ Eμ=1 TeV, Ep=7 TeV"):
    id1, id2, E1, E2 = info
    try:
        def is_mu(x): return abs(int(x)) == 13
        def is_p(x):  return int(x) == 2212
        if is_mu(id1) and is_p(id2):
            return f"μLHC @ Eμ={E1/1000:.3g} TeV, Ep={E2/1000:.3g} TeV"
        if is_p(id1) and is_mu(id2):
            return f"μLHC @ Eμ={E2/1000:.3g} TeV, Ep={E1/1000:.3g} TeV"
    except Exception:
        pass
    return fallback




# --------------------------
# Physics/util helpers
# --------------------------
def safe_hist(data, bins, r):
    h, edges = np.histogram(data, bins=bins, range=r)
    return h.astype(float), edges

def dsigma_from_counts(counts, xs_pb, n_events, bin_width):
    if n_events <= 0 or bin_width <= 0:
        return np.zeros_like(counts, dtype=float)
    return counts * (xs_pb / float(n_events)) / float(bin_width)

def integrate_tail_hist(y_pb_per_GeV, edges_GeV, thr_GeV):
    total = 0.0
    for i in range(len(y_pb_per_GeV)):
        lo, hi = edges_GeV[i], edges_GeV[i+1]
        if hi <= thr_GeV:
            continue
        width = hi - lo
        if lo < thr_GeV < hi:
            total += y_pb_per_GeV[i] * (hi - thr_GeV)
        else:
            total += y_pb_per_GeV[i] * width
    return float(total)

def q_asimov(mu, mu0):
    if mu <= 0 or mu0 <= 0:
        return float("inf")
    return 2.0*(mu - mu0 + mu0*math.log(mu0/mu))



def interval_asimov_exact(c, A, B, L_fb, Aeps, q_target=3.84, f_scan=300.0):
    """Two-sided 95% CL for σ(f)=c+Af+Bf² using Asimov q."""
    def qf(f):
        sig = max(c + A*f + B*f*f, 1e-18)
        mu  = L_fb * Aeps * sig * PB_TO_FB
        mu0 = L_fb * Aeps * c   * PB_TO_FB
        return q_asimov(mu, mu0)

    # right side
    flo, fhi, step = 0.0, 0.0, 0.1
    while True:
        fhi = flo + step
        if qf(fhi) >= q_target or fhi >= f_scan: break
        step *= 1.8
    for _ in range(80):
        mid = 0.5*(flo+fhi)
        if qf(mid) < q_target: flo = mid
        else: fhi = mid
    f_plus = 0.5*(flo+fhi)

    # left side
    flo, fhi, step = 0.0, 0.0, 0.1
    while True:
        fhi = flo + step
        if qf(-fhi) >= q_target or fhi >= f_scan: break
        step *= 1.8
    for _ in range(80):
        mid = 0.5*(flo+fhi)
        if qf(-mid) < q_target: flo = mid
        else: fhi = mid
    f_minus = -0.5*(flo+fhi)

    return f_minus, f_plus



def build_shape_coeffs(edges, y_sm, y_p, y_m, f0, Wmin=0.0, Wmax=None):
    if Wmax is None: Wmax = edges[-1]
    lo = edges[:-1]; hi = edges[1:]
    mask = (hi > Wmin) & (lo < Wmax)
    α_full = np.asarray(y_sm)[mask]
    β_full = (np.asarray(y_p)[mask] - np.asarray(y_m)[mask])/(2.0*f0)
    γ_full = (np.asarray(y_p)[mask] + np.asarray(y_m)[mask] - 2.0*np.asarray(y_sm)[mask])/(2.0*f0*f0)
    widths = (hi - lo)[mask].copy()
    # adjust partial first bin if Wmin cuts inside
    if mask.any():
        i0 = np.argmax(mask)
        if lo[i0] < Wmin < hi[i0]:
            frac = (hi[i0]-Wmin)/(hi[i0]-lo[i0])
            widths[0] *= frac
    α = np.clip(α_full, 1e-18, None)
    return α, β_full, γ_full, widths



def asimov_shape_interval(α, β, γ, widths, L_fb, Aeps, q_target=3.84, f_scan=1e3):
    const = L_fb * Aeps * 1000.0
    n0 = const * α * widths
    def q_of(f):
        dens = np.clip(α + β*f + γ*f*f, 1e-18, None)
        mu = const * dens * widths
        return 2.0*np.sum(mu - n0 + n0*np.log(n0/mu))

    # right
    flo, fhi, step = 0.0, 0.0, 0.1
    while True:
        fhi = flo + step
        if q_of(fhi) >= q_target or fhi >= f_scan: break
        step *= 1.8
    for _ in range(80):
        mid = 0.5*(flo+fhi)
        if q_of(mid) < q_target: flo = mid
        else: fhi = mid
    fr = 0.5*(flo+fhi)

    # left
    flo, fhi, step = 0.0, 0.0, 0.1
    while True:
        fhi = flo + step
        if q_of(-fhi) >= q_target or fhi >= f_scan: break
        step *= 1.8
    for _ in range(80):
        mid = 0.5*(flo+fhi)
        if q_of(-mid) < q_target: flo = mid
        else: fhi = mid
    fl = -0.5*(flo+fhi)
    return fl, fr




# --------------------------
# LHE parsing to observables
# --------------------------
def parse_lhe_file(path: str):
    """Return dict of arrays for all observables built at event end."""
    out = {
        "pt_leptons": [], "eta_leptons": [],
        "pt_leading_jet": [], "delta_r": [], "met": [],
        "C_lep": [], "C_lep_exp": [], "C_jets_abs": [], "deta_jj": [],
        "mW_had": [], "mW_lep": [], "mWW": []
    }

    with open_any(path) as f:
        in_event = False
        jets: List[ROOT.TLorentzVector] = []
        leptons: List[ROOT.TLorentzVector] = []
        neutrinos: List[ROOT.TLorentzVector] = []
        for raw in f:
            line = raw.strip()
            if "<event>" in line:
                in_event = True
                jets, leptons, neutrinos = [], [], []
                w_hadronic = None
                w_leptonic = None
                continue
            if "</event>" in line:
                in_event = False

                # MET
                metx = sum(n.Px() for n in neutrinos)
                mety = sum(n.Py() for n in neutrinos)
                out["met"].append(float(np.hypot(metx, mety)))

                # leading jet
                if len(jets) >= 1:
                    jlead = max(jets, key=lambda j: j.Pt())
                    out["pt_leading_jet"].append(float(jlead.Pt()))
                    # ΔR(ℓ, jlead)
                    for l in leptons:
                        out["delta_r"].append(float(l.DeltaR(jlead)))

                # leptons kinematics
                for l in leptons:
                    out["pt_leptons"].append(float(l.Pt()))
                    out["eta_leptons"].append(float(l.Eta()))

                # dijet obs + W_had
                if len(jets) >= 2:
                    j_sorted = sorted(jets, key=lambda j: j.Pt(), reverse=True)
                    j1, j2 = j_sorted[0], j_sorted[1]
                    eta1, eta2 = j1.Eta(), j2.Eta()
                    deta = abs(eta1 - eta2)
                    out["deta_jj"].append(float(deta))
                    eta_c = 0.5*(eta1 + eta2)           # dijet center
                    out["C_jets_abs"].append(abs(float(eta_c)))
                    # best pair near mW
                    best = None
                    for a in range(len(jets)):
                        for b in range(a+1, len(jets)):
                            cand = jets[a] + jets[b]
                            score = abs(cand.M() - MW)
                            if best is None or score < best[0]:
                                best = (score, cand)
                    if best:
                        w_hadronic = best[1]
                        out["mW_had"].append(float(w_hadronic.M()))

                    # lepton centrality
                    if deta > 0 and len(leptons) >= 1:
                        for l in leptons:
                            C = (l.Eta() - eta_c) / deta
                            out["C_lep"].append(float(C))
                            out["C_lep_exp"].append(float(np.exp(-abs(C))))

                # W_lep
                if len(leptons) >= 1 and len(neutrinos) >= 1:
                    lbest = max(leptons, key=lambda l: l.Pt())
                    nu_vec = sum(neutrinos, ROOT.TLorentzVector())
                    w_leptonic = lbest + nu_vec
                    out["mW_lep"].append(float(w_leptonic.M()))

                # MWW
                if (w_hadronic is not None) and (w_leptonic is not None):
                    ww = w_hadronic + w_leptonic
                    out["mWW"].append(float(ww.M()))
                continue

            if in_event:
                if not line or (not line[0].isdigit() and line[0] != "-"):
                    continue
                parts = line.split()
                if len(parts) < 10:
                    continue
                pdg = int(parts[0])
                status = int(parts[1])
                px, py, pz, E = map(float, parts[6:10])
                v = ROOT.TLorentzVector(); v.SetPxPyPzE(px, py, pz, E)

                if abs(pdg) in (11, 13, 15) and status == 1:
                    leptons.append(v)
                elif abs(pdg) in (12, 14, 16) and status == 1:
                    neutrinos.append(v)
                # treat everything else (non-γ, non-lepton, non-ν) with status=1 as jet
                elif abs(pdg) != 22 and status == 1 and abs(pdg) not in (11,12,13,14,15,16):
                    jets.append(v)

    return {k: np.asarray(v, dtype=float) for k, v in out.items()}



# --------------------------
# Differential spectra helper
# --------------------------
def make_dsigma(arr, xs_pb, nbins, r):
    counts, edges = safe_hist(arr, nbins, r)
    width = (r[1] - r[0]) / nbins
    return edges[:-1], dsigma_from_counts(counts, xs_pb, int(arr.size), width)



# --------------------------
# Plot helpers
# --------------------------
def style():
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    plt.tight_layout()


# --------------------------
# Main
# --------------------------
def main():
    ap = argparse.ArgumentParser(description="μLHC γγ→W⁺W⁻ (semi-lep) — SM vs EFT limits")
    ap.add_argument("--lhe-sm", default=DEFAULT_LHE_SM)
    ap.add_argument("--lhe-plus", default=DEFAULT_LHE_P, help="EFT +f0 sample (f0=1 TeV^-4)")
    ap.add_argument("--lhe-minus", default=DEFAULT_LHE_M, help="EFT -f0 sample")
    # xs are OPTIONAL now; if omitted, read from LHE banner/<init>
    ap.add_argument("--xs-sm", type=float, default=None, help="σ_SM in pb (overrides LHE)")
    ap.add_argument("--xs-plus", type=float, default=None, help="σ(+f0) in pb (overrides LHE)")
    ap.add_argument("--xs-minus", type=float, default=None, help="σ(-f0) in pb (overrides LHE)")
    ap.add_argument("--f0", type=float, default=1.0, help="Reference EFT coupling in TeV^-4")
    ap.add_argument("--lumi-fb", type=float, default=1000.0)
    ap.add_argument("--aeps", type=float, default=1.0)
    ap.add_argument("--label", default=None, help="If not given, auto-built from beam IDs/energies")
    ap.add_argument("--outdir", default="muLHC_outputs")
    ap.add_argument("--make-plots", action="store_true")
    ap.add_argument("--make-counting-limits", action="store_true")
    ap.add_argument("--make-shape-limits", action="store_true")
    ap.add_argument("--nbins", type=int, default=40)
    ap.add_argument("--mww-min", type=float, default=160.0)
    ap.add_argument("--mww-max", type=float, default=1600.0)
    args = ap.parse_args()

    os.makedirs(args.outdir, exist_ok=True)

    # Cross sections and label from LHE if not provided
    xs_sm, beam_sm = read_lhe_xsec_and_beams(args.lhe_sm)
    xs_p,  beam_p  = read_lhe_xsec_and_beams(args.lhe_plus)
    xs_m,  beam_m  = read_lhe_xsec_and_beams(args.lhe_minus)

    # Prefer CLI overrides if given
    if args.xs_sm is not None: xs_sm = args.xs_sm
    if args.xs_plus is not None: xs_p = args.xs_plus
    if args.xs_minus is not None: xs_m = args.xs_minus

    # Build label
    label_auto = label_from_beams(beam_sm)
    LABEL = args.label if args.label is not None else label_auto

    # Parse LHE → observables
    D_sm  = parse_lhe_file(args.lhe_sm)
    D_p   = parse_lhe_file(args.lhe_plus)
    D_m   = parse_lhe_file(args.lhe_minus)

    # Binning
    NB = args.nbins
    R_mWW   = (args.mww_min, args.mww_max)
    edges = np.linspace(R_mWW[0], R_mWW[1], NB+1)

    # Spectra for MWW (used for limits)
    x_sm, y_mWW_sm = make_dsigma(D_sm["mWW"],  xs_sm, NB, R_mWW)
    x_p,  y_mWW_p  = make_dsigma(D_p["mWW"],   xs_p,  NB, R_mWW)
    x_m,  y_mWW_m  = make_dsigma(D_m["mWW"],   xs_m,  NB, R_mWW)



    # --- Optional plots
    if args.make_plots:
        plt.figure(figsize=(8,6))
        plt.step(x_sm, y_mWW_sm, where="mid", label="SM")
        plt.step(x_p,  y_mWW_p,  where="mid", label=f"+f0 (f0={args.f0} TeV$^{{-4}}$)")
        plt.step(x_m,  y_mWW_m,  where="mid", label=f"−f0 (f0={args.f0} TeV$^{{-4}}$)")
        plt.yscale("log")
        plt.xlabel(r"$M_{WW}$ [GeV]")
        plt.ylabel(r"$d\sigma/dM_{WW}$ [pb/GeV]")
        plt.title(rf"$\mu^- p\to\mu^- W^+W^- p$  —  {LABEL}")
        style()
        plt.savefig(os.path.join(args.outdir, "dsigma_mWW.pdf"), dpi=300)

    out_summary = {
        "inputs": {
            "lhe_sm": args.lhe_sm, "lhe_plus": args.lhe_plus, "lhe_minus": args.lhe_minus,
            "xs_sm_pb": xs_sm, "xs_plus_pb": xs_p, "xs_minus_pb": xs_m,
            "label": LABEL, "nbins": NB, "mww_range": R_mWW,
            "lumi_fb": args.lumi_fb, "aeps": args.aeps
        }
    }



    # --- Counting (tail σ)
    THRS = [400, 500, 600, 700, 800, 900, 1000, 1200, 1400]
    tails = []
    for thr in THRS:
        c  = integrate_tail_hist(y_mWW_sm, edges, thr)
        sp = integrate_tail_hist(y_mWW_p,  edges, thr)
        sm = integrate_tail_hist(y_mWW_m,  edges, thr)
        N_c  = args.lumi_fb * args.aeps * c  * PB_TO_FB
        N_sp = args.lumi_fb * args.aeps * sp * PB_TO_FB
        N_sm = args.lumi_fb * args.aeps * sm * PB_TO_FB
        tails.append({"thr_GeV":thr, "sigma_sm_pb":c, "sigma_p_pb":sp, "sigma_m_pb":sm,
                      "N_sm":N_c, "N_p":N_sp, "N_m":N_sm})
    out_summary["tail_sigma"] = tails

    if args.make_counting_limits:
        rows = []
        for thr in THRS:
            c  = integrate_tail_hist(y_mWW_sm, edges, thr)
            sp = integrate_tail_hist(y_mWW_p,  edges, thr)
            sm = integrate_tail_hist(y_mWW_m,  edges, thr)
            # σ(f) = c + A f + B f^2 inferred from ±f0
            A = (sp - sm)/(2.0*args.f0)
            B = (sp + sm - 2.0*c)/(2.0*args.f0*args.f0)
            f_lo, f_hi = interval_asimov_exact(c, A, B, args.lumi_fb, args.aeps)
            rows.append({"thr_GeV":thr, "A_pb_per_f":A, "B_pb_per_f2":B,
                         "f_lo_95CL":f_lo, "f_hi_95CL":f_hi})
        out_summary["counting_limits"] = rows

    # --- Shape likelihood
    if args.make_shape_limits:
        best = None
        for Wmin in np.arange(R_mWW[0], R_mWW[1]-1e-6, 50.0):
            α, β, γ, widths = build_shape_coeffs(edges, y_mWW_sm, y_mWW_p, y_mWW_m, args.f0, Wmin=Wmin)
            if α.size == 0: continue
            f_lo, f_hi = asimov_shape_interval(α, β, γ, widths, args.lumi_fb, args.aeps)
            width = f_hi - f_lo
            rec = {"Wmin_GeV": Wmin, "f_lo_95CL": f_lo, "f_hi_95CL": f_hi, "interval_width": width}
            if best is None or width < best["interval_width"]: best = rec
        out_summary["shape_best_interval"] = best if best else {}

    with open(os.path.join(args.outdir, "summary.json"), "w") as jf:
        json.dump(out_summary, jf, indent=2)


    # Console summary
    print("\n== Inputs ==")
    print(json.dumps(out_summary["inputs"], indent=2))
    if "counting_limits" in out_summary:
        print("\n== Counting limits (95% CL) ==")
        for r in out_summary["counting_limits"]:
            print(f"Wmin={r['thr_GeV']:>4.0f} GeV :  f in [{r['f_lo_95CL']:.5g}, {r['f_hi_95CL']:.5g}]")
    if "shape_best_interval" in out_summary and out_summary["shape_best_interval"]:
        b = out_summary["shape_best_interval"]
        print(f"\n== Shape best window ==\nWmin={b['Wmin_GeV']} GeV :  f in [{b['f_lo_95CL']:.5g}, {b['f_hi_95CL']:.5g}]")

if __name__ == "__main__":
    main()


