# 代码3-16 绘制一条蓝色的正弦虚线

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,2*np.pi,50)  # x坐标输入
y = np.sin(x)  # 计算对应x的正弦值
plt.plot(x, y, 'bp--')  # 控制图形格式为蓝色带星虚线，显示正弦曲线
plt.show()
