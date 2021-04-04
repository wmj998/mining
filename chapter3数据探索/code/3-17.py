# 代码3-17 绘制饼图


import matplotlib.pyplot as plt

# The slices will be ordered and plotted counter-clockwise.
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'  # 定义标签
sizes = [15, 30, 45, 10]  # 每一块的比例
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']  # 每一块的颜色
explode = (0, 0.1, 0, 0)  # 突出显示，这里仅仅突出显示第二块（即'Hogs'）

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')  # 显示为圆（避免比例压缩为椭圆）
plt.show()
