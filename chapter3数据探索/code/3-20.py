# 代码3-20 使用plot(logy = True)函数进行绘图


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

plt.figure(figsize = (8, 9))  # 设置画布大小

plt.subplot(2, 1, 1)
x = pd.Series(np.exp(np.arange(20)))  # 原始数据
x.plot(label = '原始数据图', legend = True)

plt.subplot(2, 1, 2)
x.plot(logy = True, label = '对数数据图', legend = True)
plt.show()
