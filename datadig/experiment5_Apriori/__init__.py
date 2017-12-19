# -*- coding: UTF-8 -*-
"""
作者:scc
时间：2017年  12  月   11日
实现功能：Apriori算法 找出频繁项集，挖掘关联规则。
算法优点:
缺点：对于大数据集跑得很慢。
"""


def loadDataSet():
    return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]


# 返回数据集中出现的单项数据集合(候选项集)，返回类型是frozenset类型为元素的集合
def createC1(dataset):
    C1 = []
    for transaction in dataset:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
    C1.sort()
    return map(frozenset, C1)


# D数据集 Ck项集
# 扫描数据集，计算项集支持度
def scanD(D, Ck, minSupport):
    ssCnt = {}
    for tid in D:
        for can in Ck:
            if can.issubset(tid):
                if not ssCnt.has_key(can):
                    ssCnt[can] = 1
                else:
                    ssCnt[can] += 1
    numitems = float(len(D))  # 数据集长度
    retList = []
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key] / numitems
        if support >= minSupport:
            retList.insert(0, key)
        supportData[key] = support
    return retList, supportData


def aprioriGen(Lk, k):
    retList = []
    lenLk = len(Lk)
    for i in range(lenLk):
        for j in range(i + 1, lenLk):
            L1 = list(Lk[i])[:k - 2];
            L2 = list(Lk[j])[:k - 2]
            L1.sort()
            L2.sort()
            if L1 == L2:
                retList.append(Lk[i] | Lk[j])
    return retList


def apriori(dataset, minsupport=0.5):
    C1 = createC1(dataset)  # 候选项集
    D = map(set, dataset)  # 数据集
    L1, supportData = scanD(D, C1, minsupport)  # 频繁项集与支持度
    L = [L1]
    k = 2
    while (len(L[k - 2]) > 0):
        Ck = aprioriGen(L[k - 2], k)
        Lk, supK = scanD(D, Ck, minsupport)
        supportData.update(supK)
        L.append(Lk)
        k += 1
    return L, supportData


dataset = loadDataSet()
print dataset
# C1=createC1(dataset)
# C1
# D=map(set,dataset)
# D
# L1,suppData0=scanD(D,C1,0.5)
# L1
L, supportData = apriori(dataset)  # 得到频繁项集 默认支持度大于0.5


# print L


# 下面是关联规则   默认最小置信度为0.7
# 主函数
def generateRules(L, supportData, minConf=0.7):
    bigRuleList = []
    for i in range(1, len(L)):  # 不处理单元素集合L[0]
        for freqSet in L[i]:
            H1 = [frozenset([item]) for item in freqSet]
            if (i > 1):  # 当集合中元素的长度大于2的时候，尝试对集合合并。
                # 比如：[2,3,5]=>{[2,3],5}
                rulesFromConseq(freqSet, H1, supportData, bigRuleList, minConf)
            else:  # 对于2元组，直接计算置信度
                calConf(freqSet, H1, supportData, bigRuleList, minConf)
    return bigRuleList


def calConf(freqSet, H, supportData, brl, minConf=0.7):
    prunedH = []
    for conseq in H:
        conf = supportData[freqSet] / supportData[freqSet - conseq]  # 置信度
        if conf >= minConf:
            print freqSet - conseq, "--->", conseq, "conf", conf
            brl.append((freqSet - conseq, conseq, conf))
            prunedH.append(conseq)
        if (len(freqSet) > 2):
            conf = supportData[freqSet] / supportData[conseq]  # 置信度
            if conf >= minConf:
                print conseq, "--->", freqSet - conseq, "conf", conf
                brl.append((conseq, freqSet - conseq, conf))
                prunedH.append(freqSet - conseq)
    return prunedH


def rulesFromConseq(freqSet, H, supportData, brl, minConf=0.7):
    m = len(H[0])
    if (len(freqSet) > (m + 1)):
        Hmp1 = aprioriGen(H, m + 1)
        Hmp1 = calConf(freqSet, Hmp1, supportData, brl, minConf)
        if (len(Hmp1) > 1):
            rulesFromConseq(freqSet, Hmp1, supportData, brl, minConf)


ruleList = generateRules(L, supportData)
# print ruleList
