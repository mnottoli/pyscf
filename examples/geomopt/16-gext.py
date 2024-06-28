#!/usr/bin/env python

'''
Enable the Grassmann extrapolation in geometry optimizations.
'''

from pyscf import gto, scf

mol = gto.M(atom='''
C       1.1879  -0.3829 0.0000
C       0.0000  0.5526  0.0000
O       -1.1867 -0.2472 0.0000
H       -1.9237 0.3850  0.0000
H       2.0985  0.2306  0.0000
H       1.1184  -1.0093 0.8869
H       1.1184  -1.0093 -0.8869
H       -0.0227 1.1812  0.8852
H       -0.0227 1.1812  -0.8852
''', basis='3-21g')
mf = scf.RHF(mol)

from pyscf.geomopt.geometric_solver import optimize

mol_eq = optimize(mf, gext=True)
mol_eq = mf.Gradients().optimizer(solver='geomeTRIC').kernel(params={'gext': True})

from pyscf.geomopt.berny_solver import optimize

mol_eq = optimize(mf, gext=True)
mol_eq = mf.Gradients().optimizer(solver='berny').kernel(params={'gext': True})
