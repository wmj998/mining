# 代码3-14 pandas累积统计特征函数、移动窗口统计函数示例

import pandas as pd
D=pd.Series(range(0, 20))  # 构造Series，内容为0~19共20个整数
print(D.cumsum())  # 给出前n项和
print(D.rolling(2).sum())  # 依次对相邻两项求和
