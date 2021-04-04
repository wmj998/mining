# 代码3-21 绘制误差棒图


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

error = np.random.randn(10)  # 定义误差列
y = pd.Series(np.sin(np.arange(10)))  # 均值数据列
print(error)
print(y)
y.plot(yerr = error)  # 绘制误差图
plt.show()
