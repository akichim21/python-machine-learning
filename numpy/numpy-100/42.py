# Generate a generic 2D Gaussian-like array (★★☆)
import numpy as np

X, Y = np.meshgrid(np.linspace(-1, 1, 10), np.linspace(-1, 1, 10))
D = np.sqrt(X*X + Y*Y)
print(D)
sigma, mu = 1.0, 0.0
G = np.exp(-( (D - mu) ** 2 / (2.0 * sigma ** 2)))
print(G)
