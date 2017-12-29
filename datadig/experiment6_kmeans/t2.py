# -*- coding: UTF-8 -*-
"""
作者:scc
时间：2017年    月   日
实现功能：
"""
from sklearn.decomposition import PCA
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

pca = PCA(n_components=2)
tripData = pd.read_csv("K:\\thisPython\datadig\experiment6_kmeans\\trip.csv")
kMeansData = pd.read_csv("K:\\thisPython\datadig\experiment6_kmeans\\new_df.csv")
data = tripData.iloc[:, 2:]
kMeansData = kMeansData.loc[:, 'jllabel']
xy = pca.fit_transform(data)
new_pca = pd.DataFrame(xy, columns=['x', 'y'])
print "降维后的数据："
print new_pca.head(10)
label = np.array(kMeansData)
new_pca['label'] = kMeansData
# 绘图
f1 = plt.figure(1)
label0 = np.array(new_pca[new_pca['label'] == 0])
label1 = np.array(new_pca[new_pca['label'] == 1])
label2 = np.array(new_pca[new_pca['label'] == 2])
plt.plot(label0[:, 0], label0[:, 1], 'ro')
plt.plot(label1[:, 0], label1[:, 1], 'go')
plt.plot(label2[:, 0], label2[:, 1], 'bo')
plt.savefig("kmeans.png")
plt.show()
