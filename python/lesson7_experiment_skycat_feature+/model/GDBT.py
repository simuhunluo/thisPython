# -*- coding: UTF-8 -*-
from sklearn.ensemble import GradientBoostingRegressor
import pandas as pd
test_data = pd \
    .read_csv("K:\\thisPython\python\lesson7_experiment_skycat_feature+\model\\testDataSet.csv")
train_data = pd \
    .read_csv("K:\\thisPython\python\lesson7_experiment_skycat_feature+\model\\trainDataSet.csv")
X_train = train_data.iloc[:, 2:64]
y_train = train_data.loc[:, ['tag']]
X_test = test_data.iloc[:, 2:64]
y_test = test_data.loc[:, ['tag']]
gbdt = GradientBoostingRegressor(
    loss='ls'
    , learning_rate=0.1
    , n_estimators=100
    , subsample=1
    , min_samples_split=2
    , min_samples_leaf=1
    , max_depth=3
    , init=None
    , random_state=None
    , max_features=None
    , alpha=0.9
    , verbose=0
    , max_leaf_nodes=None
    , warm_start=False
)
gbdt.fit(X_train, y_train)
pred = gbdt.predict(X_test)
pred = pd.DataFrame(pred, columns=['pre'])
print pred.shape
print pred
test_data['pre'] = pred
print test_data.shape
# print test_data
# tag为1的个数
tag_n = test_data[test_data['tag'] == 1].shape[0]
print tag_n
# #pre中1的个数
pre_n = test_data[test_data['pre'] >= 0.5].shape[0]
print pre_n
# pre==1并且tag==1的个数
pre_tag_n = test_data[(test_data['pre'] >= 0.5) & (test_data['tag'] == 1)].shape[0]
print pre_tag_n
tag_n = float(tag_n)
pre_n = float(pre_n)
pre_tag_n = float(pre_tag_n)
precision = pre_tag_n / pre_n
recall = pre_tag_n / tag_n
F1 = 2 * precision * recall / (precision + recall)
print F1
