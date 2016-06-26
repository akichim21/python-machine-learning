# What is the equivalent of enumerate for numpy arrays ? (★★☆)
import numpy as np

Z = np.arange(9).reshape(3, 3)
for index, value in np.ndenumerate(Z):
  print(index, value)

print("")
for index in np.ndindex(Z.shape):
  print(index, Z[index])
