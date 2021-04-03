# 代码4-4 线损率属性构造

import pandas as pd

# 参数初始化
inputfile= 'D:/文件丶/数据分析与挖掘实战/chapter4/demo/data/electricity_data.xls'  # 供入供出电量数据
outputfile = 'D:/文件丶/数据分析与挖掘实战/chapter4/demo/electricity_data.xls'  # 属性构造后数据文件

data = pd.read_excel(inputfile)  # 读入数据
data['线损率'] = (data['供入电量'] - data['供出电量']) / data['供入电量']

data.to_excel(outputfile, index = False)  # 保存结果
