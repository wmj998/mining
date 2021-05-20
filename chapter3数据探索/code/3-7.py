# 代码3-7 某单位日用电量预测分析

import pandas as pd
import matplotlib.pyplot as plt

df_normal = pd.read_csv("../data/user.csv")
df_steal = pd.read_csv("../data/Steal user.csv")

plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决plt中文显示的问题
plt.rcParams['axes.unicode_minus'] = False  # 解决plt负号显示的问题

plt.title("用电量趋势")
plt.xlabel("日期")
plt.ylabel("每日电量")

# 设置x轴刻度间隔
x_major_locator = plt.MultipleLocator(7)
ax = plt.gca()
ax.xaxis.set_major_locator(x_major_locator)

plt.plot(df_normal["Date"], df_normal["Eletricity"], color="b", label="正常用户")
plt.plot(df_steal["Date"], df_steal["Eletricity"], color="r", label="窃电用户")

plt.legend()  # 显示图例
plt.show()  # 展示图片
