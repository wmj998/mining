# 代码11-14 构建模型

import pandas as pd

# 利用训练集数据构建模型
UI_matrix_tr = pd.DataFrame(0, index=IP_tr, columns=url_tr)
# 求用户－物品矩阵
for i in data_tr.index:
    UI_matrix_tr.loc[data_tr.loc[i, 'realIP'], data_tr.loc[i, 'fullURL']] = 1
sum(UI_matrix_tr.sum(axis=1))

# 求物品相似度矩阵（因计算量较大，需要耗费的时间较久）
Item_matrix_tr = pd.DataFrame(0, index=url_tr, columns=url_tr)
for i in Item_matrix_tr.index:
    for j in Item_matrix_tr.index:
        a = sum(UI_matrix_tr.loc[:, [i, j]].sum(axis=1) == 2)
        b = sum(UI_matrix_tr.loc[:, [i, j]].sum(axis=1) != 0)
        Item_matrix_tr.loc[i, j] = a / b

# 将物品相似度矩阵对角线处理为零
for i in Item_matrix_tr.index:
    Item_matrix_tr.loc[i, i] = 0

# 利用测试集数据对模型评价
IP_te = data_te.iloc[:, 0]
url_te = data_te.iloc[:, 1]
IP_te = list(set(IP_te))
url_te = list(set(url_te))

# 测试集数据用户物品矩阵
UI_matrix_te = pd.DataFrame(0, index=IP_te, columns=url_te)
for i in data_te.index:
    UI_matrix_te.loc[data_te.loc[i, 'realIP'], data_te.loc[i, 'fullURL']] = 1

# 对测试集IP进行推荐
Res = pd.DataFrame('NaN', index=data_te.index,
                   columns=['IP', '已浏览网址', '推荐网址', 'T/F'])
Res.loc[:, 'IP'] = list(data_te.iloc[:, 0])
Res.loc[:, '已浏览网址'] = list(data_te.iloc[:, 1])

# 开始推荐
for i in Res.index:
    if Res.loc[i, '已浏览网址'] in list(Item_matrix_tr.index):
        Res.loc[i, '推荐网址'] = Item_matrix_tr.loc[Res.loc[i, '已浏览网址'],
                             :].argmax()
        if Res.loc[i, '推荐网址'] in url_te:
            Res.loc[i, 'T/F'] = UI_matrix_te.loc[Res.loc[i, 'IP'],
                                                 Res.loc[i, '推荐网址']] == 1
        else:
            Res.loc[i, 'T/F'] = False

# 保存推荐结果
Res.to_csv('./tmp/Res.csv', index=False, encoding='utf8')
