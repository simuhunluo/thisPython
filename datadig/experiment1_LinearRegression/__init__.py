# -*-encoding=utf-8-*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
from sklearn import linear_model

"""
（1）获取数据并进行数据预处理，将含有缺失值的样本去掉，取出死亡率在0<q<=1范围内的数据。
（2）完成数据的描述和研究对象的分布类型中的分析过程，利用python绘制相关的散点图等。
（3）根据分析结果，利用年龄、年份和生存人数这3个变量与死亡人数之间的关系，利用普通最小二乘线性
模型进行模型拟合，并进行预测；将观测值与拟合值，进行图形展示（以样本的观测值做为x轴，拟合值作
为y轴绘制散点图） 。
"""
data = pd.read_csv("death_rate.csv")

data = data.dropna()
data = data.loc[(data['q_male'] <= 1) & (data['q_male'] > 0)]
data = data.loc[:, ['Year', 'Age', 'Male_Exp', 'q_male', 'Male_death', 'L_male_exp']]
#                    年份    年龄   男性存活人数 男性死亡率  男性死亡人数   存活人数的对数
# print data
# 数据的描述
# 年龄和男性死亡率的散点图
# plt.plot(data['Age'], np.log2(data['q_male']), 'bo')
# plt.rc('font', family='STXihei', size=15)
# plt.ylabel('q_male')
# plt.xlabel('Age')
# plt.title('Age&q_male')
# plt.grid(color='#95a5a6', linestyle='--', linewidth=3, axis='both', alpha=0.4)
# plt.show()
# 年龄与生存人口对数的散点图
# plt.plot(data['Age'], data['L_male_exp'], 'ro')
# plt.rc('font', family='STXihei', size=15)
# plt.ylabel('L_male_exp')
# plt.xlabel('Age')
# plt.title('Age&L_male_exp')
# plt.grid(color='#95a5a6', linestyle='--', linewidth=3, axis='both', alpha=0.4)
# plt.show()
# 年份与男性死亡率之间的关系
# plt.plot(data['Year'], np.log2(data['q_male']), 'bo')
# plt.rc('font', family='STXihei', size=15)
# plt.ylabel('q_male')
# plt.xlabel('Year')
# plt.title('Year&q_male')
# plt.grid(color='#95a5a6', linestyle='--', linewidth=3, axis='both', alpha=0.4)
# plt.show()

# 研究对象的分布类型
# the histogram of the data
# plt.hist(data['Male_death'], 100, normed=1, facecolor='g', alpha=0.75)
# plt.xlabel('Male_death')
# plt.ylabel('Density')
# plt.title('Histogram of the data')
# plt.axis([0, 2000, 0, 0.006])
# plt.grid(True)
# plt.show()
# the histogram of the data()log
# plt.hist(np.log2(data['Male_death']), 100, normed=1, facecolor='g', alpha=0.75)
# plt.xlabel('Smarts')
# plt.ylabel('Probability')
# plt.title('Histogram of log')
# plt.axis([0, 11, 0, 0.3])
# plt.grid(True)
# plt.show()
"""
（3）根据分析结果，利用年龄、年份和生存人数这3个变量与死亡人数之间的关系，利用普通最小二乘线性
模型进行模型拟合，并进行预测；将观测值与拟合值，进行图形展示（以样本的观测值做为x轴，拟合值作
为y轴绘制散点图） 。
"""
X_train, X_test, y_train, y_test = train_test_split(data.loc[:, ['Age','Year','Male_Exp']], data['Male_death'],
                                                    test_size=0.25, random_state=41)
lr = linear_model.LinearRegression()
lr.fit(X_train, y_train)
print('intercept_:%.3f' % lr.intercept_)
print('score: %.3f' % lr.score(X_test,y_test))
# plt.scatter(X_test['Age'], y_test, color='green')
plt.plot(y_test, lr.predict(y_test), 'bo')
plt.show()

