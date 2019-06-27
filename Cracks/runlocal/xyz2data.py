import numpy as np

with open("data.setup_passivated", "r") as infile:
    for i in range(5):
        infile.readline()
    xmin, xmax = map(float, infile.readline().split()[:2])
    ymin, ymax = map(float, infile.readline().split()[:2])
    zmin, zmax = map(float, infile.readline().split()[:2])

data = np.loadtxt("xyz.water", unpack=True, skiprows=2)

N= len(data[0])
start=np.argmax(data[0]==3)
ar=np.ones(N,dtype=bool)
ar[:start]=0
lowx=data[1]<200
new=ar*lowx
Nnew=np.sum(np.invert(new))
newdat=data.transpose()[np.invert(new)].transpose()


new_data = np.column_stack((np.arange(1, Nnew + 1), *newdat))
new_data[:,2]-=40.50296

np.savetxt(
        "waterbox.data",
        new_data,
        fmt="%d %d %g %g %g",
        header=f"""created by xyz2data.py

{Nnew} atoms
3 atom types

{xmin} {xmax} xlo xhi
{ymin} {ymax} ylo yhi
{zmin} {zmax} zlo zhi

Masses

1 28.08
2 15.9994
3 1.00794

Atoms
""", comments="")
