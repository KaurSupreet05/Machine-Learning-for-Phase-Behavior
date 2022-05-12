Implicit none 
Character*40    ::  dummya, dummyb 
Character*40       :: dumya, dumyb,dumyc,dumyd,catname 
Character :: solarray,darray,atmarray
Real*8       :: lx,ly,lz,lxn, rcut
double precision    :: dist
Integer :: ii,nr, iline, j, k,i, nn, nf,na, ncount, nb
Integer, Parameter :: natoms=8192, nframes=100
Integer*8, Dimension (1:natoms) :: dum1,dum3
Character*8, Dimension(1:natoms) :: dum2
Integer, Dimension (1:10) :: dum4,nk
Real, allocatable  :: CX(:,:),CY(:,:),CZ(:,:),xda,yda,zda
Real*8 :: val, xd, yd, zd, div

!!! Each gro file has 100 frames corresponding to each density point 
open (10, File= 'confout-1-dens.gro')
open (20, File= 'spin-total.dat')


allocate(CX(nframes,natoms))
allocate(CY(nframes,natoms))
allocate(CZ(nframes,natoms))

do ii=1, nframes
   read (10, *) dumya,dumyb,dumyc
   read (10, *) nn
   
do i=1,natoms
   read(10,'(i5,a9,i6,3f8.3)') dum1(i),dum2(i),dum3(i),CX(ii,i),CY(ii,i),CZ(ii,i)
   
enddo   
   
   read (10, *)lx,ly,lz
  
enddo


      rcut = 0.50*lx
      na = 0
      nb = 0
 do i=1,nframes
        if (mod(i,10).eq.0) then
           print*,i,'th step complete'
        endif
    do j=1,natoms/2
       do k=1,natoms
          if (j.ne.k) then
             xd = CX(i,j)-CX(i,k)
             yd = CY(i,j)-CY(i,k)
             zd = CZ(i,j)-CZ(i,k)
             xd = xd-lx*nint(xd/lx)
             yd = yd-lx*nint(yd/lx)
             zd = zd-lx*nint(zd/lx)
             dist = dsqrt(xd*xd+yd*yd+zd*zd)
             if (dist.lt.rcut) then
                ncount = ncount + 1
                if (k.le.natoms/2) then
                   na = na+1
                else
                   nb = nb+1
                endif
             endif
          endif
       enddo
       if (na.gt.nb) then
          write(20,*) 1
       elseif (na.lt.nb) then
          write(20,*) -1
       else
          write(20,*) 1
       endif
       ncount = 0
       na = 0
       nb = 0
    enddo
    do j=natoms/2+1,natoms
       do k=1,natoms
          if (j.ne.k) then
             xd = CX(i,j)-CX(i,k)
             yd = CY(i,j)-CY(i,k)
             zd = CZ(i,j)-CZ(i,k)
             xd = xd-lx*nint(xd/lx)
             yd = yd-lx*nint(yd/lx)
             zd = zd-lx*nint(zd/lx)
             dist = dsqrt(xd*xd+yd*yd+zd*zd)
             if (dist.lt.rcut) then
                ncount = ncount + 1
                if (k.le.natoms/2) then
                   na = na+1
                else
                   nb = nb+1
                endif
             endif
          endif
       enddo
       if (nb.gt.na) then
          write(20,*) 1
       elseif (nb.lt.na) then
          write(20,*) -1
       else
          write(20,*) 1
       endif
       ncount = 0
       na = 0
       nb = 0
    enddo
     

      enddo


end program
