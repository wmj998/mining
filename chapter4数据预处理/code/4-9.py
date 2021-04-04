# 代码 4-9 对一个10×4维的随机矩阵进行主成分分析

import numpy as np
from sklearn.decomposition import PCA

D = np.random.rand(10,4)

pca = PCA()
pca.fit(D)
pca.components_  # 返回模型的各个特征向量
print(pca.components_)

pca.explained_variance_ratio_  # 返回各个成分各自的方差百分比
print(pca.explained_variance_ratio_)
