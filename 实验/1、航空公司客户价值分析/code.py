from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('data.xls')
data = (data - data.mean()) / data.std()
data.to_excel('tmp/standard_data.xls', index=False)

# data = StandardScaler().fit_transform(data)
# np.save('tmp/standard_data.np', data)
# np.savetxt('tmp/standard_data.csv', data)
# standard_data = np.load('standard_data.np.npy')


standard_data = pd.read_excel('tmp/standard_data.xls')

kmeans_model = KMeans(n_clusters=5, random_state=123).fit(standard_data)
kmeans_centers = kmeans_model.cluster_centers_
kmeans_labels = kmeans_model.labels_

centers = pd.DataFrame(kmeans_centers, columns=standard_data.columns)
labels = ['L', 'R', 'F', 'M', 'C']
legend = ['客户类别' + str(i + 1) for i in centers.index]
center = pd.concat([centers, centers['L']], axis=1).values

n = len(legend)
angle = np.linspace(0, 2 * np.pi, n, endpoint=False)
angles = np.concatenate((angle, [angle[0]]))

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, polar=True)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

for i in range(n):
    ax.plot(angles, center[i])

ax.set_thetagrids(angle * 180 / np.pi, labels)
plt.title('聚类中心特征图')
plt.legend(legend)
plt.savefig('tmp/image.png')
plt.show()


data['labels'] = kmeans_labels
counts = data.labels.value_counts()
centers['counts'] = counts

writer = pd.ExcelWriter('tmp/cluster_result.xls')
data.to_excel(writer, sheet_name='类标号', index=False)
centers.to_excel(writer, sheet_name='聚类中心')
writer.save()
writer.close()
