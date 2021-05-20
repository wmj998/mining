# 代码3-18 绘制二维条形直方图

import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(1000)  # 1000个服从正态分布的随机数
plt.hist(x, 10)  # 分成10组进行绘制直方图
plt.show()
