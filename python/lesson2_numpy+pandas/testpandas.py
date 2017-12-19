# -*- encoding=utf-8 -*-
import pandas as pd

"""
（1）通过pandas包将数据flight.csv读取成dataframe，命名为df，然后进行操作。
（2）进行数据观察：查看数据的条数，查看各字段的类型，查看数据框的头尾部分的数据，查看数据的字
段，查看数据的概况；对缺失值数据，进行填充，填充值为0。
（3）按字段取出‘date’’dist’和‘flight’形成新的df1；按位置选取数据框的行为3和4，列为0,1的数
据形成新的df2；
（4）在原始的df中添加一列‘low_dest’，内容是‘dest’这列的字符串的小写形式
（5）从原始的df中选取‘dist’大于1000并且小于1200的数据作为一个新的df3，再从原始数据中选取
‘time’大于100数据做为新的df4，然后将df3和df4，按行合并为一个数据框,命名为df5
（6）取出df3中的‘time’,‘dist’这两列做为df6，求出df6中每列中最大值与最小值的差值（对数据运
用函数的方式）
（7）将df根据“dest”分组，统计各目的地，都有多少条数据，命名为“dest_count”，然后将“dest”
和“dest_count”组成新的dataframe命名为df7（提示计算条数用np.size ）
（8）分别将df5和 df7保存到本地文件，文件名分别为df5.csv和df7.csv
"""
#1
df = pd.read_csv("flight.csv")
# （2）进行数据观察：查看数据的条数，查看各字段的类型，查看数据框的头尾部分的数据，查看数据的字段，查看数据的概况；对缺失值数据，进行填充，填充值为0。
print df.count()
print df.dtypes
print df.head()
print df.tail()
df.fillna(0)
# （3）按字段取出‘date’’dist’和‘flight’形成新的df1；按位置选取数据框的行为3和4，列为0,1的数据形成新的df2；
df1 = df.loc[:, ['date', 'dist', 'flight']]
print df1
df2 = df.iloc[[3, 4], [0, 1]]
print df2
# （4）在原始的df中添加一列‘low_dest’，内容是‘dest’这列的字符串的小写形式
df['low_dest'] = df['dest'].str.lower()
print df
# （5）从原始的df中选取‘dist’大于1000并且小于1200的数据作为一个新的df3，再从原始数据中选取‘time’大于100数据做为新的df4，然后将df3和df4，按行合并为一个数据框,命名为df5
df3 = df[(df['dist'] > 1000) & (df['dist'] < 1200)]
print df3
df4 = df[df['time'] > 100]
print df4
df5 = pd.merge(df3, df4)
print df5
# 6）取出df3中的‘time’,‘dist’这两列做为df6，求出df6中每列中最大值与最小值的差值（对数据运用函数的方式）
df6 = df3.loc[:, ['time', 'dist']]
print df6


def get_max_min_dif(max, min):
    return (max - min)


print get_max_min_dif(max(df6['time']), min(df6['time']))
# （7）将df根据“dest”分组，统计各目的地，都有多少条数据，命名为“dest_count”，然后将“dest”和“dest_count”组成新的dataframe命名为df7（提示计算条数用np.size ）

dest_count = df.groupby(df['dest']).size()
print dest_count
df7 = pd.DataFrame(dest_count, columns=['dest_count'])
print df7
# （8）分别将df5和 df7保存到本地文件，文件名分别为df5.csv和df7.csv

df5.to_csv("df5.csv")
df7.to_csv("df7.csv")
