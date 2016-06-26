# How to convert a float (32 bits) array into an integer (32 bits) in place ?
import numpy as np

Z = np.arange(10, dtype=np.int32)
Z = Z.astype(np.float32, copy=False)
print(Z)
