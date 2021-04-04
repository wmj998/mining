# 代码3-3 捞起生鱼片的季度销售情况

import pandas as pd
import matplotlib.pyplot as plt

catering_sale = 'D:/文件丶/数据分析与挖掘实战/chapter3/data/catering_fish_congee.xls'  # 餐饮数据
data = pd.read_excel(catering_sale,header = None,names=['date','sale'])  # 读取数据，指定“日期”列为索引

bins = [0,500,1000,1500,2000,2500,3000,3500,4000]
data['sale分层'] = pd.cut(data.sale, bins)
aggResult = data.groupby('sale分层').agg({'sale':'count'})
pAggResult = round(aggResult/aggResult.sum(),2) * 100

plt.figure(figsize=(10,6))  # 设置图框大小尺寸
pAggResult['sale'].plot(kind='bar',width=0.8,fontsize=10)  # 绘制频率直方图
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.title('季度销售额频率分布直方图',fontsize=20)
plt.show()
