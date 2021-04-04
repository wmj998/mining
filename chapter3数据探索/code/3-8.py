# 代码3-8 菜品盈利帕累托图

# 菜品盈利数据 帕累托图
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 初始化参数
dish_profit = 'D:/文件丶/数据分析与挖掘实战/chapter3/data/catering_dish_profit.xls'  # 餐饮菜品盈利数据
data = pd.read_excel(dish_profit, index_col = '菜品名')

data = data['盈利']
data.sort_values(ascending = False) # False降序排列
p = 1.0*data.cumsum()/data.sum()

plt.ylabel('盈利（元）')
data.plot(kind='bar') # kind='bar'直方图,默认折线图

p.plot(color = 'r', secondary_y = True, style = '-o',linewidth = 2)
plt.ylabel('盈利（比例）')
plt.annotate(format(p[6], '.4%'), xy = (6, p[6]), xytext=(6*0.9, p[6]*0.9), arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))  # 添加注释，即85%处的标记。这里包括了指定箭头样式。
plt.show()
