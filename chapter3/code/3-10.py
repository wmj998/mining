# 代码3-10 计算两个列向量的相关系数
import pandas as pd
D = pd.DataFrame([range(1, 8), range(2, 9)])  # 生成样本D，一行为1~7，一行为2~8
print(D.corr())  # 计算相关系数矩阵
S1 = D.loc[0]  # 提取第一行
S2 = D.loc[1]  # 提取第二行
print(S1.corr(S2))  # 计算S1、S2的相关系数