#!/usr/bin/env python3
# Compare integrated σ(γγ→W+W−; W>W0) using ELASTIC photon–photon luminosities
# μLHC (μ–p, Eμ=2000 GeV, Ep=7 TeV) vs μLHC (μ–p, Eμ=1000 GeV, Ep=7 TeV)
# Styling matches your WW plot: CMS, 8x9", margins, log–log, xlim(161,1000), ylim(1e-4,1e1).

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


# ---------------- γγ → W+W− Born σ(W) in pb ----------------
# PR364-style expression, guarded below threshold (W < 2 mW -> 0).
def cs_ww_W(W):
    W = np.asarray(W, dtype=float)
    mW = 80.379  # GeV
    alpha = 1.0/128.0
    hbarc2 = 0.389  # GeV^2 -> mb
    beta2 = 1.0 - (4.0*mW*mW)/(W*W)
    beta2 = np.where(beta2>0.0, beta2, 0.0)
    beta  = np.sqrt(beta2)

    # Avoid division by zero in the log term near threshold
    with np.errstate(divide='ignore', invalid='ignore'):
        term_log = np.where(beta>0.0, np.log((1.0+beta)/(1.0-beta)), 0.0)

    # σ = π α^2 / W^2 * β * [ -3 (1-β^4)/β ln((1+β)/(1-β)) + 2(22 - 9β^2 + 3β^4)/(1-β^2) ]
    pref  = np.pi * (alpha**2) * hbarc2 * 1e9  # -> pb
    denom = np.where(W>0.0, W*W, np.inf)

    # Protect (1-β^2) in denominator
    one_minus_b2 = np.where(1.0-beta2>0.0, 1.0-beta2, np.nan)

    bracket = (-3.0 * (1.0 - beta**4)/np.where(beta>0.0, beta, np.inf) * term_log
               + 2.0 * (22.0 - 9.0*beta2 + 3.0*beta**4) / one_minus_b2)

    sigma = pref * beta * bracket / denom
    # Below threshold -> 0
    sigma = np.where(W >= 2.0*mW, sigma, 0.0)
    # Clean any tiny NaNs at threshold
    sigma = np.nan_to_num(sigma, nan=0.0, posinf=0.0, neginf=0.0)
    return sigma  # pb

# ---------------- Integrate σ(W>W0) = ∫_{W0}^{Wmax} S(W) * σ_γγ→WW(W) dW ----------------
def integrate_sigma(W, S):
    W = np.asarray(W, float)
    S = np.asarray(S, float)
    i = np.argsort(W)
    W, S = W[i], S[i]
    sig = cs_ww_W(W)             # pb
    integrand = S * sig          # pb / GeV
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


# ---------------- Common W0 grid (follow your figure ranges) ----------------
Wmin = max(161.0, W0_e.min(), W0_mu.min())
Wmax = min(1000.0, W0_e.max(), W0_mu.max())
W0_common = np.logspace(np.log10(Wmin), np.log10(Wmax), 500)
Sig_e_i  = np.interp(W0_common, W0_e,  Sig_e)
Sig_mu_i = np.interp(W0_common, W0_mu, Sig_mu)

# ---------------- Save table ----------------
np.savetxt(
    "exact_ww_cross_section_elastic_muLHC5_vs_muLHC7_CMS.txt",
    np.column_stack([W0_common, Sig_e_i, Sig_mu_i]),
    header="W0 [GeV]\tSigma_muLHC@7.5 TeV [pb]\tSigma_muLHC@5.3 TeV [pb]",
    fmt="%.8e", delimiter="\t"
)


# ---------------- Plot (match your JHEP-like style) ----------------
fig, ax = plt.subplots(figsize=(10.0, 12.0))
plt.subplots_adjust(left=0.15, right=0.95, bottom=0.12, top=0.95)


ax.set_xlim(161.0, 1000.0)
ax.set_ylim(1.0e-3, 1.0e+1)


# Solid vs dashed, thick lines—consistent with your plots
ax.loglog(W0_common, Sig_e_i,
          label=r"$\mu$LHC ($\mu$–p), $E_\mu=2000$ GeV, $E_p=7$ TeV",
          linestyle="--", linewidth=4)
ax.loglog(W0_common, Sig_mu_i,
          label=r"$\mu$LHC ($\mu$–p), $E_\mu=1000$ GeV, $E_p=7$ TeV",
          linestyle="solid", linewidth=4)


ax.set_xlabel(r"$W_0$ [GeV]")
ax.set_ylabel(r"$\sigma(\gamma\gamma\to W^+W^-;\, W>W_0)$  [pb]")


# Legend title reflects the elastic caps embedded in your S_γγ files (Q^2_ℓ,p < M_Z^2 GeV^2)
ax.legend(title=r"Elastic ($Q^2_\ell<M_Z^2$ GeV$^2$, $Q^2_p<M_Z^2$ GeV$^2$)", loc="upper right")


ax.grid(True, which="both", linestyle="--", alpha=0.45)


plt.savefig("exact_ww_cross_section_elastic_muLHC5_vs_muLHC7_CMS.pdf")
plt.savefig("exact_ww_cross_section_elastic_muLHC5_vs_muLHC7_CMS.png", dpi=300)
plt.show()
