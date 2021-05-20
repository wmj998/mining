# 代码3-15 绘图之前需要加载的代码
import matplotlib.pyplot as plt  # 导入绘图库

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.figure(figsize=(7, 5))  # 创建图像区域，指定比例
