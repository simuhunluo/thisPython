# -*-encoding=utf-8-*-
import h2o
from h2o.estimators.random_forest import H2ORandomForestEstimator

h2o.init()
trainData = h2o.import_file("C:\Users\scc\PycharmProjects\untitled1\datadig4\lesson2\\train.csv")
testData = h2o.import_file("C:\Users\scc\PycharmProjects\untitled1\datadig4\lesson2\\test.csv")
realTrainData = trainData[2:15]  # 不选取第1、2和最后一列

m = 0
n = 0
res = 0
for i in (5, 20):
    for j in (5, 20):
        model = H2ORandomForestEstimator(ntrees=i, max_depth=j)
        model.train(x=realTrainData.names, y='target', training_frame=trainData)
        pre_tag = H2ORandomForestEstimator.predict(model, testData)
        pre_tag.head()
        pre_and_test = pre_tag.cbind(testData)
        print pre_and_test[0:10].head()
        # 计算准确率
        n = pre_and_test.nrow
        # 预测的数目
        pre_n = pre_and_test[(pre_and_test['predict'] > 0.5), :].nrow
        print pre_n
        # 实际的数目
        act_n = pre_and_test[(pre_and_test['target'] == 1), :].nrow
        print act_n
        # 预测和实际一致的
        target_n = pre_and_test[(pre_and_test['predict'] > 0.5) & (pre_and_test['target'] == 1), :].nrow
        # accuracy = float(target_n) / float(n)
        print target_n
        target_n = float(target_n)
        pre_n = float(pre_n)
        act_n = float(act_n)
        precision = target_n / pre_n
        recall = target_n / act_n
        F1 = 2 * precision * recall / (precision + recall)
        if res < F1:
            res = F1
            m=i
            n=j

print "--------------------------------------------------------"
print res
print i
print j