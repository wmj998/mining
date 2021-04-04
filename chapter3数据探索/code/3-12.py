# 代码3-12 计算6×5随机矩阵的偏度（三阶矩）∕峰度（四阶矩）

import numpy as np
import pandas as pd
D = pd.DataFrame(np.random.randn(6, 5))  # 产生6×5随机矩阵
print(D.skew())  # 计算偏度
print(D.kurt())  # 计算峰度
