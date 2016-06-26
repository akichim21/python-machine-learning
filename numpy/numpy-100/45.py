# How to I sort an array by the nth column ? (★★☆)
import numpy as np

Z = np.random.randint(0, 10, (3, 3))
print(Z)
print(Z[:,1])
print(Z[:,1].argsort())
print(Z[Z[:,1].argsort()])
