# 代码3-5 不同部门在各月份的销售对比情况
# 部门之间销售金额比较

import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决plt中文显示的问题
plt.rcParams['axes.unicode_minus'] = False    # 解决plt负号显示的问题

data=pd.read_excel("D:/文件丶/数据分析与挖掘实战/chapter3/data/dish_sale.xls")
plt.figure(figsize=(8, 4))
plt.plot(data['月份'], data['A部门'], color='green', label='A部门',marker='o')
plt.plot(data['月份'], data['B部门'], color='red', label='B部门',marker='s')
plt.plot(data['月份'], data['C部门'],  color='skyblue', label='C部门',marker='x')
plt.legend() # 显示图例
plt.ylabel('销售额（万元）')
plt.show()


#  B部门各年份之间销售金额的比较
data=pd.read_excel("D:/文件丶/数据分析与挖掘实战/chapter3/data/dish_sale_b.xls")
plt.figure(figsize=(8, 4))
plt.plot(data['月份'], data['2012年'], color='green', label='2012年',marker='o')
plt.plot(data['月份'], data['2013年'], color='red', label='2013年',marker='s')
plt.plot(data['月份'], data['2014年'],  color='skyblue', label='2014年',marker='x')
plt.legend() # 显示图例
plt.ylabel('销售额（万元）')
plt.show()
