# Considering a one-dimensional vector D, how to compute means of subsets of D using a vector S of same size describing subset indices ? (★★★)
import numpy as np

D = np.random.uniform(0, 1, 100)
print(D)
S = np.random.randint(0, 10, 100)
print(S)
D_sums = np.bincount(S, weights = D)
print(D_sums)
D_counts = np.bincount(S)
print(D_counts)
D_means = D_sums / D_counts
print(D_means)
