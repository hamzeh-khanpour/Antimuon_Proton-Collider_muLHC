# =======================================================================
#     Hamzeh khanpour -- 2025 -- FCC_μh @ 10 TeV
#     FCC_μh @ 10 TeV
# =======================================================================


# --- ROOT.TLorentzVector shim (avoids Python3.12/ROOT cling segfault) ---
# Keeps the rest of the code structure intact by exposing ROOT.TLorentzVector.


import math
import numpy as np

class _TLorentzVectorShim:
    __slots__ = ("_px", "_py", "_pz", "_e")
    def __init__(self, px=0.0, py=0.0, pz=0.0, e=0.0):
        self._px, self._py, self._pz, self._e = float(px), float(py), float(pz), float(e)
    # ROOT-like setters/getters
    def SetPxPyPzE(self, px, py, pz, e): self._px, self._py, self._pz, self._e = float(px), float(py), float(pz), float(e)
    def Px(self): return self._px
    def Py(self): return self._py
    def Pz(self): return self._pz
    def E (self): return self._e
    # Kinematics
    def Pt(self): return math.hypot(self._px, self._py)
    def Phi(self): return math.atan2(self._py, self._px) if (self._px or self._py) else 0.0
    def Eta(self):
        p  = math.sqrt(self._px*self._px + self._py*self._py + self._pz*self._pz)
        if p == abs(self._pz):  # avoid div-by-zero in atanh
            return 0.0 if self._pz == 0.0 else (1e9 if self._pz > 0 else -1e9)
        # η = 0.5 ln((p+pz)/(p-pz))
        return 0.5 * math.log((p + self._pz) / max(p - self._pz, 1e-18))
    def M(self):
        m2 = self._e*self._e - (self._px*self._px + self._py*self._py + self._pz*self._pz)
        return math.sqrt(max(m2, 0.0))
    def DeltaR(self, other):
        dphi = self.Phi() - other.Phi()
        while dphi >  math.pi: dphi -= 2*math.pi
        while dphi < -math.pi: dphi += 2*math.pi
        deta = self.Eta() - other.Eta()
        return math.hypot(deta, dphi)
    # four-vector addition
    def __add__(self, other):
        return _TLorentzVectorShim(self._px + other._px, self._py + other._py, self._pz + other._pz, self._e + other._e)
    __radd__ = __add__

class _ROOTNamespace:
    pass



ROOT = _ROOTNamespace()
ROOT.TLorentzVector = _TLorentzVectorShim
# ------------------------------------------------------------------------

import matplotlib.pyplot as plt

# Matplotlib configuration for publication-quality plots
import mplhep as hep
hep.style.use("CMS")



# =======================================================================
# Function to parse the LHE file and extract observables
# =======================================================================
def parse_lhe_file(file_name):
    pt_leptons = []
    eta_leptons = []
    pt_leading_jet = []                 # Leading jet pT
    delta_r_values = []                 # ΔR(ℓ, leading jet)
    missing_transverse_energy = []      # MET
    centrality_values = []              # Lepton centrality (your def)
    exp_centrality_values = []          # Exponential centrality
    jet_centrality_values = []          # Jet centrality
    delta_eta_jj_values = []            # η(j1) − η(j2)
    m_w_hadronic_values = []            # M_W^jj
    m_w_leptonic_values = []            # M_W^ℓν
    m_w_hadronic_leptonic_values = []   # M_WW^reco

    with open(file_name, "r") as file:
        in_event = False

        for line in file:
            line = line.strip()

            if "<event>" in line:
                in_event = True
                jets = []
                leptons = []
                neutrinos = []
                # ensure defined for this event
                w_hadronic = None
                w_leptonic = None
                continue

            if "</event>" in line:
                in_event = False

                # MET from ν
                met_x = sum(nu.Px() for nu in neutrinos)
                met_y = sum(nu.Py() for nu in neutrinos)
                met = math.hypot(met_x, met_y)
                missing_transverse_energy.append(met)

                # Leading jet & ΔR with each lepton
                if jets:
                    leading_jet = max(jets, key=lambda j: j.Pt())
                    pt_leading_jet.append(leading_jet.Pt())
                    for lepton in leptons:
                        delta_r_values.append(lepton.DeltaR(leading_jet))

                # lepton “centrality” (your definition in original code)
                for lepton in leptons:
                    centrality_values.append(lepton.Eta())  # placeholder for your metric
                    exp_centrality_values.append(math.exp(-lepton.Eta()) / math.cosh(lepton.Eta()))

                # jet centrality and Δη(jj), hadronic W mass
                if len(jets) >= 2:
                    jet_centrality = abs(jets[0].Eta() + jets[1].Eta()) / 2.0
                    jet_centrality_values.append(jet_centrality)
                    delta_eta_jj_values.append(jets[0].Eta() - jets[1].Eta())
                    w_hadronic = jets[0] + jets[1]
                    m_w_hadronic_values.append(w_hadronic.M())

                # leptonic W mass if ℓ + ν present
                if len(leptons) == 1 and len(neutrinos) > 0:
                    neutrino_vec = sum(neutrinos, ROOT.TLorentzVector())
                    w_leptonic = leptons[0] + neutrino_vec
                    m_w_leptonic_values.append(w_leptonic.M())

                # M_WW^reco
                if (w_hadronic is not None) and (w_leptonic is not None):
                    ww = w_hadronic + w_leptonic
                    m_w_hadronic_leptonic_values.append(ww.M())
                continue

            if in_event:
                # Skip non-numeric lines
                if not line or (not line[0].isdigit() and line[0] != "-"):
                    continue

                parts = line.split()
                if len(parts) < 10:
                    continue

                pdg_id = int(parts[0])
                status = int(parts[1])
                px = float(parts[6]); py = float(parts[7]); pz = float(parts[8]); energy = float(parts[9])

                # leptons
                if abs(pdg_id) in [11, 13, 15]:
                    lepton = ROOT.TLorentzVector(); lepton.SetPxPyPzE(px, py, pz, energy)
                    leptons.append(lepton)
                    pt_leptons.append(lepton.Pt()); eta_leptons.append(lepton.Eta())

                # jets (final-state, not γ/ν/leptons)
                if (abs(pdg_id) not in [11, 12, 13, 14, 15, 16, 22]) and (status == 1):
                    jet = ROOT.TLorentzVector(); jet.SetPxPyPzE(px, py, pz, energy)
                    jets.append(jet)

                # neutrinos
                if abs(pdg_id) in [12, 14, 16]:
                    nu = ROOT.TLorentzVector(); nu.SetPxPyPzE(px, py, pz, energy)
                    neutrinos.append(nu)

    return (pt_leptons, eta_leptons, pt_leading_jet, delta_r_values,
            missing_transverse_energy, centrality_values, exp_centrality_values,
            jet_centrality_values, delta_eta_jj_values,
            m_w_hadronic_values, m_w_leptonic_values, m_w_hadronic_leptonic_values)



# =======================================================================

plt.subplots_adjust(left=0.15, right=0.95, bottom=0.12, top=0.95)



# --- LHE file paths (unchanged)
signal_file_0 = "/home/hamzeh-khanpour/MG5_aMC_v3_6_6/FCC_muh_EFT_aa_ww_semi_leptonic/Events/run_01/FCC_muh_EFT_aa_ww_semi_leptonic.lhe"
signal_file_2 = "/home/hamzeh-khanpour/MG5_aMC_v3_6_6/FCC_muh_EFT_aa_ww_semi_leptonic/Events/run_02/FCC_muh_EFT_aa_ww_semi_leptonic.lhe"
background_file = "/home/hamzeh-khanpour/MG5_aMC_v3_6_6/FCC_muh_SM_aa_ww_semi_leptonic/Events/run_01/FCC_muh_SM_aa_ww_semi_leptonic.lhe"



# --- Parse LHE
(pt_leptons_signal_0, eta_leptons_signal_0, pt_leading_jet_signal_0, delta_r_signal_0,
 met_signal_0, centrality_signal_0, exp_centrality_signal_0, jet_centrality_signal_0, delta_eta_jj_signal_0,
 m_w_hadronic_signal_0, m_w_leptonic_signal_0, m_w_hadronic_leptonic_signal_0) = parse_lhe_file(signal_file_0)

(pt_leptons_signal_2, eta_leptons_signal_2, pt_leading_jet_signal_2, delta_r_signal_2,
 met_signal_2, centrality_signal_2, exp_centrality_signal_2, jet_centrality_signal_2, delta_eta_jj_signal_2,
 m_w_hadronic_signal_2, m_w_leptonic_signal_2, m_w_hadronic_leptonic_signal_2) = parse_lhe_file(signal_file_2)

(pt_leptons_background, eta_leptons_background, pt_leading_jet_background, delta_r_background,
 met_background, centrality_background, exp_centrality_background, jet_centrality_background, delta_eta_jj_background,
 m_w_hadronic_background, m_w_leptonic_background, m_w_hadronic_leptonic_background) = parse_lhe_file(background_file)



# =======================================================================

# Parameters for differential cross-sections (unchanged)
signal_cross_section_0   = 0.157532   # pb (FM2 = +0.1 TeV^-4)
signal_cross_section_2   = 0.157557   # pb (FM2 = -0.1 TeV^-4)
background_cross_section = 0.155338   # pb



num_bins = 40
pt_range_lepton = (0, 500)
pt_range_jet    = (0, 500)
eta_range       = (-10, 10)
delta_r_range   = (0, 10)
met_range       = (1, 500)
centrality_range      = (-10, 10)
exp_centrality_range  = (0, 2)
jet_centrality_range  = (0, 6)
delta_eta_jj_range    = (-10, 10)
m_w_hadronic_range    = (1, 140)
m_w_leptonic_range    = (1, 140)
m_w_hadronic_leptonic_range = (160, 2600)



# Bin widths
bin_width_pt_lepton       = (pt_range_lepton[1] - pt_range_lepton[0]) / num_bins
bin_width_pt_jet          = (pt_range_jet[1]    - pt_range_jet[0])    / num_bins
bin_width_eta             = (eta_range[1]       - eta_range[0])       / num_bins
bin_width_delta_r         = (delta_r_range[1]   - delta_r_range[0])   / num_bins
bin_width_met             = (met_range[1]       - met_range[0])       / num_bins
bin_width_centrality      = (centrality_range[1]     - centrality_range[0])     / num_bins
bin_width_exp_centrality  = (exp_centrality_range[1] - exp_centrality_range[0]) / num_bins
bin_width_jet_centrality  = (jet_centrality_range[1] - jet_centrality_range[0]) / num_bins
bin_width_delta_eta_jj    = (delta_eta_jj_range[1]   - delta_eta_jj_range[0])   / num_bins
bin_width_m_w_hadronic    = (m_w_hadronic_range[1]   - m_w_hadronic_range[0])   / num_bins
bin_width_m_w_leptonic    = (m_w_leptonic_range[1]   - m_w_leptonic_range[0])   / num_bins
bin_width_m_w_had_lep     = (m_w_hadronic_leptonic_range[1] - m_w_hadronic_leptonic_range[0]) / num_bins



# =======================================================================
# Helper for differential spectra
# =======================================================================
def _calc_hist(data, data_range):
    hist, edges = np.histogram(data, bins=num_bins, range=data_range)
    centers = 0.5*(edges[:-1] + edges[1:])
    return centers, hist, (edges[1]-edges[0])

def calculate_dsigma(data, cross_section, bin_width, data_range):
    centers, counts, _ = _calc_hist(data, data_range)
    if len(data) == 0:
        return centers, np.zeros_like(centers, dtype=float)
    # density (pb/GeV): normalize by entries, scale by σ_total, divide by Δbin
    dsigma = (counts / max(len(data), 1)) * (cross_section / bin_width)
    return centers, dsigma



# =======================================================================
# Build all differential distributions (structure unchanged)
# =======================================================================

# Lepton pT
pt_bins_signal_0, dsigma_signal_pt_0 = calculate_dsigma(pt_leptons_signal_0, signal_cross_section_0, bin_width_pt_lepton, pt_range_lepton)
pt_bins_signal_2, dsigma_signal_pt_2 = calculate_dsigma(pt_leptons_signal_2, signal_cross_section_2, bin_width_pt_lepton, pt_range_lepton)
pt_bins_background, dsigma_background_pt = calculate_dsigma(pt_leptons_background, background_cross_section, bin_width_pt_lepton, pt_range_lepton)


# Lepton η
eta_bins_signal_0, dsigma_signal_eta_0 = calculate_dsigma(eta_leptons_signal_0, signal_cross_section_0, bin_width_eta, eta_range)
eta_bins_signal_2, dsigma_signal_eta_2 = calculate_dsigma(eta_leptons_signal_2, signal_cross_section_2, bin_width_eta, eta_range)
eta_bins_background, dsigma_background_eta = calculate_dsigma(eta_leptons_background, background_cross_section, bin_width_eta, eta_range)

# Leading jet pT
pt_jet_bins_signal_0, dsigma_signal_jet_pt_0 = calculate_dsigma(pt_leading_jet_signal_0, signal_cross_section_0, bin_width_pt_jet, pt_range_jet)
pt_jet_bins_signal_2, dsigma_signal_jet_pt_2 = calculate_dsigma(pt_leading_jet_signal_2, signal_cross_section_2, bin_width_pt_jet, pt_range_jet)
pt_jet_bins_background, dsigma_background_jet_pt = calculate_dsigma(pt_leading_jet_background, background_cross_section, bin_width_pt_jet, pt_range_jet)

# ΔR(ℓ, j_lead)
delta_r_bins_signal_0, dsigma_signal_delta_r_0 = calculate_dsigma(delta_r_signal_0, signal_cross_section_0, bin_width_delta_r, delta_r_range)
delta_r_bins_signal_2, dsigma_signal_delta_r_2 = calculate_dsigma(delta_r_signal_2, signal_cross_section_2, bin_width_delta_r, delta_r_range)
delta_r_bins_background, dsigma_background_delta_r = calculate_dsigma(delta_r_background, background_cross_section, bin_width_delta_r, delta_r_range)

# MET
met_bins_signal_0, dsigma_signal_met_0 = calculate_dsigma(met_signal_0, signal_cross_section_0, bin_width_met, met_range)
met_bins_signal_2, dsigma_signal_met_2 = calculate_dsigma(met_signal_2, signal_cross_section_2, bin_width_met, met_range)
met_bins_background, dsigma_background_met = calculate_dsigma(met_background, background_cross_section, bin_width_met, met_range)

# Centralities / Δη(jj)
centrality_bins_signal_0, dsigma_signal_centrality_0 = calculate_dsigma(centrality_signal_0, signal_cross_section_0, bin_width_centrality, centrality_range)
centrality_bins_signal_2, dsigma_signal_centrality_2 = calculate_dsigma(centrality_signal_2, signal_cross_section_2, bin_width_centrality, centrality_range)
centrality_bins_background, dsigma_background_centrality = calculate_dsigma(centrality_background, background_cross_section, bin_width_centrality, centrality_range)

exp_centrality_bins_signal_0, dsigma_signal_exp_centrality_0 = calculate_dsigma(exp_centrality_signal_0, signal_cross_section_0, bin_width_exp_centrality, exp_centrality_range)
exp_centrality_bins_signal_2, dsigma_signal_exp_centrality_2 = calculate_dsigma(exp_centrality_signal_2, signal_cross_section_2, bin_width_exp_centrality, exp_centrality_range)
exp_centrality_bins_background, dsigma_background_exp_centrality = calculate_dsigma(exp_centrality_background, background_cross_section, bin_width_exp_centrality, exp_centrality_range)

jet_centrality_bins_signal_0, dsigma_signal_jet_centrality_0 = calculate_dsigma(jet_centrality_signal_0, signal_cross_section_0, bin_width_jet_centrality, jet_centrality_range)
jet_centrality_bins_signal_2, dsigma_signal_jet_centrality_2 = calculate_dsigma(jet_centrality_signal_2, signal_cross_section_2, bin_width_jet_centrality, jet_centrality_range)
jet_centrality_bins_background, dsigma_background_jet_centrality = calculate_dsigma(jet_centrality_background, background_cross_section, bin_width_jet_centrality, jet_centrality_range)

delta_eta_jj_bins_signal_0, dsigma_signal_delta_eta_jj_0 = calculate_dsigma(delta_eta_jj_signal_0, signal_cross_section_0, bin_width_delta_eta_jj, delta_eta_jj_range)
delta_eta_jj_bins_signal_2, dsigma_signal_delta_eta_jj_2 = calculate_dsigma(delta_eta_jj_signal_2, signal_cross_section_2, bin_width_delta_eta_jj, delta_eta_jj_range)
delta_eta_jj_bins_background, dsigma_background_delta_eta_jj = calculate_dsigma(delta_eta_jj_background, background_cross_section, bin_width_delta_eta_jj, delta_eta_jj_range)

# W masses
m_w_hadronic_bins_signal_0, dsigma_signal_m_w_hadronic_0 = calculate_dsigma(m_w_hadronic_signal_0, signal_cross_section_0, bin_width_m_w_hadronic, m_w_hadronic_range)
m_w_hadronic_bins_signal_2, dsigma_signal_m_w_hadronic_2 = calculate_dsigma(m_w_hadronic_signal_2, signal_cross_section_2, bin_width_m_w_hadronic, m_w_hadronic_range)
m_w_hadronic_bins_background, dsigma_background_m_w_hadronic = calculate_dsigma(m_w_hadronic_background, background_cross_section, bin_width_m_w_hadronic, m_w_hadronic_range)

m_w_leptonic_bins_signal_0, dsigma_signal_m_w_leptonic_0 = calculate_dsigma(m_w_leptonic_signal_0, signal_cross_section_0, bin_width_m_w_leptonic, m_w_leptonic_range)
m_w_leptonic_bins_signal_2, dsigma_signal_m_w_leptonic_2 = calculate_dsigma(m_w_leptonic_signal_2, signal_cross_section_2, bin_width_m_w_leptonic, m_w_leptonic_range)
m_w_leptonic_bins_background, dsigma_background_m_w_leptonic = calculate_dsigma(m_w_leptonic_background, background_cross_section, bin_width_m_w_leptonic, m_w_leptonic_range)

# Reco M_WW
m_w_hadronic_leptonic_bins_signal_0, dsigma_signal_m_w_hadronic_leptonic_0 = calculate_dsigma(m_w_hadronic_leptonic_signal_0, signal_cross_section_0, bin_width_m_w_had_lep, m_w_hadronic_leptonic_range)
m_w_hadronic_leptonic_bins_signal_2, dsigma_signal_m_w_hadronic_leptonic_2 = calculate_dsigma(m_w_hadronic_leptonic_signal_2, signal_cross_section_2, bin_width_m_w_had_lep, m_w_hadronic_leptonic_range)
m_w_hadronic_leptonic_bins_background, dsigma_background_m_w_hadronic_leptonic = calculate_dsigma(m_w_hadronic_leptonic_background, background_cross_section, bin_width_m_w_had_lep, m_w_hadronic_leptonic_range)



# =======================================================================
# Example plots (labels made raw r"..." to avoid \L warnings)
# =======================================================================

# Lepton pT
plt.step(pt_bins_signal_0, dsigma_signal_pt_0, where="mid", alpha=0.7, label=r"FCC_μh@10 TeV : Signal ($w^+ w^-$) [$f_{M_2}/\Lambda^4=+0.1$]", linewidth=3)
plt.step(pt_bins_signal_2, dsigma_signal_pt_2, where="mid", alpha=0.7, label=r"FCC_μh@10 TeV : Signal ($w^+ w^-$) [$f_{M_2}/\Lambda^4=-0.1$]", linewidth=3)
plt.step(pt_bins_background, dsigma_background_pt, where="mid", alpha=0.7, label=r"FCC_μh@10 TeV : SM background ($w^+ w^-$)", linewidth=3)
plt.xlabel(r"$p_T^{\ell} \ \mathrm{[GeV]}$")
plt.ylabel(r"$\frac{d\sigma}{dp_T^{\ell}} \ \mathrm{[pb/GeV]}$")
plt.title(r"$e^- p \to e^- w^+ w^- p \to e^- j j \ell \nu_{\ell} p$ : FCC_μh@10 TeV", fontsize=24)
plt.yscale("log"); plt.legend(); plt.grid(True, linestyle="--", alpha=0.6); plt.tight_layout(); plt.savefig("differential_cross_section_pt_lepton_FCC_μh.pdf", dpi=600)
plt.show()





# Eta
plt.step(eta_bins_signal_0, dsigma_signal_eta_0, where="mid", alpha=0.7, label=r"FCC_μh@10 TeV : Signal ($w^+ w^-$) [$f_{M_2}/\Lambda^4=+0.1$]", linewidth=3)
plt.step(eta_bins_signal_2, dsigma_signal_eta_2, where="mid", alpha=0.7, label=r"FCC_μh@10 TeV : Signal ($w^+ w^-$) [$f_{M_2}/\Lambda^4=-0.1$]", linewidth=3)
plt.step(eta_bins_background, dsigma_background_eta, where="mid", alpha=0.7, label=r"FCC_μh@10 TeV : SM background ($w^+ w^-$)", linewidth=3)
plt.xlabel(r"$\eta^{\ell}$"); plt.ylabel(r"$\frac{d\sigma}{d\eta^{\ell}} \ \mathrm{[pb]}$")
plt.yscale("log"); plt.legend(); plt.grid(True, linestyle="--", alpha=0.6); plt.tight_layout(); plt.show()





# Leading jet pT
plt.step(pt_jet_bins_signal_0, dsigma_signal_jet_pt_0, where="mid", alpha=0.7, label=r"FCC_μh@10 TeV : Signal ($w^+ w^-$) [$f_{M_2}/\Lambda^4=+0.1$]", linewidth=3)
plt.step(pt_jet_bins_signal_2, dsigma_signal_jet_pt_2, where="mid", alpha=0.7, label=r"FCC_μh@10 TeV : Signal ($w^+ w^-$) [$f_{M_2}/\Lambda^4=-0.1$]", linewidth=3)
plt.step(pt_jet_bins_background, dsigma_background_jet_pt, where="mid", alpha=0.7, label=r"FCC_μh@10 TeV : SM background ($w^+ w^-$)", linewidth=3)
plt.xlabel(r"$p_T^{\mathrm{leading~jet}} \ \mathrm{[GeV]}$"); plt.ylabel(r"$\frac{d\sigma}{dp_T^{\mathrm{leading~jet}}} \ \mathrm{[pb/GeV]}$")
plt.title(r"$e^- p \to e^- w^+ w^- p \to e^- j j \ell \nu_{\ell} p$ : FCC_μh@10 TeV", fontsize=24)
plt.yscale("log"); plt.legend(); plt.grid(True, linestyle="--", alpha=0.6); plt.tight_layout(); plt.savefig("differential_cross_section_leading_jet_pt_FCC_μh.pdf", dpi=600)
plt.show()





# ΔR
plt.step(delta_r_bins_signal_0, dsigma_signal_delta_r_0, where="mid", alpha=0.7, label=r"FCC_μh@10 TeV : Signal ($w^+ w^-$) [$f_{M_2}/\Lambda^4+0.1$]", linewidth=3)
plt.step(delta_r_bins_signal_2, dsigma_signal_delta_r_2, where="mid", alpha=0.7, label=r"FCC_μh@10 TeV : Signal ($w^+ w^-$) [$f_{M_2}/\Lambda^4=-0.1$]", linewidth=3)
plt.step(delta_r_bins_background, dsigma_background_delta_r, where="mid", alpha=0.7, label=r"FCC_μh@10 TeV : SM background ($w^+ w^-$)", linewidth=3)
plt.xlabel(r"$\Delta R(\ell, j_{\mathrm{lead}})$"); plt.ylabel(r"$\frac{d\sigma}{d\Delta R} \ \mathrm{[pb]}$")
plt.title(r"$e^- p \to e^- w^+ w^- p \to e^- j j \ell \nu_{\ell} p$ : FCC_μh@10 TeV", fontsize=24)
plt.legend(); plt.grid(True, linestyle="--", alpha=0.6); plt.tight_layout(); plt.show()



# Reco M_WW (differential)
plt.step(m_w_hadronic_leptonic_bins_signal_0, dsigma_signal_m_w_hadronic_leptonic_0, where="mid", alpha=0.7, label=r"FCC_μh@10 TeV : Signal ($w^+ w^-$) [$f_{M_2}/\Lambda^4=+0.1$]", linewidth=3)
plt.step(m_w_hadronic_leptonic_bins_signal_2, dsigma_signal_m_w_hadronic_leptonic_2, where="mid", alpha=0.7, label=r"FCC_μh@10 TeV : Signal ($w^+ w^-$) [$f_{M_2}/\Lambda^4=-0.1$]", linewidth=3)
plt.step(m_w_hadronic_leptonic_bins_background, dsigma_background_m_w_hadronic_leptonic, where="mid", alpha=0.7, label=r"FCC_μh@10 TeV : SM background ($w^+ w^-$)", linewidth=3)
plt.xlabel(r"$M_{WW} \ \mathrm{[GeV]}$"); plt.ylabel(r"$\frac{d\sigma}{dM_{WW}} \ \mathrm{[pb/GeV]}$")
plt.title(r"$e^- p \to e^- w^+ w^- p \to e^- j j \ell \nu_{\ell} p$ : FCC_μh@10 TeV", fontsize=24)
plt.yscale("log"); plt.legend(); plt.grid(True, linestyle="--", alpha=0.6); plt.tight_layout(); plt.savefig("normalized_cross_section_m_ww_reco_FCC_μh.pdf", dpi=600)
plt.show()





# =======================================================================
# Tail σ(MWW>W_cut) and 95% CL limits (counting, Asimov exact) — unchanged
# =======================================================================

THRESHOLDS = [400.0, 500.0, 600.0, 700.0, 800.0, 900.0, 1000.0, 1200.0, 1400.0, 1600.0, 1800.0, 2000.0, 2200.0, 2400.0, 2600.0, 2800.0]  # GeV
L_fb = 1000.0     # fb^-1
Aeps = 1.0        # acceptance×efficiency
PB_TO_FB = 1e3
f0 = 1.0          # TeV^-4

edges_mww = np.linspace(m_w_hadronic_leptonic_range[0], m_w_hadronic_leptonic_range[1], num_bins + 1)

def integrate_tail_hist(y, edges, thr):
    total = 0.0
    for i in range(len(y)):
        lo, hi = edges[i], edges[i+1]
        if hi <= thr: continue
        width = hi - lo
        if lo < thr < hi: total += y[i] * (hi - thr)
        else:             total += y[i] * width
    return float(total)

def q_asimov(mu, mu0):
    if mu <= 0 or mu0 <= 0: return float("inf")
    return 2.0 * (mu - mu0 + mu0 * math.log(mu0 / mu))

def interval_asimov_exact(c, A, B, L_fb, Aeps, q_target=3.84, f_scan=300.0):
    def qf(f):
        sig = max(c + A*f + B*f*f, 1e-18)
        mu  = L_fb * Aeps * sig * PB_TO_FB
        mu0 = L_fb * Aeps * c   * PB_TO_FB
        return q_asimov(mu, mu0)
    # right root
    flo, fhi, step = 0.0, 0.0, 0.1
    while True:
        fhi = flo + step
        if qf(fhi) >= q_target or fhi >= f_scan: break
        step *= 1.8
    for _ in range(80):
        mid = 0.5*(flo+fhi)
        if qf(mid) < q_target: flo = mid
        else:                  fhi = mid
    f_plus = 0.5*(flo+fhi)
    # left root
    fhi, flo, step = 0.0, 0.0, -0.1
    while True:
        flo = fhi + step
        if qf(flo) >= q_target or abs(flo) >= f_scan: break
        step *= 1.8
    for _ in range(80):
        mid = 0.5*(flo+fhi)
        if qf(mid) < q_target: fhi = mid
        else:                  flo = mid
    f_minus = 0.5*(flo+fhi)
    return f_minus, f_plus

def extract_AB(c, sp, sm, f0):
    A = (sp - sm) / (2.0 * f0)
    B = (sp + sm - 2.0 * c) / (2.0 * f0 * f0)
    return A, B



row_sm = [integrate_tail_hist(dsigma_background_m_w_hadronic_leptonic, edges_mww, thr) for thr in THRESHOLDS]
row_p  = [integrate_tail_hist(dsigma_signal_m_w_hadronic_leptonic_0, edges_mww, thr)   for thr in THRESHOLDS]
row_m  = [integrate_tail_hist(dsigma_signal_m_w_hadronic_leptonic_2, edges_mww, thr)   for thr in THRESHOLDS]

print("\n=== σ(MWW > W_cut) from LHE-level spectra (pb) ===")
hdr = "cut  ".ljust(8) + "σ_SM      σ(+1)    σ(−1)    ".ljust(32) + "N_SM@1000fb  N(+1)@1000fb  N(−1)@1000fb"
print(hdr); print("-"*len(hdr))
for thr, c, sp, sm in zip(THRESHOLDS, row_sm, row_p, row_m):
    N_c  = L_fb * PB_TO_FB * Aeps * c
    N_sp = L_fb * PB_TO_FB * Aeps * sp
    N_sm = L_fb * PB_TO_FB * Aeps * sm
    print(f"W>{int(thr):<4} {c:9.3e} {sp:9.3e} {sm:9.3e}   {N_c:12.1f}   {N_sp:12.1f}    {N_sm:12.1f}")

print("\n=== 95% CL (two-sided, Asimov SM) on f (TeV^-4), per cut and best ===")
print("cut   A[pb/TeV^4]       B[pb/TeV^8]        interval [f−, f+]  ")
best = None
for thr, c, sp, sm in zip(THRESHOLDS, row_sm, row_p, row_m):
    A, B = extract_AB(c, sp, sm, f0)
    f_lo, f_hi = interval_asimov_exact(c, A, B, L_fb=L_fb, Aeps=Aeps, q_target=3.84)
    width = f_hi - f_lo
    print(f"W>{int(thr):<4} {A:14.3e}  {B:14.3e}   [{f_lo:7.3g}, {f_hi:7.3g}]")
    if (best is None) or (width < best[-1]):
        best = (thr, f_lo, f_hi, A, B, c, width)

thr_best, f_lo, f_hi, A_best, B_best, c_best, _ = best
print(f"\n>> Best cut: W > {thr_best:.0f} GeV")
print(f"   σ_tail(f) = c + A f + B f^2 with c={c_best:.4e} pb, A={A_best:.4e} pb/TeV^4, B={B_best:.4e} pb/TeV^8")
print(f"   Two-sided 95% CL: f ∈ [{f_lo:.3g}, {f_hi:.3g}] TeV^-4")



# =======================================================================
# Multi-bin SHAPE likelihood in MWW (Asimov SM, no extra backgrounds)
# (structure preserved; only math/np/calc reused)
# =======================================================================


SHAPE_CUTS = [(400.0, None), (500.0, None), (600.0, None), (700.0, None), (800.0, None),
              (900.0, None), (1000.0, None), (1200.0, None), (1400.0, None), (1600.0, None), (1800.0, None), (2000.0, None), (2200.0, None), (2400.0, None), (2600.0, None), (2800.0, None)]

edges_mww = np.linspace(m_w_hadronic_leptonic_range[0], m_w_hadronic_leptonic_range[1], num_bins + 1)

def build_shape_coeffs(edges, y_sm, y_p, y_m, f0, Wmin=0.0, Wmax=None):
    if Wmax is None: Wmax = edges[-1]
    lo, hi = edges[:-1], edges[1:]
    mask_window = (hi > Wmin) & (lo < Wmax)
    α_full = np.asarray(y_sm)[mask_window]
    β_full = (np.asarray(y_p)[mask_window] - np.asarray(y_m)[mask_window]) / (2.0 * f0)
    γ_full = (np.asarray(y_p)[mask_window] + np.asarray(y_m)[mask_window] - 2.0*np.asarray(y_sm)[mask_window]) / (2.0 * f0 * f0)
    widths_full = (hi - lo)[mask_window].copy()
    i0 = np.argmax(mask_window)
    if lo[i0] < Wmin < hi[i0]:
        frac = (hi[i0] - Wmin) / (hi[i0] - lo[i0])
        widths_full[0] *= frac
    α = np.clip(α_full, 1e-18, None); β = β_full.copy(); γ = γ_full.copy()
    return α, β, γ, widths_full

def asimov_shape_interval(α, β, γ, widths, L_fb, Aeps, q_target=3.84, f_scan=1e3):
    const = L_fb * Aeps * 1000.0
    n0 = const * α * widths
    def q_of(f):
        dens = α + β*f + γ*f*f
        dens = np.clip(dens, 1e-18, None)
        mu   = const * dens * widths
        return 2.0 * np.sum(mu - n0 + n0 * np.log(n0 / mu))
    # right
    flo, fhi, step = 0.0, 0.0, 0.1
    while True:
        fhi = flo + step
        if q_of(fhi) >= q_target or fhi >= f_scan: break
        step *= 1.8
    for _ in range(80):
        mid = 0.5*(flo+fhi)
        if q_of(mid) < q_target: flo = mid
        else:                    fhi = mid
    f_plus = 0.5*(flo+fhi)
    # left
    fhi, flo, step = 0.0, 0.0, -0.1
    while True:
        flo = fhi + step
        if q_of(flo) >= q_target or abs(flo) >= f_scan: break
        step *= 1.8
    for _ in range(80):
        mid = 0.5*(flo+fhi)
        if q_of(mid) < q_target: fhi = mid
        else:                    flo = mid
    f_minus = 0.5*(flo+fhi)
    return f_minus, f_plus

print("\n=== SHAPE likelihood limits in MWW (Asimov SM, two-sided 95% CL) ===")
best_shape = None
for (Wmin, Wmax) in SHAPE_CUTS:
    α, β, γ, widths = build_shape_coeffs(edges_mww,
                                         dsigma_background_m_w_hadronic_leptonic,
                                         dsigma_signal_m_w_hadronic_leptonic_0,
                                         dsigma_signal_m_w_hadronic_leptonic_2,
                                         f0=f0, Wmin=Wmin, Wmax=Wmax)
    if α.size == 0: continue
    f_lo, f_hi = asimov_shape_interval(α, β, γ, widths, L_fb=L_fb, Aeps=Aeps, q_target=3.84)
    width = f_hi - f_lo
    label = f"W>{Wmin:.0f} GeV" if Wmax is None else f"{Wmin:.0f}<W<{Wmax:.0f} GeV"
    print(f"{label:>14}:  f ∈ [{f_lo:.3g}, {f_hi:.3g}] TeV^-4")
    if best_shape is None or width < best_shape[-1]:
        best_shape = (label, f_lo, f_hi, width)

if best_shape:
    label, f_lo, f_hi, _ = best_shape
    print(f">> Best SHAPE window: {label}  →  f ∈ [{f_lo:.3g}, {f_hi:.3g}] TeV^-4")

# Optional auto-scan (unchanged structure)
Wmins = np.arange(0.0, float(edges_mww[-1]) - 1e-6, 50.0)
best_shape = None
for Wmin in Wmins:
    α, β, γ, widths = build_shape_coeffs(edges_mww,
                                         dsigma_background_m_w_hadronic_leptonic,
                                         dsigma_signal_m_w_hadronic_leptonic_0,
                                         dsigma_signal_m_w_hadronic_leptonic_2,
                                         f0=f0, Wmin=Wmin, Wmax=None)
    if α.size == 0: continue
    f_lo, f_hi = asimov_shape_interval(α, β, γ, widths, L_fb=L_fb, Aeps=Aeps, q_target=3.84)
    width = f_hi - f_lo
    if best_shape is None or width < best_shape[-1]:
        best_shape = (Wmin, f_lo, f_hi, width)
if best_shape:
    Wmin_best, f_lo, f_hi, _ = best_shape
    print(f"\n>> Best SHAPE threshold (auto-scan): W>{Wmin_best:.0f} GeV  →  f ∈ [{f_lo:.3g}, {f_hi:.3g}] TeV^-4")


