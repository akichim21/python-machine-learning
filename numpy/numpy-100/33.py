# Given two arrays, X and Y, construct the Cauchy matrix C (Cij = 1/(xi - yj))
import numpy as np

X = np.arange(8)
Y = X + 0.5
A = np.subtract.outer(X, Y)
print(A)
C = 1.0 / A
# np.linalg.detは行列式
print(np.linalg.det(C))

# practice

print(np.subtract(X, Y))
XX = np.array([0, 0])
YY = np.array([2, 2])
print(np.subtract.outer(XX, YY))
XX = np.array([1, 0])
YY = np.array([2, 2])
print(np.subtract.outer(XX, YY))
XX = np.array([0, 0])
YY = np.array([1, 2])
print(np.subtract.outer(XX, YY))
