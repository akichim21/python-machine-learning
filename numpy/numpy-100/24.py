# Consider a generator function that generates 10 integers and use it to build an array (★☆☆)
import numpy as np

def generate():
  for x in range(10):
    yield x

# Create a new 1-dimensional array from an iterable object.
Z = np.fromiter(generate(), dtype=float, count = -1)
print(Z)
