# Considering a four dimensions array, how to get sum over the last two axis at once ? (★★★)
import numpy as np

A = np.random.randint(0, 10, (3, 4, 3, 4))
print(A)
print(A.shape[:-2])
print(A.reshape(A.shape[:-2] + (-1,)))
sum = A.reshape(A.shape[:-2] + (-1,)).sum(axis=-1)
print(sum)
