#!/usr/bin/env python3
# Elastic γγ luminosity S_γγ and σ(γγ→ττ) for lepton–proton (ℓ–p) with elastic proton EPA
# Generalized from LHeC (e–p) to arbitrary lepton ℓ ∈ {e, μ}, with compare mode for LHeC vs μLHC.
# Original authorship & physics content: Hamzeh Khanpour, Laurent Forthomme, Krzysztof Piotrzkowski (Nov 2024)
# Refactor by ChatGPT (Nov 2025) to support μ–p and CLI.

import numpy as np
import math
import matplotlib.pyplot as plt
from multiprocessing import Pool
import scipy.integrate as integrate
import argparse

# ------------------------- Constants -------------------------
ALPHA2PI = 7.2973525693e-3 / math.pi  # α/π
pmass = 0.938272081   # Proton mass [GeV]
# Lepton masses [GeV]
MASS_E = 0.000510999
MASS_MU = 0.1056583755

DEFAULT_Q2L_MAX = 10.0   # lepton-side Q^2 max [GeV^2]
DEFAULT_Q2P_MAX = 10.0   # proton-side Q^2 max [GeV^2]

# -------------------- Proton elastic form factors (dipole) --------------------
def G_E(Q2):
    return (1.0 + Q2 / 0.71) ** (-4)

def G_M(Q2):
    return 7.78 * G_E(Q2)

# ------------------------- Helper functions -------------------------
def qmin2(mass, y):
    """Minimum photon virtuality q^2_min = m^2 y^2 / (1 - y) (EPA)."""
    return mass * mass * y * y / (1.0 - y) if y < 1.0 else float("inf")

def compute_yp(W, Q2l, yl, El, Ep):
    """Solve W^2 = -Q_l^2 + y_l y_p s with s = 4 El Ep, for yp."""
    s = 4.0 * El * Ep
    denom = yl * s
    return (W * W + Q2l) / denom if denom != 0.0 else 0.0

def compute_jacobian(yl, yp, Q2l, El, Ep):
    """Jacobian ∂W/∂y_p with W^2 = -Q_l^2 + y_l y_p s."""
    s = 4.0 * El * Ep
    W2 = -Q2l + yl * yp * s
    if W2 <= 0.0:
        return 0.0
    W = math.sqrt(W2)
    return abs(yl * s / (2.0 * W)) if W != 0.0 else 0.0

# ------------- Photon fluxes (lepton pointlike; proton elastic) -------------
def flux_y_lepton(yl, lnQ2l, m_lepton, q2lmax):
    Q2l = math.exp(lnQ2l)
    if yl <= 0.0 or yl >= 1.0:
        return 0.0
    qmin2v = qmin2(m_lepton, yl)
    if qmin2v <= 0.0 or Q2l < qmin2v or Q2l > q2lmax:
        return 0.0
    # EPA (pointlike lepton)
    flux = ALPHA2PI / (yl * Q2l) * ((1.0 - yl) * (1.0 - qmin2v / Q2l) + 0.5 * yl * yl)
    return flux * Q2l  # dQ^2 = Q^2 d(ln Q^2)

def flux_y_proton(yp, q2pmax):
    if yp <= 0.0 or yp >= 1.0:
        return 0.0
    qmin2p = qmin2(pmass, yp)
    if qmin2p <= 0.0:
        return 0.0

    def lnQ2p_integrand(lnQ2p):
        Q2p = math.exp(lnQ2p)
        if Q2p < qmin2p or Q2p > q2pmax:
            return 0.0
        gE2 = G_E(Q2p)
        gM2 = G_M(Q2p)
        formE = (4.0 * pmass * pmass * gE2 + Q2p * gM2) / (4.0 * pmass * pmass + Q2p)
        formM = gM2
        flux = ALPHA2PI / (yp * Q2p) * ((1.0 - yp) * (1.0 - qmin2p / Q2p) * formE + 0.5 * yp * yp * formM)
        return flux * Q2p  # dQ^2 = Q^2 d(ln Q^2)

    result_lnQ2p, _ = integrate.quad(lnQ2p_integrand, math.log(qmin2p), math.log(q2pmax), epsrel=1e-4)
    return result_lnQ2p

# --------------------- S_γγ(W) via 2D integration ---------------------
def flux_el_yy_atW(W, lEbeam, pEbeam, m_lepton, q2lmax, q2pmax, nitn=(5, 10), neval=(1000, 10000)):
    s_cms = 4.0 * lEbeam * pEbeam
    yl_min, yl_max = W * W / s_cms, 1.0
    if yl_min >= 1.0:
        return 0.0

    def unit_integrand(u0, u1):
        yl = yl_min + u0 * (yl_max - yl_min)
        lnQ2l_min = math.log(qmin2(m_lepton, yl_min))
        lnQ2l_max = math.log(q2lmax)
        lnQ2l = lnQ2l_min + u1 * (lnQ2l_max - lnQ2l_min)
        Q2l = math.exp(lnQ2l)
        yp_val = compute_yp(W, Q2l, yl, lEbeam, pEbeam)
        if yp_val <= 0.0 or yp_val >= 1.0:
            return 0.0
        jac = compute_jacobian(yl, yp_val, Q2l, lEbeam, pEbeam)
        if jac == 0.0:
            return 0.0
        flux_p = flux_y_proton(yp_val, q2pmax)
        flux_l = flux_y_lepton(yl, lnQ2l, m_lepton, q2lmax)
        return flux_l * flux_p / jac * (yl_max - yl_min) * (lnQ2l_max - lnQ2l_min)

    # Try VEGAS; if unavailable, fallback to plain MC
    try:
        import vegas
        integ = vegas.Integrator([[0, 1], [0, 1]])
        integ(lambda x: unit_integrand(x[0], x[1]), nitn=nitn[0], neval=neval[0])  # warm-up
        res = integ(lambda x: unit_integrand(x[0], x[1]), nitn=nitn[1], neval=neval[1])
        return res.mean if res.Q > 0.1 else None
    except Exception:
        # Simple Monte Carlo fallback (deterministic seed)
        rng = np.random.default_rng(12345)
        Nwarm, Nfinal = neval
        def mc(N):
            u = rng.random((N, 2))
            vals = np.fromiter((unit_integrand(u[i, 0], u[i, 1]) for i in range(N)), float, count=N)
            return vals.mean()
        _ = mc(Nwarm)
        return mc(Nfinal)

# -------------------- γγ → ττ Born cross section --------------------
def cs_tautau_w_condition_Hamzeh(W):
    alpha = 1.0 / 137.0
    hbarc2 = 0.389  # to pb
    mtau = 1.77686
    if W < 2.0 * mtau:
        return 0.0
    beta = math.sqrt(1.0 - 4.0 * mtau * mtau / (W * W))
    xs = (4.0 * math.pi * alpha * alpha * hbarc2) / (W * W) * beta * (
        (3.0 - beta**4) / (2.0 * beta) * math.log((1.0 + beta) / (1.0 - beta)) - 2.0 + beta * beta
    ) * 1e9
    return xs

# -------------------- Integrated σ(W>W0) via 1D --------------------
def integrated_tau_tau_cross_section(W0, lEbeam, pEbeam, m_lepton, q2lmax, q2pmax):
    s_cms = 4.0 * lEbeam * pEbeam
    upper = math.sqrt(s_cms)
    if W0 >= upper:
        return 0.0

    def unit_integrand(u):
        W = W0 + u * (upper - W0)
        sig = cs_tautau_w_condition_Hamzeh(W)
        Sgg = flux_el_yy_atW(W, lEbeam, pEbeam, m_lepton, q2lmax, q2pmax)
        if Sgg is None:
            Sgg = 0.0
        return sig * Sgg * (upper - W0)

    try:
        import vegas
        integ = vegas.Integrator([[0, 1]])
        integ(unit_integrand, nitn=5, neval=1000)
        res = integ(unit_integrand, nitn=10, neval=10000)
        return res.mean if res.Q > 0.1 else 0.0
    except Exception:
        # MC fallback
        rng = np.random.default_rng(54321)
        Nwarm, Nfinal = 1000, 10000
        def mc(N):
            u = rng.random(N)
            vals = np.fromiter((unit_integrand(u[i]) for i in range(N)), float, count=N)
            return vals.mean()
        _ = mc(Nwarm)
        return mc(Nfinal)

# ------------------------------ CLI ------------------------------
parser = argparse.ArgumentParser(description="Elastic γγ luminosity and σ(γγ→ττ) for ℓ–p; compare LHeC vs μLHC.")
parser.add_argument("--lepton", choices=["e", "mu"], default="mu", help="Lepton type (e or mu).")
parser.add_argument("--El", type=float, default=1000.0, help="Lepton beam energy [GeV].")
parser.add_argument("--Ep", type=float, default=7000.0, help="Proton beam energy [GeV].")
parser.add_argument("--q2lmax", type=float, default=DEFAULT_Q2L_MAX, help="Max Q^2 on lepton side [GeV^2].")
parser.add_argument("--q2pmax", type=float, default=DEFAULT_Q2P_MAX, help="Max Q^2 on proton side [GeV^2].")
parser.add_argument("--compare", action="store_true", help="Also compute LHeC(e–p) overlay.")
parser.add_argument("--cores", type=int, default=4, help="Processes for pools.")
parser.add_argument("--label", type=str, default="μLHC (μ–p)", help="Label for plots.")
args = parser.parse_args()

lEbeam = args.El
pEbeam = args.Ep
q2lmax = args.q2lmax
q2pmax = args.q2pmax
num_cores = args.cores
m_lepton = MASS_E if args.lepton == "e" else MASS_MU
collider_label = args.label

# Grids
W_values = np.logspace(1.0, 3.0, 303)  # 10–1000 GeV
W0_range = np.arange(10.0, 1001.0, 1.0)
W0_value = 10.0

# -------------------------- Main computation --------------------------
if __name__ == "__main__":
    with Pool(processes=num_cores) as pool:
        luminosity_values = pool.starmap(
            flux_el_yy_atW,
            [(W, lEbeam, pEbeam, m_lepton, q2lmax, q2pmax) for W in W_values]
        )

    # Save S_γγ(W)
    fname_txt = f"Sgg_elastic_{args.lepton}_El{int(lEbeam)}_Ep{int(pEbeam)}_q2lmax_{int(q2lmax)}_q2pmax_{int(q2pmax)}.txt"
    with open(fname_txt, "w") as f:
        f.write("# W [GeV]    S_gg [GeV^-1]\n")
        for W, S in zip(W_values, luminosity_values):
            if S is not None and S != 0.0:
                f.write(f"{W:.6e}    {S:.6e}\n")

    # Single-point S_γγ and integrated σ
    luminosity_at_W10 = flux_el_yy_atW(W0_value, lEbeam, pEbeam, m_lepton, q2lmax, q2pmax)
    integ_sigma_W0 = integrated_tau_tau_cross_section(W0_value, lEbeam, pEbeam, m_lepton, q2lmax, q2pmax)

    # ---------- Plot S_γγ(W) ----------
    plt.figure(figsize=(10, 8))
    plt.xlim(10.0, 1000.0); plt.ylim(1.e-7, 1.e-1)
    plt.loglog(W_values, luminosity_values, linewidth=2, label='Elastic')
    plt.text(15, 5.e-6, f'q2lmax = {q2lmax:.1e} GeV^2', fontsize=14)
    plt.text(15, 2.e-6, f'q2pmax = {q2pmax:.1e} GeV^2', fontsize=14)
    plt.text(15, 9.e-7, f'm_l = {m_lepton:.6f} GeV', fontsize=14)
    if luminosity_at_W10 is not None:
        plt.text(15, 5.e-7, f'S_γγ(W=10 GeV) = {luminosity_at_W10:.2e} GeV$^{{-1}}$', fontsize=14)

    plt.xlabel(r"$W$ [GeV]", fontsize=18)
    plt.ylabel(r"$S_{\gamma\gamma}$ [GeV$^{-1}$]", fontsize=18)
    plt.title(f"Elastic S$_{{\gamma\gamma}}$ (ℓ–p, elastic p) — {collider_label}", fontsize=20)
    plt.grid(True, which="both", linestyle="--")
    plt.legend(fontsize=14)
    plt.savefig(f"Sgg_{args.lepton}_El{int(lEbeam)}_Ep{int(pEbeam)}_q2l{int(q2lmax)}_q2p{int(q2pmax)}.pdf")
    plt.savefig(f"Sgg_{args.lepton}_El{int(lEbeam)}_Ep{int(pEbeam)}_q2l{int(q2lmax)}_q2p{int(q2pmax)}.jpg")

    # ---------- Compute σ(W>W0) vs W0 ----------
    with Pool(processes=num_cores) as pool:
        cross_section_values = pool.starmap(
            integrated_tau_tau_cross_section,
            [(W0, lEbeam, pEbeam, m_lepton, q2lmax, q2pmax) for W0 in W0_range]
        )

    plt.figure(figsize=(10, 8))
    plt.xlim(10.0, 1000.0); plt.ylim(1.e-3, 1.e2)
    plt.loglog(W0_range, cross_section_values, linewidth=2, label='Elastic')
    plt.text(15, 2.e-2, f'q2lmax = {q2lmax:.1e} GeV^2', fontsize=14)
    plt.text(15, 1.e-2, f'q2pmax = {q2pmax:.1e} GeV^2', fontsize=14)
    plt.text(15, 7.e-3, f'm_l = {m_lepton:.6f} GeV', fontsize=14)
    plt.text(15, 5.e-3, f'σ(W>{W0_value:g} GeV) = {integ_sigma_W0:.2e} pb', fontsize=14)
    plt.xlabel(r"$W_0$ [GeV]", fontsize=18)
    plt.ylabel(r"$\sigma_{\tau^+\tau^-}$ (W > $W_0$) [pb]", fontsize=18)
    plt.title(f"Integrated σ(γγ→ττ) (W>W0), ℓ–p elastic p — {collider_label}", fontsize=20)
    plt.grid(True, which="both", linestyle="--")
    plt.legend(fontsize=14)

    fname_pdf = f"sigtau_{args.lepton}_El{int(lEbeam)}_Ep{int(pEbeam)}_q2l{int(q2lmax)}_q2p{int(q2pmax)}.pdf"
    fname_jpg = f"sigtau_{args.lepton}_El{int(lEbeam)}_Ep{int(pEbeam)}_q2l{int(q2lmax)}_q2p{int(q2pmax)}.jpg"
    plt.savefig(fname_pdf); plt.savefig(fname_jpg)

    # ---------- Optional overlay: μLHC(μ–p) vs LHeC(e–p) ----------
    if args.compare:
        El_e, Ep_e, m_e = 50.0, 7000.0, MASS_E
        label_e = "LHeC (e–p)"

        with Pool(processes=num_cores) as pool:
            Sgg_e = pool.starmap(
                flux_el_yy_atW, [(W, El_e, Ep_e, m_e, q2lmax, q2pmax) for W in W_values]
            )
        with Pool(processes=num_cores) as pool:
            sig_e = pool.starmap(
                integrated_tau_tau_cross_section, [(W0, El_e, Ep_e, m_e, q2lmax, q2pmax) for W0 in W0_range]
            )

        plt.figure(figsize=(10, 8))
        plt.xlim(10.0, 1000.0); plt.ylim(1.e-7, 1.e-1)
        plt.loglog(W_values, luminosity_values, linewidth=2, label=collider_label)
        plt.loglog(W_values, Sgg_e, linewidth=2, label=label_e)
        plt.xlabel(r"$W$ [GeV]"); plt.ylabel(r"$S_{\gamma\gamma}$ [GeV$^{-1}$]")
        plt.title("Elastic S$_{\\gamma\\gamma}$ overlay: μLHC(μ–p) vs LHeC(e–p)")
        plt.grid(True, which="both", linestyle="--"); plt.legend(fontsize=14)
        plt.savefig("Sgg_overlay_muLHC_vs_LHeC.pdf"); plt.savefig("Sgg_overlay_muLHC_vs_LHeC.jpg")

        plt.figure(figsize=(10, 8))
        plt.xlim(10.0, 1000.0); plt.ylim(1.e-3, 1.e2)
        plt.loglog(W0_range, cross_section_values, linewidth=2, label=collider_label)
        plt.loglog(W0_range, sig_e, linewidth=2, label=label_e)
        plt.xlabel(r"$W_0$ [GeV]"); plt.ylabel(r"$\sigma(\gamma\gamma\to\tau\tau)$ [pb]")
        plt.title("σ(γγ→ττ) overlay: μLHC(μ–p) vs LHeC(e–p)")
        plt.grid(True, which="both", linestyle="--"); plt.legend(fontsize=14)
        plt.savefig("sigtau_overlay_muLHC_vs_LHeC.pdf"); plt.savefig("sigtau_overlay_muLHC_vs_LHeC.jpg")
