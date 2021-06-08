import numpy as np
import pandas as pd

# 读取数据
data = pd.read_excel('water_heater.xls')
# 划分用水事件
threshold = pd.Timedelta('4 min')  # 阈值为4分钟
data['发生时间'] = pd.to_datetime(data['发生时间'], format='%Y%m%d%H%M%S')  # 转换时间格式
data = data[data['水流量'] > 0]  # 只要流量大于0的记录
sjKs = data['发生时间'].diff() > threshold  # 相邻时间向前差分，比较是否大于阈值
sjKs.iloc[0] = True  # 令第一个时间为第一个用水事件的开始事件
sjJs = sjKs.iloc[1:]  # 向后差分的结果
sjJs = pd.concat([sjJs, pd.Series(True)])  # 令最后一个时间作为最后一个用水事件的结束时间
# 创建数据框，并定义用水事件序列
sj = pd.DataFrame(np.arange(1, sum(sjKs) + 1), columns=["事件序号"])
sj["事件起始编号"] = data.index[sjKs == 1] + 1  # 定义用水事件的起始编号
sj["事件终止编号"] = data.index[sjJs == 1] + 1  # 定义用水事件的终止编号
sj.to_excel('sj.xls', index=False)
