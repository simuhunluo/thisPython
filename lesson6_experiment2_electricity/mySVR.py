# -*- coding: UTF-8 -*-
from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import learning_curve
import pandas as pd
import numpy as np
import os

trainData = pd.read_csv(os.getcwd() + "\NSW_TRAIN.csv")
testData = pd.read_csv(os.getcwd() + "\NSW_TEST.csv")
X_train = trainData.loc[:, ['WEEK', 'Min_T', 'Max_T', 'AVG_T' ]]
y_train = trainData.iloc[:, -2]  # 取平均负荷为target
X_test = testData.loc[:, ['WEEK', 'Min_T', 'Max_T', 'AVG_T']]
y_test = testData.iloc[:, -2]
svr = GridSearchCV(SVR(kernel='rbf', gamma=0.1), cv=5,
                   param_grid={"C": [1e0, 1e1, 1e2, 1e3],
                               "gamma": np.logspace(-2, 2, 5)})
svr.fit(X_train, y_train)
pre = svr.predict(X_test)
score = svr.score(X_test, y_test)
# print pre
print score
pre_ele = pd.DataFrame(pre, columns=['pre_avg'])
real_ele = pd.DataFrame(y_test)
after = pd.concat([pre_ele, real_ele], axis=1)
after['error'] = abs(after['AVG_ELE'] - after['pre_avg']) / after['pre_avg']
error_count=after[after['error']<0.05].shape[0]
print error_count
