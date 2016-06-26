# Consider a random vector with shape (100,2) representing coordinates, find point by point distances (★★☆)
import numpy as np

Z = np.random.random((10, 2))
print(Z)
print(Z[:,0])
X, Y = np.atleast_2d(Z[:,0]), np.atleast_2d(Z[:,1])
print(X)
print(Y)
print(X.T)
print(Y.T)
D = np.sqrt( (X - X.T) ** 2 + (Y - Y.T) ** 2)
print(D)

import scipy
import scipy.spatial

Z = np.random.random((10, 2))
D = scipy.spatial.distance.cdist(Z, Z)
print(D)
