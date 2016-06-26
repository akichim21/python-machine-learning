# Consider the following file:
# 1,2,3,4,5
# 6,,,7,8
# ,,9,10,11
import numpy as np

Z = np.genfromtxt("missing.dat", delimiter=",")
print(Z)
