# pandas

import pandas
import numpy


# 创建series
# 1.数组创建,默认带索引
r1 = pandas.Series(numpy.array(["a", "b", "c"]))
print(r1)
# 0    a
# 1    b
# 2    c
# dtype: object


# 2.字典创建,索引为字典的键
r2 = pandas.Series({1: "a", 2: "b", 3: "c"})
print(r2)
# 1    a
# 2    b
# 3    c
# dtype: object

# 获取series属性
print(r1.values)    # ['a' 'b' 'c']
print(r1.index)     # RangeIndex(start=0, stop=3, step=1)


# dateframe
# 创建dateframe

# 1.
dates = pandas.date_range("2021-01-01", periods=7)
df1 = pandas.DataFrame(numpy.random.randn(
    7, 5), index=dates, columns=list("ABCDE"))
print(df1)
#                    A         B         C         D         E
# 2021-01-01  0.179104  0.638528  0.914919  0.398283  0.355321
# 2021-01-02  1.446824 -1.718512  0.279211  0.763067 -0.043381
# 2021-01-03 -1.428293 -0.751160 -0.455070 -0.726809  0.752122
# 2021-01-04 -1.501621 -1.050230  2.207411 -0.398285 -0.528348
# 2021-01-05 -0.007814  0.929894 -0.269024  0.563109  0.567269
# 2021-01-06  0.294577  0.441871 -0.022372  1.457020  0.111319
# 2021-01-07 -1.576160 -1.055194 -0.162669 -2.183711  0.809824


# 2.通过字典形式创建
df2 = pandas.DataFrame({'A': 1.,
                        'B': pandas.Timestamp('2021-01-01'),
                        "C": pandas.Series(1, list(range(4)), dtype='float32'),
                        "D": numpy.array([3]*4),
                        "E": 'foo'})

print(df2)
#      A          B    C  D    E
# 0  1.0 2021-01-01  1.0  3  foo
# 1  1.0 2021-01-01  1.0  3  foo
# 2  1.0 2021-01-01  1.0  3  foo
# 3  1.0 2021-01-01  1.0  3  foo


# 获取dataframe数据
print(df2['A'])

# iloc只能通过行号索引获取
print(df2.iloc[0])



# 常用操作  =======

# 数据对齐


# 映射

# 排序

# 删除
# 合并
# 还原索引,让隐藏的索引变为一列可以操作的数据

# 获取数据详情信息
print(df2.describe())
#          A    C    D
# count  4.0  4.0  4.0
# mean   1.0  1.0  3.0
# std    0.0  0.0  0.0
# min    1.0  1.0  3.0
# 25%    1.0  1.0  3.0
# 50%    1.0  1.0  3.0
# 75%    1.0  1.0  3.0
# max    1.0  1.0  3.0



#  ===============  pd常用统计方法  ========


# 缺失值处理
#  替换
#  删除

