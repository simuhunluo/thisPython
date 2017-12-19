# -*- encoding=utf-8-*-
import numpy as np
import urllib
from sklearn import preprocessing

url = "http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
raw_data = urllib.urlopen(url)
dataset = np.loadtxt(raw_data, delimiter=",")

X = dataset[:, 0:7]
y = dataset[:, 8]

normalized_X = preprocessing.normalize(X)  # 值域在0,1
standardized_X = preprocessing.scale(X)  # 值域不一定在0,1
# 树算法(Tree algorithms)计算特征的信息量：
from sklearn import metrics
from sklearn.ensemble import ExtraTreesClassifier

model = ExtraTreesClassifier()  # 特征选择
model.fit(X, y)
print(model.feature_importances_)
