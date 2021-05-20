# 代码4-8 求向量D中的单值元素，并返回相关索引

import pandas as pd
import numpy as np

D = pd.Series([1, 1, 2, 3, 5])

D_1 = D.unique()
D_2 = np.unique(D)
print(D_1)
print(D_2)
