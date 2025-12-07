ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c      written by the UFO converter
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

C     
C     NB: VECSIZE_MEMMAX is defined in vector.inc
C     NB: vector.inc must be included before coupl.inc
C     

      DOUBLE PRECISION G, ALL_G(1)
      COMMON/STRONG/ G, ALL_G

      DOUBLE COMPLEX GAL(2)
      COMMON/WEAK/ GAL

      DOUBLE PRECISION MU_R, ALL_MU_R(1)
      COMMON/RSCALE/ MU_R, ALL_MU_R

      DOUBLE PRECISION NF
      PARAMETER(NF=0D0)
      DOUBLE PRECISION NL
      PARAMETER(NL=0D0)

      DOUBLE PRECISION MDL_MB,MDL_MC,MDL_MD,MDL_MH,MDL_MMU,MDL_MS
     $ ,MDL_MT,MDL_MTA,MDL_MU,MDL_MW,MDL_MZ,MDL_ME

      COMMON/MASSES/ MDL_MB,MDL_MC,MDL_MD,MDL_MH,MDL_MMU,MDL_MS,MDL_MT
     $ ,MDL_MTA,MDL_MU,MDL_MW,MDL_MZ,MDL_ME


      DOUBLE PRECISION MDL_WH,MDL_WT,MDL_WW,MDL_WZ

      COMMON/WIDTHS/ MDL_WH,MDL_WT,MDL_WW,MDL_WZ


      DOUBLE COMPLEX GC_2, GC_3, GC_19, GC_21, GC_23, GC_25, GC_34,
     $  GC_36, GC_38, GC_40, GC_41, GC_43, GC_45, GC_47, GC_62, GC_63,
     $  GC_68, GC_69, GC_72, GC_74, GC_76, GC_79, GC_81, GC_83, GC_10,
     $  GC_12, GC_14, GC_16

      DOUBLE COMPLEX GC_7(VECSIZE_MEMMAX), GC_27(VECSIZE_MEMMAX),
     $  GC_29(VECSIZE_MEMMAX), GC_31(VECSIZE_MEMMAX),
     $  GC_33(VECSIZE_MEMMAX)

      COMMON/COUPLINGS/ GC_7, GC_27, GC_29, GC_31, GC_33, GC_2, GC_3,
     $  GC_19, GC_21, GC_23, GC_25, GC_34, GC_36, GC_38, GC_40, GC_41,
     $  GC_43, GC_45, GC_47, GC_62, GC_63, GC_68, GC_69, GC_72, GC_74,
     $  GC_76, GC_79, GC_81, GC_83, GC_10, GC_12, GC_14, GC_16

