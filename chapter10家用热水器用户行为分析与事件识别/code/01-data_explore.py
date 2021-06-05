# 代码10-1

import pandas as pd
import matplotlib.pyplot as plt

inputfile = '../data/original_data.xls'  # 输入的数据文件
data = pd.read_excel(inputfile)  # 读取数据

# 查看有无水流的分布
# 数据提取
lv_non = pd.value_counts(data['有无水流'])['无']
lv_move = pd.value_counts(data['有无水流'])['有']
# 绘制条形图

fig = plt.figure(figsize=(6, 5))  # 设置画布大小
plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文显示
plt.rcParams['axes.unicode_minus'] = False
plt.bar(x=range(2), height=[lv_non, lv_move], width=0.4, alpha=0.8,
        color='skyblue')
plt.xticks([index for index in range(2)], ['无', '有'])
plt.xlabel('水流状态')
plt.ylabel('记录数')
plt.title('不同水流状态记录数')
plt.show()
plt.close()

# 查看水流量分布
water = data['水流量']
# 绘制水流量分布箱型图
fig = plt.figure(figsize=(5, 8))
plt.boxplot(water,
            patch_artist=True,
            labels=['水流量'],  # 设置x轴标题
            boxprops={'facecolor': 'lightblue'})  # 设置填充颜色
plt.title('水流量分布箱线图')
# 显示y坐标轴的底线
plt.grid(axis='y')
plt.show()
