# 代码3-19 绘制箱型图

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
x = np.random.randn(1000)  # 1000个服从正态分布的随机数
D = pd.DataFrame([x, x+1]).T  # 构造两列的DataFrame
print(D)
D.plot(kind = 'box')  # 调用Series内置的绘图方法画图，用kind参数指定箱型图box
plt.show()
