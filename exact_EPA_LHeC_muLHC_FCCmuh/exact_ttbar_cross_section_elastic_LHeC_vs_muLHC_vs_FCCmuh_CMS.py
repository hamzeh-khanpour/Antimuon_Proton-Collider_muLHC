#!/usr/bin/env python3
# Compare integrated σ(γγ → t t̄ ; W > W0) using ELASTIC photon–photon luminosities
# LHeC (e–p, Ee=50 GeV, Ep=7 TeV) vs μLHC (μ–p, Eμ=500 GeV, Ep=7 TeV) vs FCC-μH (μ–p, Eμ=500 GeV, Ep=50 TeV)
# Style & layout follow your ττ script (CMS style, 10x12", margins, log–log).  (See: exact_tautau_cross_section_elastic_LHeC_vs_muLHC_CMS.py)


import numpy as np
import matplotlib.pyplot as plt
import mplhep as hep


hep.style.use("CMS")
# plt.style.use(hep.style.ROOT)


# ----------------------- Inputs -----------------------
# Elastic photon–photon luminosity spectra (two columns: W[GeV], Sγγ[1/GeV])
f_LHeC   = "Sgg_elastic_e_El50_Ep7000_q2lmax_8317_q2pmax_8317.txt"
f_muLHC  = "Sgg_elastic_mu_El500_Ep7000_q2lmax_8317_q2pmax_8317.txt"
f_FCCmuh = "FCC_muh_Sgg_elastic_mu_El500_Ep50000_q2lmax_8317_q2pmax_8317.txt"

def load_sgg(fname):
    arr = np.loadtxt(fname, comments="#", unpack=False)
    W = arr[:, 0].astype(float)
    S = arr[:, 1].astype(float)
    idx = np.argsort(W)
    return W[idx], S[idx]

W_e,   S_e   = load_sgg(f_LHeC)
W_mu,  S_mu  = load_sgg(f_muLHC)
W_FCC, S_FCC = load_sgg(f_FCCmuh)



# ---------------- γγ → t t̄ Born σ(W) (pb) ----------------
# QED fermion-pair production at LO with color (Nc=3) and top charge Qf=2/3; threshold at W >= 2 m_t.
def cs_ttbar_W(W):
    alpha = 1.0/137.0
    hbarc2 = 0.389  # (GeV^2·mb); ×1e9 → pb at the end
    mt  = 172.5     # GeV
    Qf  = 2.0/3.0
    Nc  = 3.0

    W = np.asarray(W, dtype=float)
    xs = np.zeros_like(W, dtype=float)

    mask = (W >= 2.0*mt)
    beta = np.zeros_like(W, dtype=float)
    beta[mask] = np.sqrt(1.0 - 4.0*mt*mt/(W[mask]*W[mask]))

    # Physics Reports 364 (2002) Eq.62-like form:
    term = ( (3.0 - beta[mask]**4)/(2.0*beta[mask]) * np.log((1.0+beta[mask])/(1.0-beta[mask]))
             - 2.0 + beta[mask]**2 )
    pref = 4.0*np.pi*(alpha*alpha)*(Qf**4)*Nc*hbarc2
    xs[mask] = pref/(W[mask]*W[mask]) * beta[mask] * term * 1e9  # → pb

    # numerical safety
    xs = np.nan_to_num(xs, nan=0.0, posinf=0.0, neginf=0.0)
    return xs



# ---------------- Integrate σ(W>W0) = ∫_{W0}^{Wmax} S(W) * σγγ(W) dW ----------------
def integrate_sigma(W, S):
    """Return arrays (W0_grid, Sigma[W>W0]) using backward trapezoid over the input grid."""
    W = np.asarray(W, float)
    S = np.asarray(S, float)
    idx = np.argsort(W)
    W = W[idx]
    S = S[idx]

    sig = cs_ttbar_W(W)   # pb
    integrand = S * sig   # pb / GeV

    n = len(W)
    W0 = np.empty(n-1, dtype=float)
    Sigma = np.empty(n-1, dtype=float)
    acc = 0.0
    for i in range(n-2, -1, -1):   # integrate from high W downward
        dW   = W[i+1] - W[i]
        trap = 0.5*(integrand[i] + integrand[i+1]) * dW
        acc += trap
        W0[i]   = W[i]
        Sigma[i] = acc
    return W0, Sigma

W0_e,   Sig_e   = integrate_sigma(W_e,   S_e)
W0_mu,  Sig_mu  = integrate_sigma(W_mu,  S_mu)
W0_FCC, Sig_FCC = integrate_sigma(W_FCC, S_FCC)



# ---------------- Common W0 grid & interpolation ----------------
# Keep the ττ plot's look (10→1000 GeV) but enforce the tt̄ threshold region.
mt   = 172.5
Wthr = 2.0*mt
Wmin = max(Wthr, W0_e.min(), W0_mu.min(), W0_FCC.min(), 10.0)
Wmax = min(1000.0, W0_e.max(), W0_mu.max(), W0_FCC.max())
W0_common = np.logspace(np.log10(Wmin), np.log10(Wmax), 500)

Sig_e_i   = np.interp(W0_common, W0_e,   Sig_e)
Sig_mu_i  = np.interp(W0_common, W0_mu,  Sig_mu)
Sig_FCC_i = np.interp(W0_common, W0_FCC, Sig_FCC)

# ---------------- Save the numbers ----------------
np.savetxt(
    "exact_ttbar_cross_section_elastic_LHeC_vs_muLHC_FCCmuh.txt",
    np.column_stack([W0_common, Sig_e_i, Sig_mu_i, Sig_FCC_i]),
    header="W0 [GeV]\tSigma_LHeC [pb]\tSigma_muLHC [pb]\tSigma_FCCmuh [pb]",
    fmt="%.8e", delimiter="\t"
)


# ---------------- Plot (clone ττ styling) ----------------
fig, ax = plt.subplots(figsize=(10.0, 12.0))
plt.subplots_adjust(left=0.15, right=0.95, bottom=0.12, top=0.95)

ax.set_xlim(350.0, 1000.0)


# tt̄ is much smaller than ττ; choose a compact vertical band and keep everything visible.
ymin = max(1e-6, min(Sig_e_i.min(), Sig_mu_i.min(), Sig_FCC_i.min()) * 0.5)
ymax = max(Sig_e_i.max(), Sig_mu_i.max(), Sig_FCC_i.max()) * 2.0
ax.set_ylim(ymin, max(ymax, 1e-2))


# Lines & legend style match your ττ figure (dashed/solid/dotted, thick strokes)
ax.loglog(W0_common, Sig_e_i,
          label=r"LHeC ($e$–p), $E_e=50$ GeV, $E_p=7$ TeV",
          linestyle="--", linewidth=4)
ax.loglog(W0_common, Sig_mu_i,
          label=r"$\mu$LHC ($\mu$–p), $E_\mu=500$ GeV, $E_p=7$ TeV",
          linestyle="solid", linewidth=4)
ax.loglog(W0_common, Sig_FCC_i,
          label=r"FCC-$\mu$H ($\mu$–p), $E_\mu=500$ GeV, $E_p=50$ TeV",
          linestyle=":", linewidth=4)


ax.set_xlabel(r"$W_0$ [GeV]")
ax.set_ylabel(r"$\sigma(\gamma\gamma\to t\bar{t};\, W>W_0)$  [pb]")


# Legend title mirrors your Q^2-caps style; all beams are elastic with Q^2_ℓ,p < M_Z^2 GeV^2
ax.legend(title=r"Elastic ($Q^2_\ell<M_Z^2$ GeV$^2$, $Q^2_p<M_Z^2$ GeV$^2$)", loc="upper right")

# Subtle grid like your figure
ax.grid(True, which="both", linestyle="--", alpha=0.45)

plt.savefig("exact_ttbar_cross_section_elastic_LHeC_vs_muLHC_FCCmuh.pdf")
plt.savefig("exact_ttbar_cross_section_elastic_LHeC_vs_muLHC_FCCmuh.png", dpi=300)
plt.show()
