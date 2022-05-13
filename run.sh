#!/bin/bash

 irun=1
 nrun=51
 while [ $irun -le $nrun ]
 do

 sed  -e s/1-dens/$irun-dens/g  < feature-vector.f90 > feature-vector-$irun.f90
 
 gfortran feature-vector-$irun.f90 
 ./a.out
 mv spin-total.dat spin-total_$irun.out

 irun=$(( $irun + 1 ))

 done
 rm property-*
 date
 exit 0
