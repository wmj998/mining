# 代码11-15 计算推荐结果的准确率、召回率和F1指标

import pandas as pd

# 读取保存的推荐结果
Res = pd.read_csv('../tmp/Res.csv', keep_default_na=False, encoding='utf8')

# 计算推荐准确率
Pre = round(sum(Res.loc[:, 'T/F'] == 'True') / (len(Res.index) - sum(Res.loc[:, 'T/F'] == 'NaN')), 3)

print(Pre)

# 计算推荐召回率
Rec = round(sum(Res.loc[:, 'T/F'] == 'True') / (sum(Res.loc[:, 'T/F'] == 'True') + sum(Res.loc[:, 'T/F'] == 'NaN')), 3)

print(Rec)

# 计算F1指标
F1 = round(2 * Pre * Rec / (Pre + Rec), 3)
print(F1)
