# Create a 2d array with 1 on the border and 0 inside (★☆☆)
import numpy as np

Z = np.ones((10, 10))
print(Z)
Z[1:-1,1:-1] = 0
print(Z)
