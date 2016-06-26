# Consider a given vector, how to add 1 to each element indexed by a second vector (be careful with repeated indices) ? (★★★)
import numpy as np

Z = np.ones(10)
I = np.random.randint(0, len(Z), 20)
print(I)
Z += np.bincount(I, minlength=len(Z))
print(Z)
