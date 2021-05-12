import pandas as pd
import matplotlib.pyplot as plt

inputfile = '../data/input_data2.xlsx'
outputfile = '../tmp/output_data2.xlsx'
data = pd.read_excel(inputfile, index_col='id')

from sklearn.cluster import KMeans
model = KMeans(n_clusters=2, random_state=1234)
model.fit(data)

data['聚类类别'] = model.labels_
r = pd.DataFrame(model.cluster_centers_,columns=['R'])  # 找出聚类中心
r['类别数目'] = pd.Series(model.labels_).value_counts()

writer = pd.ExcelWriter(outputfile)
data.to_excel(writer, sheet_name='聚类类别')
r.to_excel(writer, sheet_name='聚类中心')
writer.save()

d = data[data['聚类类别'] == 0]
plt.plot(d['R'], [0 for i in d['R']],'r.')
d = data[data['聚类类别'] == 1]
plt.plot(d['R'], [0 for j in d['R']],'go')
plt.show()
