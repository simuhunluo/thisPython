# -*- coding: UTF-8 -*-
from sklearn.ensemble import GradientBoostingRegressor as GBR
import pandas as pd

trainData = pd.read_csv("K:\python\lesson6_experiment2\NSW_TRAIN.csv")
testData = pd.read_csv("K:\python\lesson6_experiment2\NSW_TEST.csv")
# X_train = trainData.loc[:, ['WEEK','HOLIDAY','Min_T','Max_T','AVG_T','RAIN']]  # 6列特征
X_train = trainData.loc[:, ['WEEK', 'Min_T', 'Max_T', 'AVG_T', 'RAIN']]  # 6列特征
y_train = trainData.iloc[:, -2]  # 取平均负荷为target
X_test = testData.loc[:, ['WEEK', 'Min_T', 'Max_T', 'AVG_T', 'RAIN']]
y_test = testData.iloc[:, -2]
gbr = GBR()
gbr.fit(X_train, y_train)
pre = gbr.predict(X_test)
score = gbr.score(X_test, y_test)
print gbr.feature_importances_
pre_ele = pd.DataFrame(pre, columns=['pre_avg'])
real_ele = pd.DataFrame(y_test)
after = pd.concat([pre_ele, real_ele], axis=1)
after['error'] = abs(after['AVG_ELE'] - after['pre_avg']) / after['pre_avg']
error = after['error'].sum() / after['error'].shape[0]
error = round(error, 4)
print error
