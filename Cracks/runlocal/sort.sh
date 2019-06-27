#!/bin/bash
#does something
mkdir $1
mv $1".in" $1
cd $1
module load mpi
mpirun -n 1 lmp_mpi -in $1".in"
echo "Box initialized"
packmol < add_water.inp
echo "Water added"
python ../xyz2data.py
echo "Final data in waterbox.data"
mv ../$2 .
mpirun -n 8 lmp_mpi -in $2".in"
