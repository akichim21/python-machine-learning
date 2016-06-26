# Create a 5x5 matrix with values 1,2,3,4 just below the diagonal (★☆☆)
# diagonal: 対角線
import numpy as np

X = 1 + np.arange(4)
print(np.diag(X, k = -1))

# practice
print(np.diag(X, k = 1))
print(np.diag(X))
