# 代码3-13 6×5随机矩阵的describe

import numpy as np
import pandas as pd

D = pd.DataFrame(np.random.randn(6, 5))  # 产生6×5随机矩阵
print(D.describe())
