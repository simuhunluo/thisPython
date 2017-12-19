# -*- encoding=utf-8 -*-
import numpy as np

"""
（1）用0~19的数字生成(4,5)的数组命名为a,查看a的维度；查看a的轴的个数；查看a元素的总个数;
查看a中每个元素的字节大小。
（2）创建元素为1,2,3,4的(2,2)的数组 b，查看b中元素类型。
（3）创建一个全1的（4,4）的数组c;创建一个内容随机的(3,2)数组d，并打印d。
（4）
（5）生成一个3个元素的数组n2,通过常用函数计算每个元素的平方根；每个元素的标准差。
（6）生成一个9个（可以从0~8）元素的数组n3,计算每个元素的平方；取出位置2的元素；取出位置2至5
之间的元素。
（7）随机生成2个3*3的数组n4和n5，将n4和n5进行垂直合并形成n6;将n4和n5进行水平合并形成n7。
（8）创建一个2行3列的零矩阵命名为z,将z的2行3列的位置值置成1。
（9）生成4*4的对角矩阵，以[1,2,3,4]为对角线,其他位置用0填充，命名为z1 。
（10）用0~8的数，创建成3*3的矩阵，命名为z2;用随机数，创建4*4的矩阵，命名为z3。
"""
# 1
a = np.arange(20).reshape(4, 5)
print a.ndim  # 维度 轴
print a.size  # 元素个数
print a.itemsize  # 单个元素的大小
# 2
b = np.array([1, 2, 3, 4]).reshape(2, 2)
print b.dtype
# 3
c = np.ones([4, 4])
print c
d = np.random.random([3, 2])
print d
# 4 用0~11的数，创建一个3*4的数组n1，计算每一列的和；计算每一行的最小值。
n1 = np.arange(12).reshape(3, 4)
print n1
print n1.sum(axis=0)
print n1.min(axis=1)
# （5）生成一个3个元素的数组n2,通过常用函数计算每个元素的平方根；每个元素的标准差。
n2 = np.array([3, 6, 8])
print np.sqrt(n2)
print np.std(n2, axis=0)
# （6）生成一个9个（可以从0~8）元素的数组n3,计算每个元素的平方；取出位置2的元素；取出位置2至5之间的元素。
n3 = np.arange(9)
print np.square(n3)
print n3[2]
print n3[2:5]
# （7）随机生成2个3*3的数组n4和n5，将n4和n5进行垂直合并形成n6;将n4和n5进行水平合并形成n7。
n4 = np.random.random([3, 3])
n5 = np.random.random([3, 3])
n6 = np.vstack((n4, n5))
print n6
n7 = np.hstack((n4, n5))
print n7
# （8）创建一个2行3列的零矩阵命名为z,将z的2行3列的位置值置成1。
z = np.zeros([2, 3])
print z
z[1][2] = 1
print z
# （9）生成4*4的对角矩阵，以[1,2,3,4]为对角线,其他位置用0填充，命名为z1 。
z1 = np.diag([1, 2, 3, 4])
print z1
# （10）用0~8的数，创建成3*3的矩阵，命名为z2;用随机数，创建4*4的矩阵，命名为z3。
z2 = np.arange(9).reshape(3, 3)
print z2
z3 = np.random.random([4, 4])
print z3
