
muLHC

python3.10 muLHC_dsig_dMWW_v1.py \
  /home/hamzeh-khanpour/MG5_aMC_v3_6_4/muLHC_SM_aa_ww/Events/run_01/muLHC_SM_aa_ww.lhe \
  /home/hamzeh-khanpour/MG5_aMC_v3_6_4/muLHC_EFT_aa_ww/Events/run_01/muLHC_EFT_aa_ww.lhe \
  --bins 60 --range 160 1600 --yield-mode dsig --logy \
  --out-prefix muLHC_mww_compare_muLHC_SM_vs_EFT_dsig_logy



python3.10 muLHC_dsig_dMWW_v1.py \
  /home/hamzeh-khanpour/MG5_aMC_v3_6_4/muLHC_SM_aa_ww/Events/run_01/muLHC_SM_aa_ww.lhe \
  /home/hamzeh-khanpour/MG5_aMC_v3_6_4/muLHC_EFT_aa_ww/Events/run_01/muLHC_EFT_aa_ww.lhe \
  --bins 60 --range 160 1600 --yield-mode counts --logy --lumi-fb 1   \
  --out-prefix muLHC_mww_compare_muLHC_SM_vs_EFT_dsig_logy_counts




LHC

python3.10 LHC_dsig_dMWW_v1.py \
  /home/hamzeh-khanpour/MG5_aMC_v3_6_4/gamma-UPC-aaww-SM-EFT/Events/run_03/gamma-UPC-aaww-SM-chff.lhe \
  /home/hamzeh-khanpour/MG5_aMC_v3_6_4/gamma-UPC-aaww-SM-EFT/Events/run_04/gamma-UPC-aaww-EFT-chff.lhe \
  --bins 60 --range 160 1600 --yield-mode dsig --logy \
  --out-prefix LHC_mww_compare_muLHC_SM_vs_EFT_dsig_logy




LHeC

python3.10 LHeC_dsig_dMWW_v1.py \
  /home/hamzeh-khanpour/MG5_aMC_v3_6_4/LHeC_SM_aa_ww/Events/run_01/LHeC_SM_aa_ww.lhe \
  /home/hamzeh-khanpour/MG5_aMC_v3_6_4/LHeC_EFT_aa_ww/Events/run_02/LHeC_EFT_aa_ww.lhe \
  --bins 60 --range 160 1600 --yield-mode dsig --logy \
  --out-prefix LHeC_mww_compare_muLHC_SM_vs_EFT_dsig_logy














muLHC  muLHC_SM_EFT_aa_ww_semileptonic_decay_number_of_events_overflow_dsigma_dpT.py  for  overflow bins


python muLHC_SM_EFT_aa_ww_semileptonic_decay_number_of_events_overflow_dsigma_dpT.py   "/home/hamzeh-khanpour/MG5_aMC_v3_6_4/muLHC_SM_aa_ww_semi_leptonic/Events/run_01/muLHC_SM_aa_ww_semi_leptonic.lhe"   "/home/hamzeh-khanpour/MG5_aMC_v3_6_4/muLHC_EFT_aa_ww_semi_leptonic/Events/run_01/muLHC_EFT_aa_ww_semi_leptonic.lhe"   --bins-lep 16 --range-lep 0 160 --bins-j 16 --range-j 0 160  --lumi-fb 100   --yield-mode counts  --logy --overflow-lastbin-all



python muLHC_SM_EFT_aa_ww_semileptonic_decay_number_of_events_overflow_dsigma_dpT.py   "/home/hamzeh-khanpour/MG5_aMC_v3_6_4/muLHC_SM_aa_ww_semi_leptonic/Events/run_01/muLHC_SM_aa_ww_semi_leptonic.lhe"   "/home/hamzeh-khanpour/MG5_aMC_v3_6_4/muLHC_EFT_aa_ww_semi_leptonic/Events/run_01/muLHC_EFT_aa_ww_semi_leptonic.lhe"   --bins-lep 16 --range-lep 0 160 --bins-j 16 --range-j 0 160   --yield-mode dsig --logy --no-overflow-lastbin-j1 --no-overflow-lastbin-j2 --no-overflow-lastbin-lep











