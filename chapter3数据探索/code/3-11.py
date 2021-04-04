# 代码3-11 计算6×5随机矩阵的协方差矩阵

import numpy as np
import pandas as pd
D = pd.DataFrame(np.random.randn(6, 5))  # 产生6×5随机矩阵
print(D.cov())  # 计算协方差矩阵
print(D[0].cov(D[1]))  # 计算第一列和第二列的协方差
