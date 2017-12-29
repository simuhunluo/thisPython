# -*-encoding=utf-8-*-
import xgboost as xgb
import pandas as pd
test_data = pd.read_csv("K:\\thisPython\python\lesson7_experiment_skycat_feature+\model\\testDataSet.csv")
train_data = pd.read_csv("K:\\thisPython\python\lesson7_experiment_skycat_feature+\model\\trainDataSet.csv")
X_train = train_data.iloc[:, 2:64]
print X_train.head(1)
y_train = train_data.loc[:, ['tag']]
X_test = test_data.iloc[:,2:64]
y_test = test_data.loc[:, ['tag']]
param = {'max_depth': 2, 'eta': 1, 'silent': 1, 'objective': 'binary:logistic'}
xlf = xgb.XGBClassifier()
xlf.fit(X_train, y_train)
pre = xlf.predict(X_test)
pre = pd.DataFrame(pre, columns=["pre"])
print pre
test_data['pre'] = pre
print test_data.head(10)
# target中1的个数
target_n = test_data[test_data['tag'] == 1].shape[0]
print target_n
# pre中1的个数
pre_n = test_data[test_data['pre'] >= 0.5].shape[0]
print pre_n
# pre==1并且target==1的个数
pre_target_n = test_data[(test_data['pre'] >= 0.5) & (test_data['tag'] == 1)].shape[0]
print pre_target_n
target_n = float(target_n)
pre_n = float(pre_n)
pre_target_n = float(pre_target_n)
precision = pre_target_n / pre_n
recall = pre_target_n / target_n
F1 = 2 * precision * recall / (precision + recall)
print "F1:"
print F1