# 代码11-2 网页类型统计

import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/test?charset=utf8')
sql = pd.read_sql('all_gzdata', engine, chunksize=10000)

# 分析网页类型
counts = [i['fullURLId'].value_counts() for i in sql]  # 逐块统计
counts = counts.copy()
counts = pd.concat(counts).groupby(level=0).sum()  # 合并统计结果，把相同的统计项合并（即按index分组并求和）
counts = counts.reset_index()  # 重新设置index，将原来的index作为counts的一列
counts.columns = ['index', 'num']  # 重新设置列名，主要是第二列，默认为0
counts['type'] = counts['index'].str.extract('(\d{3})')  # 提取前三个数字作为类别id
counts_ = counts[['type', 'num']].groupby('type').sum()  # 按类别合并
counts_.sort_values(by='num', ascending=False, inplace=True)  # 降序排列
counts_['ratio'] = counts_.iloc[:, 0] / counts_.iloc[:, 0].sum()
print(counts_)


# 代码11-3 知识类型内部统计

# 因为只有107001一类，但是可以继续细分成三类：知识内容页、知识列表页、知识首页
def count107(i):  # 自定义统计函数
    j = i[['fullURL']][i['fullURLId'].str.contains('107')].copy()  # 找出类别包含107的网址
    j['type'] = None  # 添加空列
    j['type'][j['fullURL'].str.contains('info/.+?/')] = u'知识首页'
    j['type'][j['fullURL'].str.contains('info/.+?/.+?')] = u'知识列表页'
    j['type'][j['fullURL'].str.contains('/\d+?_*\d+?\.html')] = u'知识内容页'
    return j['type'].value_counts()


# 注意：获取一次sql对象就需要重新访问一下数据库(!!!)
# engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/test?charset=utf8')
sql = pd.read_sql('all_gzdata', engine, chunksize=10000)

counts2 = [count107(i) for i in sql]  # 逐块统计
counts2 = pd.concat(counts2).groupby(level=0).sum()  # 合并统计结果
print(counts2)
# 计算各个部分的占比
res107 = pd.DataFrame(counts2)
# res107.reset_index(inplace=True)
res107.index.name = u'107类型'
res107.rename(columns={'type': 'num'}, inplace=True)
res107[u'比例'] = res107['num'] / res107['num'].sum()
res107.reset_index(inplace=True)
print(res107)


# 代码11-4 统计带"?"的数据

def countquestion(i):  # 自定义统计函数
    j = i[['fullURLId']][i['fullURL'].str.contains('\?')].copy()  # 找出类别包含107的网址
    return j


# engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/test?charset=utf8')
sql = pd.read_sql('all_gzdata', engine, chunksize=10000)

counts3 = [countquestion(i)['fullURLId'].value_counts() for i in sql]
counts3 = pd.concat(counts3).groupby(level=0).sum()
print(counts3)

# 求各个类型的占比并保存数据
df1 = pd.DataFrame(counts3)
df1['perc'] = df1['fullURLId'] / df1['fullURLId'].sum() * 100
df1.sort_values(by='fullURLId', ascending=False, inplace=True)
print(df1.round(4))


# 代码11-5 统计199类型中的具体类型占比

def page199(i):  # 自定义统计函数
    j = i[['fullURL', 'pageTitle']][(i['fullURLId'].str.contains('199')) &
                                    (i['fullURL'].str.contains('\?'))]
    j['pageTitle'].fillna(u'空', inplace=True)
    j['type'] = u'其他'  # 添加空列
    j['type'][j['pageTitle'].str.contains(u'法律快车-律师助手')] = u'法律快车-律师助手'
    j['type'][j['pageTitle'].str.contains(u'咨询发布成功')] = u'咨询发布成功'
    j['type'][j['pageTitle'].str.contains(u'免费发布法律咨询')] = u'免费发布法律咨询'
    j['type'][j['pageTitle'].str.contains(u'法律快搜')] = u'快搜'
    j['type'][j['pageTitle'].str.contains(u'法律快车法律经验')] = u'法律快车法律经验'
    j['type'][j['pageTitle'].str.contains(u'法律快车法律咨询')] = u'法律快车法律咨询'
    j['type'][(j['pageTitle'].str.contains(u'_法律快车')) |
              (j['pageTitle'].str.contains(u'-法律快车'))] = u'法律快车'
    j['type'][j['pageTitle'].str.contains(u'空')] = u'空'

    return j


# 注意：获取一次sql对象就需要重新访问一下数据库
# engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/test?charset=utf8')
sql = pd.read_sql('all_gzdata', engine, chunksize=10000)  # 分块读取数据库信息
# sql = pd.read_sql_query('select * from all_gzdata limit 10000', con=engine)

counts4 = [page199(i) for i in sql]  # 逐块统计
counts4 = pd.concat(counts4)
d1 = counts4['type'].value_counts()
print(d1)
d2 = counts4[counts4['type'] == u'其他']
print(d2)
# 求各个部分的占比并保存数据
df1_ = pd.DataFrame(d1)
df1_['perc'] = df1_['type'] / df1_['type'].sum() * 100
df1_.sort_values(by='type', ascending=False, inplace=True)
print(df1_)


# 代码11-6 统计无目的浏览用户中各个类型占比

def xiaguang(i):  # 自定义统计函数
    j = i.loc[(i['fullURL'].str.contains('\.html')) == False,
              ['fullURL', 'fullURLId', 'pageTitle']]
    return j


# 注意获取一次sql对象就需要重新访问一下数据库
# engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/test?charset=utf8')
sql = pd.read_sql('all_gzdata', engine, chunksize=10000)  # 分块读取数据库信息

counts5 = [xiaguang(i) for i in sql]
counts5 = pd.concat(counts5)

xg1 = counts5['fullURLId'].value_counts()
print(xg1)
# 求各个部分的占比
xg_ = pd.DataFrame(xg1)
xg_.reset_index(inplace=True)
xg_.columns = ['index', 'num']
xg_['perc'] = xg_['num'] / xg_['num'].sum() * 100
xg_.sort_values(by='num', ascending=False, inplace=True)

xg_['type'] = xg_['index'].str.extract('(\d{3})')  # 提取前三个数字作为类别id

xgs_ = xg_[['type', 'num']].groupby('type').sum()  # 按类别合并
xgs_.sort_values(by='num', ascending=False, inplace=True)  # 降序排列
xgs_['percentage'] = xgs_['num'] / xgs_['num'].sum() * 100

print(xgs_.round(4))

# 代码11-7 统计用户浏览网页次数的情况

# 分析网页点击次数
# 统计点击次数
# engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/test?charset=utf8')
sql = pd.read_sql('all_gzdata', engine, chunksize=10000)  # 分块读取数据库信息

counts1 = [i['realIP'].value_counts() for i in sql]  # 分块统计各个IP的出现次数
counts1 = pd.concat(counts1).groupby(level=0).sum()  # 合并统计结果，level=0表示按照index分组
print(counts1)

counts1_ = pd.DataFrame(counts1)
counts1['realIP'] = counts1.index.tolist()

counts1_[1] = 1  # 添加1列全为1
hit_count = counts1_.groupby('realIP').sum()  # 统计各个“不同点击次数”分别出现的次数
# 也可以使用counts1_['realIP'].value_counts()功能
hit_count.columns = [u'用户数']
hit_count.index.name = u'点击次数'

# 统计1~7次、7次以上的用户人数
hit_count.sort_index(inplace=True)
hit_count_7 = hit_count.iloc[:7, :]
time = hit_count.iloc[7:, 0].sum()  # 统计点击次数7次以上的用户数
hit_count_7 = hit_count_7.append([{u'用户数': time}], ignore_index=True)
hit_count_7.index = ['1', '2', '3', '4', '5', '6', '7', '7次以上']
hit_count_7[u'用户比例'] = hit_count_7[u'用户数'] / hit_count_7[u'用户数'].sum()
print(hit_count_7)

# 代码11-8 分析浏览次数为一次的用户的行为

# 分析浏览一次的用户行为

engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/test?charset=utf8')
all_gzdata = pd.read_sql_table('all_gzdata', con=engine)  # 读取all_gzdata数据

# 对realIP进行统计
# 提取浏览1次网页的数据
real_count = all_gzdata.groupby("realIP")['realIP'].count()
real_count = pd.DataFrame(real_count)
real_count.columns = ["count"]
# real_count["realIP"] = real_count.index.tolist()
real_count = real_count.reset_index()
user_one = real_count[(real_count["count"] == 1)]  # 提取只登录一次的用户
# 通过realIP与原始数据合并
real_one = pd.merge(user_one, all_gzdata, left_on="realIP", right_on="realIP")

# 统计浏览一次的网页类型
URL_count = pd.DataFrame(real_one.groupby("fullURLId")["fullURLId"].count())
URL_count.columns = ["count"]
URL_count.sort_values(by='count', ascending=False, inplace=True)  # 降序排列
# 统计排名前4和其他的网页类型
URL_count_4 = URL_count.iloc[:4, :]
time = hit_count.iloc[4:, 0].sum()  # 统计其他的
URLindex = URL_count_4.index.values
URL_count_4 = URL_count_4.append([{'count': time}], ignore_index=True)
URL_count_4.index = [URLindex[0], URLindex[1], URLindex[2], URLindex[3],
                     '其他']
URL_count_4[u'比例'] = URL_count_4['count'] / URL_count_4['count'].sum()
print(URL_count_4)

# 代码11-9 统计单用户浏览次数为一次的网页

# 在浏览1次的前提下, 得到的网页被浏览的总次数
fullURL_count = pd.DataFrame(real_one.groupby("fullURL")["fullURL"].count())
fullURL_count.columns = ["count"]
fullURL_count = fullURL_count.reset_index()
fullURL_count.sort_values(by='count', ascending=False, inplace=True)  # 降序排列
print(fullURL_count)
