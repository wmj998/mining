# logistic_regression

import pandas as pd
from sklearn.linear_model import LogisticRegression as LR

# 参数初始化
filename = '../data/bankloan.xls'
data = pd.read_excel(filename)
x = data.iloc[:,:8].values
y = data.iloc[:,8].values

lr = LR()  # 建立逻辑回归模型
lr.fit(x, y)  # 用筛选后的特征数据来训练模型
print('模型的平均准确度为：%s' % lr.score(x, y))
