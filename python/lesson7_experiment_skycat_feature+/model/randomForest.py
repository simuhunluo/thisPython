# -*- coding: UTF-8 -*-
import h2o
from h2o.estimators.random_forest import H2ORandomForestEstimator
h2o.init()
trainData = h2o\
    .import_file("K:\\thisPython\python\lesson7_experiment_skycat_feature+\model\\trainDataSet.csv.csv")
testData = h2o.import_file("K:\\thisPython\python\lesson7_experiment_skycat_feature+\model\\testDataSet.csv.csv")
realTrainData=trainData[2:64]#不选取第1、2和最后一列
model = H2ORandomForestEstimator(ntrees=100, max_depth=100)
model.train(x=realTrainData.names,y='tag',training_frame=trainData)
pre_tag = H2ORandomForestEstimator.predict(model, testData)
pre_and_test=pre_tag.cbind(testData)
print pre_and_test[0:4].head()
# 计算准确率
n = pre_and_test.nrow
# 预测的数目
pre_n = pre_and_test[(pre_and_test['predict'] > 0.5), :].nrow
print pre_n
# 实际的数目
act_n = pre_and_test[(pre_and_test['tag'] == 1), :].nrow
print act_n
# 预测和实际一致的
target_n = pre_and_test[(pre_and_test['predict'] > 0.5) & (pre_and_test['tag'] == 1), :].nrow
print target_n
target_n = float(target_n)
pre_n = float(pre_n)
act_n = float(act_n)
precision = target_n / pre_n
recall = target_n / act_n
F1 = 2 * precision * recall / (precision + recall)
print "F1:"
print F1
