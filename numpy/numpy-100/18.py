# Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element ?
import numpy as np

# (6,7,8)を1次元に変えた時に100番目のindexを(6,7,8)に戻したindexを返す
# (1, 5, 4)を返すが、7 * 8 + 5 * 8 + 4 = 100
print(np.unravel_index(100, (6, 7, 8)))

# practice
a = np.array([[10,50,30],[60,20,40]])
print(a)
print(a.shape)
