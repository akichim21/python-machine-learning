# Considering a (w,h,3) image of (dtype=ubyte), compute the number of unique colors (★★★)
import numpy as np

w, h = 16, 16
I = np.random.randint(0, 2, (h,w,3)).astype(np.ubyte)
print(I)
# I[...,0]はI[0,0,0],I[0,1,0]...I[15,15,0]
F = I[...,0] * 256 * 256 + I[...,1] * 256 + I[...,2]
print(F)
n = len(np.unique(F))
print(n)
print(np.unique(I))
