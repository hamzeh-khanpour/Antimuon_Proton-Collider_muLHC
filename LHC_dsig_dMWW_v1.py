#!/usr/bin/env python3
"""
LHC γγ→W+W− : dσ/dM_WW (SM vs EFT) with CMS-style overlay+ratio and counts/dsig modes.

- Finds W+ (PDG=24) and W- (PDG=-24), computes M_WW per event.
- Uses per-event weight XWGTUP when available; else σ_int / N from header (MG5 LO).
- Modes:
    * dsig   : plot dσ/dM_WW [pb/GeV]
    * counts : plot expected events per bin for a given --lumi-fb
- Cosmetics:
    * mplhep "CMS" style if available; otherwise fall back to matplotlib.
    * SM dashed vs EFT solid, heavier lines, step with last-plateau.
    * Ratio panel (EFT/SM) below.
    * On-plot annotation panel (σ_gen/σ_fid + EFT tag).
- Outputs: <out-prefix>.png, .pdf, .csv
"""

import argparse, gzip, math, re, csv
from typing import Dict, List, Optional, Tuple
import numpy as np
import warnings
warnings.filterwarnings(
    "ignore", message="This figure includes Axes that are not compatible with tight_layout")
import matplotlib.pyplot as plt



#import matplotlib as mpl
#mpl.rcParams['legend.fontsize'] = 30


# Try to use mplhep "CMS" style; fall back silently if not installed.
try:
    import mplhep as hep
    try:
        hep.style.use("CMS")
    except Exception:
        pass
except Exception:
    pass

# -----------------------------
# LHE header parsing (MG5-like)
# -----------------------------
RE_HEADER   = re.compile(r"<header>(.*?)</header>", re.DOTALL | re.MULTILINE)
RE_GENINFO  = re.compile(r"<MGGenerationInfo>(.*?)</MGGenerationInfo>", re.DOTALL)
RE_RUNCARD  = re.compile(r"<MGRunCard>\s*<!\[CDATA\[(.*?)\]\]>", re.DOTALL)

def _open(path: str):
    return gzip.open(path, "rt", encoding="utf-8", errors="ignore") if path.endswith(".gz") \
           else open(path, "rt", encoding="utf-8", errors="ignore")

def read_text(path: str) -> str:
    with _open(path) as f: return f.read()

def _find_float(pat: str, s: str) -> Optional[float]:
    m = re.search(pat, s, re.MULTILINE);  return float(m.group(1)) if m else None

def _find_int(pat: str, s: str) -> Optional[int]:
    m = re.search(pat, s, re.MULTILINE);  return int(m.group(1)) if m else None

def parse_header_meta(text: str) -> Dict[str, object]:
    mH = RE_HEADER.search(text)
    header = mH.group(1) if mH else text
    mG = RE_GENINFO.search(header); gen = mG.group(1) if mG else ""
    mR = RE_RUNCARD.search(header); run = mR.group(1) if mR else ""
    sigma_pb = _find_float(r"Integrated weight \(pb\)\s*:\s*([0-9Ee\+\-\.]+)", gen) \
               or _find_float(r"Integrated weight \(pb\)\s*:\s*([0-9Ee\+\-\.]+)", header)
    nevt = _find_int(r"Number of Events\s*:\s*([0-9]+)", gen) \
           or _find_int(r"Number of Events\s*:\s*([0-9]+)", header)
    return {"sigma_pb": sigma_pb, "nevents": nevt, "run_card": run}

# -----------------------------
# Events + weights
# -----------------------------
def parse_events(path: str):
    """Yield (w_ev, particles) where each particle dict has:
       id, status, px, py, pz, E, M
    """
    with _open(path) as f:
        in_ev = False; buf=[]
        for line in f:
            if "<event" in line:
                in_ev=True; buf=[]; continue
            if in_ev:
                if "</event" in line:
                    if not buf: in_ev=False; continue
                    hdr = buf[0].strip().split()
                    nup = int(hdr[0]) if hdr and hdr[0].strip("-").isdigit() else 0
                    w_ev = None
                    if len(hdr) >= 3:
                        try: w_ev = float(hdr[2])  # XWGTUP
                        except: w_ev = None
                    rows = buf[1:1+nup]
                    parts=[]
                    for r in rows:
                        c = r.strip().split()
                        if len(c) < 13: continue
                        try:
                            pid=int(c[0]); st=int(c[1])
                            px,py,pz,E,M = map(float, c[6:11])
                            parts.append({"id":pid,"status":st,"px":px,"py":py,"pz":pz,"E":E,"M":M})
                        except: continue
                    yield (w_ev, parts)
                    in_ev=False
                else:
                    buf.append(line)

# -----------------------------
# Physics helpers
# -----------------------------
def inv_mass4(p1, p2) -> float:
    E = p1["E"] + p2["E"]
    px= p1["px"]+ p2["px"]; py= p1["py"]+ p2["py"]; pz= p1["pz"]+ p2["pz"]
    m2 = max(E*E - (px*px+py*py+pz*pz), 0.0)
    return math.sqrt(m2)

def pick_Ws(parts):
    Ws = [p for p in parts if p["status"]==1 and abs(p["id"])==24]
    wp = next((p for p in Ws if p["id"]==+24), None)
    wm = next((p for p in Ws if p["id"]==-24), None)
    return wp, wm

# -----------------------------
# Histogram + conversions
# -----------------------------
def hist_weighted(values, weights, bins, lo, hi):
    values = np.asarray(values, float)
    w      = np.asarray(weights, float)
    H, edges = np.histogram(values, bins=bins, range=(lo,hi), weights=w)
    H2, _    = np.histogram(values, bins=bins, range=(lo,hi), weights=w*w)
    widths = np.diff(edges)
    # dsigma/dM = (sum w) / width
    y  = np.divide(H, widths, out=np.zeros_like(H, dtype=float), where=widths>0)
    dy = np.divide(np.sqrt(H2), widths, out=np.zeros_like(H2, dtype=float), where=widths>0)
    centers = 0.5*(edges[:-1]+edges[1:])
    return centers, edges, y, dy

def ratio_with_err(num, den, dnum, dden):
    R = np.divide(num, den, out=np.zeros_like(num, dtype=float), where=(den!=0))
    dR = np.zeros_like(R)
    mask = (num>0) & (den>0)
    dR[mask] = R[mask]*np.sqrt( (dnum[mask]/num[mask])**2 + (dden[mask]/den[mask])**2 )
    return R, dR

def convert_yield_mode(y_dsig, edges, mode: str, lumi_fb: float):
    """Convert dsig/dM to desired plotting units.
       - 'dsig'   : pb / GeV (unchanged)
       - 'counts' : events/bin = (dsig * width [pb]) * lumi [fb^-1]*1e3
    """
    if mode == "counts":
        widths = np.diff(edges)
        sigma_bin_pb = y_dsig * widths
        return sigma_bin_pb * (lumi_fb * 1e3)
    return y_dsig

# -------- step with last-plateau (CMS look)
def step_with_plateau(edges, y):
    x = np.r_[edges[:-1], edges[-1]]
    yy = np.r_[y, y[-1] if len(y) else 0.0]
    return x, yy

# -------- small annotation panel
def annotate_panel(ax,
                   xs_gen_sm: float, xs_gen_eft: float,
                   xs_fid_sm: float, xs_fid_eft: float,
                   eft_text: Optional[str] = r"$f_{M2}/\Lambda^4 = 1\ \mathrm{TeV}^{-4}$"):
    txt = (rf"SM:  $\sigma_{{gen}}={xs_gen_sm:.3g}\ \mathrm{{pb}}$,  " "\n"
#           rf"$\sigma_{{fid}}={xs_fid_sm:.3g}\ \mathrm{{pb}}$" "\n"
           rf"EFT: $\sigma_{{gen}}={xs_gen_eft:.3g}\ \mathrm{{pb}}$,  " "\n"
#           rf"$\sigma_{{fid}}={xs_fid_eft:.3g}\ \mathrm{{pb}}$" "\n"
           + (eft_text or ""))
    ax.text(0.04, 0.3, txt, transform=ax.transAxes, va="top", ha="left",
            fontsize=18, bbox=dict(fc=(1,1,1,0), ec=(1,1,1,1), linewidth=2))

def make_label(meta: Dict[str, object], tag: str) -> str:
    s = f"{tag}"
    if meta.get("sigma_pb") is not None and meta.get("nevents") is not None:
        s += f" (σ={meta['sigma_pb']:.6g} pb, N={meta['nevents']})"
    return s

# -----------------------------
# Plot (overlay + ratio, CMS look)
# -----------------------------
def plot_overlay_and_ratio(edges, y_sm, dy_sm, y_eft, dy_eft,
                           out_prefix: str, title: str,
                           mode: str, lumi_fb: float,
                           logy: bool,
                           sm_label: str, eft_label: str,
                           eft_text: Optional[str] = None):
    import matplotlib.gridspec as gridspec
    fig = plt.figure(figsize=(9.8,8.8))
    gs  = gridspec.GridSpec(2,1, height_ratios=[3,1], hspace=0.2)

    # top: overlay
    ax = fig.add_subplot(gs[0])
    y_sm_plot  = convert_yield_mode(y_sm,  edges, mode, lumi_fb)
    y_eft_plot = convert_yield_mode(y_eft, edges, mode, lumi_fb)

    x, y_sm_step  = step_with_plateau(edges, y_sm_plot)
    _, y_eft_step = step_with_plateau(edges, y_eft_plot)

    # Colors: rely on mpl default palette; enforce dashed SM vs solid EFT (CMS habit).
    ax.step(x, y_sm_step,  where="post", label=sm_label,  lw=2.8, ls="--")
    ax.step(x, y_eft_step, where="post", label=eft_label, lw=2.8, ls="-")

    ax.set_ylabel("Events" if mode=="counts" else r"d$\sigma$/d$M_{WW}$  [pb / GeV]")
    ax.set_title(title)
    if logy:
        ax.set_yscale("log")
    ax.grid(True, which="both", alpha=0.3)
    ax.legend(ncol=2, fontsize=10)

    # small info panel
    xs_gen_sm  = getattr(plot_overlay_and_ratio, "_xs_gen_sm", 0.0)
    xs_gen_eft = getattr(plot_overlay_and_ratio, "_xs_gen_eft", 0.0)
    xs_fid_sm  = getattr(plot_overlay_and_ratio, "_xs_fid_sm", xs_gen_sm)
    xs_fid_eft = getattr(plot_overlay_and_ratio, "_xs_fid_eft", xs_gen_eft)
    annotate_panel(ax, xs_gen_sm, xs_gen_eft, xs_fid_sm, xs_fid_eft, eft_text)

    # bottom: ratio (invariant under mode)
    axR = fig.add_subplot(gs[1], sharex=ax)
    R, dR = ratio_with_err(y_eft, y_sm, dy_eft, dy_sm)
    xR, R_step = step_with_plateau(edges, R)
    axR.step(xR, R_step, where="post", color="black", lw=2.0)
    axR.bar(0.5*(edges[:-1]+edges[1:]), 2*dR, bottom=R-dR, width=np.diff(edges),
            alpha=0.22, align="center", edgecolor="none")
    axR.set_xlabel(r"$M_{WW}$  [GeV]")
    axR.set_ylabel("EFT/SM")
    axR.grid(True, which="both", alpha=0.3)
    finiteR = np.where(np.isfinite(R), R, np.nan)
    top = np.nanmax(finiteR + dR) if np.isfinite(finiteR).any() else 2.0
    axR.set_ylim(0, max(1.8, 1.1*top))

    fig.tight_layout()
    for ext in ("png","pdf"):
        fig.savefig(f"{out_prefix}.{ext}")
    plt.close(fig)

    # CSV
    with open(f"{out_prefix}.csv", "w", newline="") as cf:
        w = csv.writer(cf)
        if mode == "counts":
            w.writerow(["bin_lo_GeV", "bin_hi_GeV", "SM_events", "EFT_events", "ratio", "ratio_stat"])
            SMc = convert_yield_mode(y_sm, edges, "counts", lumi_fb)
            EFTc= convert_yield_mode(y_eft, edges, "counts", lumi_fb)
            for i in range(len(y_sm)):
                w.writerow([f"{edges[i]:.6g}", f"{edges[i+1]:.6g}",
                            f"{SMc[i]:.6g}", f"{EFTc[i]:.6g}", f"{R[i]:.6g}", f"{dR[i]:.6g}"])
        else:
            w.writerow(["bin_lo_GeV", "bin_hi_GeV", "SM_dsig_pb_per_GeV", "EFT_dsig_pb_per_GeV", "ratio", "ratio_stat"])
            for i in range(len(y_sm)):
                w.writerow([f"{edges[i]:.6g}", f"{edges[i+1]:.6g}",
                            f"{y_sm[i]:.6g}",  f"{y_eft[i]:.6g}", f"{R[i]:.6g}", f"{dR[i]:.6g}"])

# -----------------------------
# Main
# -----------------------------
def main():
    ap = argparse.ArgumentParser(description="LHC γγ→W+W− : M_WW spectra (SM vs EFT) with CMS-style overlay+ratio.")
    ap.add_argument("sm_lhe",  help="SM LHE path")
    ap.add_argument("eft_lhe", help="EFT LHE path")

    # binning and range for M_WW (as requested)
    ap.add_argument("--bins",  type=int,   default=80, help="number of M_WW bins")
    ap.add_argument("--range", type=float, nargs=2, default=(160.0, 5000.0),
                    help="M_WW range [GeV], e.g. --range 160 6000")

    # modes & cosmetics
    ap.add_argument("--yield-mode", choices=["dsig","counts"], default="dsig",
                    help="Plot dσ/dM_WW (pb/GeV) or expected counts per bin (needs --lumi-fb).")
    ap.add_argument("--lumi-fb", type=float, default=100.0,
                    help="Integrated luminosity in fb^-1 (used only if --yield-mode counts).")
    ap.add_argument("--logy", action=argparse.BooleanOptionalAction, default=False,
                    help="Use log scale on Y axis.")
    ap.add_argument("--out-prefix", default="mww_compare_muLHC_SM_vs_EFT",
                    help="Output prefix for .png/.pdf/.csv")
    ap.add_argument("--title", default=r"LHC: $p(\gamma)\otimes p(\gamma)\to W^+W^-$",
                    help="Plot title.")
    ap.add_argument("--eft-text", default=r"$f_{M2}/\Lambda^4 = 1\ \mathrm{TeV}^{-4}$",
                    help="EFT tag to show in the info panel.")
    # NEW: choose per-event weight source (minimal change to fix normalization)
    ap.add_argument("--weight-source", choices=["auto","header","lhe"], default="auto",
                    help="Per-event weights: 'header' uses σ/N; 'lhe' uses XWGTUP; 'auto' decides from a small sample.")

    args = ap.parse_args()

    # Load headers
    txt_sm  = read_text(args.sm_lhe)
    txt_eft = read_text(args.eft_lhe)
    meta_sm  = parse_header_meta(txt_sm)
    meta_eft = parse_header_meta(txt_eft)

    # Fallback per-event weights if XWGTUP is absent
    def weight_norm(meta):
        sig = meta.get("sigma_pb") or 1.0
        N   = meta.get("nevents") or 1
        return sig/float(N)

    w_fallback_sm  = weight_norm(meta_sm)
    w_fallback_eft = weight_norm(meta_eft)

    # --- Minimal AUTO logic: inspect a small sample of XWGTUP and pick header/lhe
    def sample_median_abs_xwgtup(path, max_ev=200):
        vals = []
        for i, (w_ev, _parts) in enumerate(parse_events(path)):
            if w_ev is not None:
                vals.append(abs(w_ev))
            if i+1 >= max_ev:
                break
        if not vals:
            return None
        arr = np.asarray(vals, float)
        return float(np.median(arr))

    def decide_weight_mode(tag, path, w_fallback, req):
        if req in ("header","lhe"):
            print(f"[weights] {tag}: FORCED → {req.upper()}")
            return req
        med = sample_median_abs_xwgtup(path, max_ev=200)
        if med is None:
            print(f"[weights] {tag}: AUTO → HEADER (no XWGTUP found); using σ/N={w_fallback:g} pb/evt")
            return "header"
        ratio = (med / w_fallback) if w_fallback > 0 else float("inf")
        if 0.1 <= ratio <= 10.0:
            print(f"[weights] {tag}: AUTO → LHE (median|XWGTUP|={med:g}, σ/N={w_fallback:g}, ratio≈{ratio:g})")
            return "lhe"
        else:
            print(f"[weights] {tag}: AUTO → HEADER (median|XWGTUP|={med:g}, σ/N={w_fallback:g}, ratio≈{ratio:g})")
            return "header"

    mode_sm  = decide_weight_mode("SM",  args.sm_lhe,  w_fallback_sm,  args.weight_source)
    mode_eft = decide_weight_mode("EFT", args.eft_lhe, w_fallback_eft, args.weight_source)

    # Gather M_WW and weights (W+W- four-vectors)
    def loop_file(path, w_fallback, mode):
        Ms, wts = [], []
        for w_ev, parts in parse_events(path):
            if mode == "header":
                w = w_fallback
            elif mode == "lhe":
                w = w_ev if (w_ev is not None) else w_fallback
            else:
                w = w_fallback
            wp, wm = pick_Ws(parts)
            if (wp is None) or (wm is None):
                continue
            Ms.append(inv_mass4(wp, wm))
            wts.append(w)
        return Ms, wts

    Ms_sm,  w_sm  = loop_file(args.sm_lhe,  w_fallback_sm,  mode_sm)
    Ms_eft, w_eft = loop_file(args.eft_lhe, w_fallback_eft, mode_eft)

    # Histograms -> dσ/dM with stat errors
    lo, hi = float(args.range[0]), float(args.range[1])
    centers, edges, y_sm,  dy_sm  = hist_weighted(Ms_sm,  w_sm,  args.bins, lo, hi)
    _,      _,     y_eft, dy_eft = hist_weighted(Ms_eft, w_eft, args.bins, lo, hi)

    ## Labels incl. header σ and N (CMS style)
    #sm_label  = make_label(meta_sm,  "SM")
    #eft_label = make_label(meta_eft, "EFT")



    sm_label  = "SM"
    eft_label = "EFT"



    # Pass σ_gen/σ_fid to the plot function via function attributes (simple thread-through)
    plot_overlay_and_ratio._xs_gen_sm  = meta_sm.get("sigma_pb")  or 0.0
    plot_overlay_and_ratio._xs_gen_eft = meta_eft.get("sigma_pb") or 0.0
    plot_overlay_and_ratio._xs_fid_sm  = plot_overlay_and_ratio._xs_gen_sm   # no fid cuts here
    plot_overlay_and_ratio._xs_fid_eft = plot_overlay_and_ratio._xs_gen_eft

    # Draw & save
    plot_overlay_and_ratio(edges, y_sm, dy_sm, y_eft, dy_eft,
                           out_prefix=args.out_prefix, title=args.title,
                           mode=args.yield_mode, lumi_fb=args.lumi_fb,
                           logy=args.logy,
                           sm_label=sm_label, eft_label=eft_label,
                           eft_text=args.eft_text)

    # Console summary
    Ns = len(Ms_sm); Ne = len(Ms_eft)
    print(f"[LHC] Events with W+W-: SM={Ns}, EFT={Ne}")
    print(f"[LHC] Header σ: SM={meta_sm.get('sigma_pb')} pb ; EFT={meta_eft.get('sigma_pb')} pb")
    ratio = None
    try:
        num = float(meta_eft.get("sigma_pb")) if meta_eft.get("sigma_pb") is not None else None
        den = float(meta_sm.get("sigma_pb")) if meta_sm.get("sigma_pb") is not None else None
        if num is not None and den not in (None, 0.0):
            ratio = num/den
    except Exception:
        ratio = None
    if ratio is not None:
        print(f"[LHC] Header σ ratio (EFT/SM) = {ratio:.5f}")
    else:
        print("[LHC] Header σ ratio (EFT/SM) = n/a")

if __name__ == "__main__":
    main()
