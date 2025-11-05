#!/usr/bin/env python3
# Compare integrated σ(γγ→ZZ; W>W0) using ELASTIC photon–photon luminosities
# μLHC (μ–p, Eμ=2000 GeV, Ep=7 TeV) vs μLHC (μ–p, Eμ=1000 GeV, Ep=7 TeV)
# Styling matches your WW plot: CMS, margins, log–log. ZZ threshold W_thr = 2 mZ ≈ 182.4 GeV.

import numpy as np
import matplotlib.pyplot as plt
import mplhep as hep
from pathlib import Path

hep.style.use("CMS")
# plt.style.use(hep.style.ROOT)

# ----------------------- Inputs -----------------------
f_LHeC  = "Sgg_elastic_mu_El2000_Ep7000_q2lmax_8317_q2pmax_8317.txt"
f_muLHC = "Sgg_elastic_mu_El1000_Ep7000_q2lmax_8317_q2pmax_8317.txt"


def load_sgg(fname):
    arr = np.loadtxt(fname, comments="#")
    W = arr[:,0].astype(float)
    S = arr[:,1].astype(float)
    i = np.argsort(W)
    return W[i], S[i]


W_e,  S_e  = load_sgg(f_LHeC)
W_mu, S_mu = load_sgg(f_muLHC)

# ---------------- γγ → ZZ σ(W) in pb (vectorized fit; 0 below threshold) ----------------
def cs_zz_W(W):
    W = np.asarray(W, dtype=float)
    mZ = 91.186  # GeV
    # Empirical loop-level fit used in your older ZZ script, expressed directly in pb
    A6 = 5.749069613832837e11
    A4 = 6.914037195922673e7
    A2 = 23.264122861948383
    num = 0.25786903395035327
    denom = (1.0 + A6/np.power(W,6) + A4/np.power(W,4) + A2/np.power(W,2))
    sigma = num / np.power(denom, 44.05927999125431)
    # Enforce threshold
    sigma = np.where(W >= 2.0*mZ, sigma, 0.0)
    # Clean numerical issues
    sigma = np.nan_to_num(sigma, nan=0.0, posinf=0.0, neginf=0.0)
    return sigma  # pb

# ---------------- Integrate σ(W>W0) = ∫_{W0}^{Wmax} S(W) * σ_γγ→ZZ(W) dW ----------------
def integrate_sigma(W, S):
    W = np.asarray(W, float)
    S = np.asarray(S, float)
    i = np.argsort(W)
    W, S = W[i], S[i]
    sig = cs_zz_W(W)            # pb
    integrand = S * sig         # pb / GeV
    n = len(W)
    W0  = np.empty(n-1, float)
    Sig = np.empty(n-1, float)
    acc = 0.0
    for k in range(n-2, -1, -1):
        dW   = W[k+1]-W[k]
        trap = 0.5*(integrand[k]+integrand[k+1])*dW
        acc += trap
        W0[k]  = W[k]
        Sig[k] = acc
    return W0, Sig

W0_e,  Sig_e  = integrate_sigma(W_e,  S_e)
W0_mu, Sig_mu = integrate_sigma(W_mu, S_mu)

# ---------------- Common W0 grid ----------------
mZ = 91.186
Wthr = 2.0*mZ
Wmin = max(Wthr, W0_e.min(), W0_mu.min(), 200.0)   # follow your previous ZZ x-range start
Wmax = min(1000.0, W0_e.max(), W0_mu.max())
W0_common = np.logspace(np.log10(Wmin), np.log10(Wmax), 500)
Sig_e_i  = np.interp(W0_common, W0_e,  Sig_e)
Sig_mu_i = np.interp(W0_common, W0_mu, Sig_mu)

# ---------------- Save table ----------------
np.savetxt(
    "exact_zz_cross_section_elastic_muLHC5_vs_muLHC7_CMS.txt",
    np.column_stack([W0_common, Sig_e_i, Sig_mu_i]),
    header="W0 [GeV]\tSigma_muLHC@5.3 TeV [pb]\tSigma_muLHC@7.5 TeV [pb]",
    fmt="%.8e", delimiter="\t"
)

# ---------------- Plot (match the WW script style) ----------------
fig, ax = plt.subplots(figsize=(10.0, 12.0))
plt.subplots_adjust(left=0.15, right=0.95, bottom=0.12, top=0.95)

ax.set_xlim(Wmin, Wmax)
# ZZ is loop-suppressed; choose a tighter y-range than WW.
ax.set_ylim(1.0e-6, 1.0e-2)

# Solid vs dashed, thick lines—consistent with your plots
ax.loglog(W0_common, Sig_e_i,
          label=r"$\mu$LHC ($\mu$–p), $E_\mu=2000$ GeV, $E_p=7$ TeV",
          linestyle="--", linewidth=4)
ax.loglog(W0_common, Sig_mu_i,
          label=r"$\mu$LHC ($\mu$–p), $E_\mu=1000$ GeV, $E_p=7$ TeV",
          linestyle="solid", linewidth=4)

ax.set_xlabel(r"$W_0$ [GeV]")
ax.set_ylabel(r"$\sigma(\gamma\gamma\to ZZ;\, W>W_0)$  [pb]")

# Legend title reflects the elastic caps embedded in your S_γγ files (Q^2_ℓ,p < M_Z^2 GeV^2)
ax.legend(title=r"Elastic ($Q^2_\ell<M_Z^2$ GeV$^2$, $Q^2_p<M_Z^2$ GeV$^2$)", loc="upper right")

ax.grid(True, which="both", linestyle="--", alpha=0.45)

plt.savefig("exact_zz_cross_section_elastic_muLHC5_vs_muLHC7_CMS.pdf")
plt.savefig("exact_zz_cross_section_elastic_muLHC5_vs_muLHC7_CMS.png", dpi=300)
plt.show()
