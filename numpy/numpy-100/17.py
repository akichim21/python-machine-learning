# Create a 8x8 matrix and fill it with a checkerboard pattern (★☆☆)
import numpy as np

Z = np.zeros((8, 8), dtype=int)
print(type(Z))
Z[1::2, ::2] = 1
Z[::2,1::2] = 1
print(Z)

# practive
X = np.random.random((8, 8))
print(X)
print(X[1::2])
print(X[1::2,::2])
print(X[::2])
print(X[::2,1::2])
