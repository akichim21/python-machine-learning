# Create a structured array with x and y coordinates covering the [0,1]x[0,1] area (★★☆)
import numpy as np

Z = np.zeros((10, 10), [('x', float), ('y', float)])
x, y = np.meshgrid(np.linspace(0, 1, 10),np.linspace(0, 1, 10))
print(x)
print(y)
Z['x'], Z['y'] = x, y
print(Z)
