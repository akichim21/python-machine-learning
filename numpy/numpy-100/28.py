# Consider two random array A anb B, check if they are equal (★★☆)
import numpy as np

A = np.random.randint(0, 2, 5)
B = np.random.randint(0, 2, 5)
equal = np.allclose(A, B)
print(equal)
