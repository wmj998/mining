from sklearn import datasets

iris = datasets.load_iris()
from sklearn.naive_bayes import GaussianNB

clf = GaussianNB()
clf.fit(iris.data, iris.target)
y_pred = clf.predict(iris.data)
print("Number of mislabeled points out of a total %d points:%d" % (iris.data.shape[0], (iris.target != y_pred).sum()))
