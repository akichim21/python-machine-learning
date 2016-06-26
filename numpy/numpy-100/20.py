# Normalize a 5x5 random matrix (★☆☆)
import numpy as np

Z = np.random.random((5, 5))
print(Z)

Zmax, Zmin = Z.max(), Z.min()
Z = (Z - Zmin) / (Zmax - Zmin)
print(Z)
