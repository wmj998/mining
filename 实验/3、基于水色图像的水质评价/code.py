import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

# 读取数据
data = pd.read_csv('moment.csv', encoding='gbk')

# 处理数据
labels = data.类别.values
data = data.iloc[:, 2:].values

# 数据拆分,训练集、测试集
data_tr, data_te, label_tr, label_te = train_test_split(data, labels,
                                                        test_size=0.2, random_state=20)

# 模型训练
model = DecisionTreeClassifier(random_state=10).fit(data_tr, label_tr)

# 数据预测
pre_te = model.predict(data_te)

# 混淆矩阵
cm_te = confusion_matrix(label_te, pre_te)

print('预测报告：\n', classification_report(label_te, pre_te))
print('混淆矩阵：\n', cm_te)
print('准确率：', accuracy_score(label_te, pre_te))
