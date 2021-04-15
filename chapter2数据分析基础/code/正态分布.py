import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
n = np.random.normal(0, 1, 1000)   # 生成均值为0，标准差为1的一维正态分布样本1000个
sns.distplot(n)                      # 直方图
plt.show()  # 显示
