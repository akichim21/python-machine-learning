# Create random vector of size 10 and replace the maximum value by 0 (★★☆)
import numpy as np

Z = np.random.random(10)
Z[Z.argmax()] = 0
print(Z)
