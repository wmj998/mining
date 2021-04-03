# 代码4-6 主成分分析降维

import pandas as pd
from sklearn.decomposition import PCA

# 参数初始化
inputfile = 'D:/文件丶/数据分析与挖掘实战/chapter4/demo/data/principal_component.xls'
outputfile = 'D:/文件丶/数据分析与挖掘实战/chapter4/demo/dimention_reducted.xls'  # 降维后的数据
data = pd.read_excel(inputfile, header = None)  # 读入数据

pca = PCA(3) # 降维后的维数3
pca.fit(data)
low_d = pca.transform(data)  # 用transform()函数来降低维度
data_1 = pd.DataFrame(low_d)
data_1.to_excel(outputfile, index=False, header=None)  # 保存结果


# 必要时可以用inverse_transform()函数来复原数据
# high_d = pca.inverse_transform(low_d)
# data_2 = pd.DataFrame(high_d)
# data_3 = data.append(data_2)
# data_3.to_excel(inputfile, index=False, header=None)
