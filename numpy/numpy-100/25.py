# Create a vector of size 10 with values ranging from 0 to 1, both excluded (★★☆)
import numpy as np

# 0 ~ 1(1を含まずに)の間で等間隔で12こ作る。index 1 ~ lastを抽出
Z = np.linspace(0, 1, 12, endpoint=True)[1:-1]
print(Z)
