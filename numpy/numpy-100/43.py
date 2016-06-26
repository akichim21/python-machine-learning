# How to randomly place p elements in a 2D array ? (★★☆)
import numpy as np

n = 10
p = 3
Z = np.zeros((n, n))
print(Z)
print(np.random.choice(range(n * n), p, replace=False))
np.put(Z, np.random.choice(range(n * n), p, replace=False), 1)
print(Z)
