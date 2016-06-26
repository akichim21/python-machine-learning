# How to tell if a given 2D array has null columns ? (★★☆)
import numpy as np

Z = np.random.randint(0, 3, (3, 10))
print(Z)
print(Z.any(axis=0))
print(~Z.any(axis=0))
print((~Z.any(axis=0)).any())
