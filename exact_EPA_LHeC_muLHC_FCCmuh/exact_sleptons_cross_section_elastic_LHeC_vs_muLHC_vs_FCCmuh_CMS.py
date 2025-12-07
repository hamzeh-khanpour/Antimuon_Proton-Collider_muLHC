#!/usr/bin/env python3
# Elastic γγ → \tilde{\ell}^+ \tilde{\ell}^- : LHeC vs μLHC vs FCC-μH  (W > W0)
# Styling follows your ττ script (CMS theme; dashed blue / solid orange / dotted red)

import numpy as np
import matplotlib.pyplot as plt
import mplhep as hep

hep.style.use("CMS")
# plt.style.use(hep.style.ROOT)


# ----------------------- Config -----------------------
# Slepton mass [GeV] (change here if needed)
m_slepton = 100.0


# Elastic photon–photon luminosity spectra (two columns: W[GeV], S_gg[1/GeV])
f_LHeC   = "Sgg_elastic_e_El50_Ep7000_q2lmax_8317_q2pmax_8317.txt"
f_muLHC  = "Sgg_elastic_mu_El500_Ep7000_q2lmax_8317_q2pmax_8317.txt"
f_FCCmuh = "FCC_muh_Sgg_elastic_mu_El500_Ep50000_q2lmax_8317_q2pmax_8317.txt"


# ----------------------- I/O helpers -----------------------
def load_sgg(fname):
    arr = np.loadtxt(fname, comments="#", unpack=False)
    W = arr[:, 0].astype(float)
    S = arr[:, 1].astype(float)
    idx = np.argsort(W)
    return W[idx], S[idx]

W_e,   S_e   = load_sgg(f_LHeC)
W_mu,  S_mu  = load_sgg(f_muLHC)
W_FCC, S_FCC = load_sgg(f_FCCmuh)


# ---------------- σ(γγ→\tilde{\ell}^+\tilde{\ell}^-) at LO (pb) ----------------
def cs_slepton_W(W, m=m_slepton):
    # Uses your original functional form but enforces the physical threshold W >= 2m
    alpha  = 1.0/137.0
    hbarc2 = 0.389  # (GeV^2·mb); ×1e9 below → pb
    W  = np.asarray(W, dtype=float)
    xs = np.zeros_like(W, dtype=float)

    mask = (W >= 2.0*m)
    if np.any(mask):
        beta = np.sqrt(1.0 - 4.0*m*m/(W[mask]*W[mask]))
        term = 2.0 - beta**2 - (1.0 - beta**4)/(2.0*beta) * np.log((1.0 + beta)/(1.0 - beta))
        xs[mask] = (2.0*np.pi*(alpha*alpha)*hbarc2) / (W[mask]*W[mask]) * beta * term * 1e9  # → pb
    return np.nan_to_num(xs, nan=0.0, posinf=0.0, neginf=0.0)


# ------------- Integrate Σ(W>W0) = ∫_{W0}^{Wmax} S(W) σ(W) dW (backward trapezoid) -------------
def integrate_sigma(W, S):
    W = np.asarray(W, float)
    S = np.asarray(S, float)
    idx = np.argsort(W)
    W, S = W[idx], S[idx]

    sig = cs_slepton_W(W)     # pb
    integrand = S * sig       # pb / GeV

    n = len(W)
    W0  = np.empty(n-1, float)
    Sig = np.empty(n-1, float)
    acc = 0.0
    for k in range(n-2, -1, -1):
        dW   = W[k+1] - W[k]
        trap = 0.5*(integrand[k] + integrand[k+1]) * dW
        acc += trap
        W0[k]  = W[k]
        Sig[k] = acc
    return W0, Sig

W0_e,   Sig_e   = integrate_sigma(W_e,   S_e)
W0_mu,  Sig_mu  = integrate_sigma(W_mu,  S_mu)
W0_FCC, Sig_FCC = integrate_sigma(W_FCC, S_FCC)

# ---------------- Common W0 grid ----------------
Wthr = 2.0*m_slepton
Wmin = max(Wthr, W0_e.min(), W0_mu.min(), W0_FCC.min(), 2.0*m_slepton)
Wmax = min(1000.0, W0_e.max(), W0_mu.max(), W0_FCC.max())
W0_common = np.logspace(np.log10(Wmin), np.log10(Wmax), 500)

Sig_e_i   = np.interp(W0_common, W0_e,   Sig_e)
Sig_mu_i  = np.interp(W0_common, W0_mu,  Sig_mu)
Sig_FCC_i = np.interp(W0_common, W0_FCC, Sig_FCC)

# ---------------- Save table ----------------
np.savetxt(
    "exact_sleptons_cross_section_elastic_LHeC_vs_muLHC_FCCmuh.txt",
    np.column_stack([W0_common, Sig_e_i, Sig_mu_i, Sig_FCC_i]),
    header="W0 [GeV]\tSigma_LHeC [pb]\tSigma_muLHC [pb]\tSigma_FCCmuh [pb]",
    fmt="%.8e", delimiter="\t"
)



# ---------------- Plot (ττ-style: dashed blue, solid orange, dotted red) ----------------
fig, ax = plt.subplots(figsize=(10.0, 12.0))
plt.subplots_adjust(left=0.15, right=0.95, bottom=0.12, top=0.95)

ax.set_xlim(Wmin, Wmax)
ymin = max(1e-6, min(Sig_e_i.min(), Sig_mu_i.min(), Sig_FCC_i.min()) * 0.5)
ymax = 1e-1 # max(Sig_e_i.max(), Sig_mu_i.max(), Sig_FCC_i.max()) * 2.0
ax.set_ylim(ymin, ymax)

# Colors to mirror your ττ palette
c_LHeC  = "#1f77b4"  # blue (dashed)
c_muLHC = "#ff7f0e"  # orange (solid)
c_FCC   = "#d62728"  # red (dotted)

ax.loglog(W0_common, Sig_e_i,
          label=r"LHeC ($e$–p), $E_e=50$ GeV, $E_p=7$ TeV",
          linestyle="--", linewidth=4, color=c_LHeC)
ax.loglog(W0_common, Sig_mu_i,
          label=r"$\mu$LHC ($\mu$–p), $E_\mu=500$ GeV, $E_p=7$ TeV",
          linestyle="solid", linewidth=4, color=c_muLHC)
ax.loglog(W0_common, Sig_FCC_i,
          label=r"FCC-$\mu$H ($\mu$–p), $E_\mu=500$ GeV, $E_p=50$ TeV",
          linestyle=":", linewidth=4, color=c_FCC)



ax.set_xlabel(r"$W_0$ [GeV]")
ax.set_ylabel(r"$\sigma(\gamma\gamma\to \tilde{\ell}^+\tilde{\ell}^-;\, W>W_0)$  [pb]")

ax.legend(title=r"Elastic ($Q^2_\ell<M_Z^2$ GeV$^2$, $Q^2_p<M_Z^2$ GeV$^2$)", loc="upper right")
ax.grid(True, which="both", linestyle="--", alpha=0.45)

plt.savefig("exact_sleptons_cross_section_elastic_LHeC_vs_muLHC_FCCmuh.pdf")
plt.savefig("exact_sleptons_cross_section_elastic_LHeC_vs_muLHC_FCCmuh.png", dpi=300)
plt.show()
