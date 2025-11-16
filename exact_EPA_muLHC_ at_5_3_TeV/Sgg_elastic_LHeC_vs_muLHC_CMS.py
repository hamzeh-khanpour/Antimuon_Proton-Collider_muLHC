#!/usr/bin/env python3
# Compare elastic S_γγ(W): LHeC (e–p) vs μLHC (μ–p), CMS style & exact axes.
# Inputs (present in the working directory):
#   - Sgg_elastic_e_El50_Ep7000_q2lmax_8317_q2pmax_8317.txt
#   - Sgg_elastic_mu_El1000_Ep7000_q2lmax_8317_q2pmax_8317.txt


import numpy as np
import matplotlib.pyplot as plt
import mplhep as hep


# ---------------- Style (as requested) ----------------
hep.style.use("CMS")
# plt.style.use(hep.style.ROOT)



# ---------------- Load data ----------------
# (Two-column text with a header line: W   Sgg)
f_e  = "Sgg_elastic_e_El50_Ep7000_q2lmax_8317_q2pmax_8317.txt"
f_mu = "Sgg_elastic_mu_El600_Ep7000_q2lmax_8317_q2pmax_8317.txt"

W_e,  S_e  = np.loadtxt(f_e,  unpack=True, comments="#")
W_mu, S_mu = np.loadtxt(f_mu, unpack=True, comments="#")



# ---------------- Plot ----------------
fig, ax = plt.subplots(figsize=(10.0, 12.0))
plt.subplots_adjust(left=0.15, right=0.95, bottom=0.12, top=0.95)



# Exact axis ranges / log scales
ax.set_xlim(10.0, 1000.0)
ax.set_ylim(1.0e-7, 1.0e-1)



# Curves (solid vs dashed for clear comparison)
ax.loglog(W_e,  S_e,  linestyle="--", linewidth=3.0,
          label=r"LHeC ($e$–p), $E_e=50$ GeV, $E_p=7$ TeV")
ax.loglog(W_mu, S_mu, linestyle="-",  linewidth=3.0,
          label=r"$\mu$LHC ($\mu$–p), $E_\mu=600$ GeV, $E_p=7$ TeV")



# Labels and legend (same wording/units as your JHEP-style plots)
ax.set_xlabel(r"$W$ [GeV]")
ax.set_ylabel(r"$S_{\gamma\gamma}$ [GeV$^{-1}$]")
ax.legend(loc="upper right", title=r"Elastic ($Q^2_\ell<M_Z^2$ GeV$^2$; $Q^2_p<M_Z^2$ GeV$^2$)")



# Optional: light grid to match your visual style (kept subtle)
ax.grid(True, which="both", linestyle="--", alpha=0.50)


# Save & show
plt.savefig("Sgg_elastic_LHeC_vs_muLHC_4TeV.pdf")
plt.savefig("Sgg_elastic_LHeC_vs_muLHC_4TeV.png", dpi=300)
plt.show()

