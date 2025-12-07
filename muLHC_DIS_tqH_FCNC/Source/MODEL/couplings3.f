ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c      written by the UFO converter
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      SUBROUTINE COUP3( VECID)

      IMPLICIT NONE
      INTEGER VECID
      INCLUDE 'model_functions.inc'
      INCLUDE '../vector.inc'


      DOUBLE PRECISION PI, ZERO
      PARAMETER  (PI=3.141592653589793D0)
      PARAMETER  (ZERO=0D0)
      INCLUDE 'input.inc'
      INCLUDE 'coupl.inc'
      GC_7(VECID) = MDL_COMPLEXI*G
      GC_27(VECID) = (G*MDL_IMZETALCT)/MDL_MT+(MDL_COMPLEXI*G
     $ *MDL_REZETALCT)/MDL_MT
      GC_29(VECID) = (G*MDL_IMZETALUT)/MDL_MT+(MDL_COMPLEXI*G
     $ *MDL_REZETALUT)/MDL_MT
      GC_31(VECID) = (G*MDL_IMZETARCT)/MDL_MT+(MDL_COMPLEXI*G
     $ *MDL_REZETARCT)/MDL_MT
      GC_33(VECID) = (G*MDL_IMZETARUT)/MDL_MT+(MDL_COMPLEXI*G
     $ *MDL_REZETARUT)/MDL_MT
      END
