
# 安装工具库
# pip install XXX


# Numpy是python在数据分析领域中不可或缺的工具,是pandas,scikit-learn等工具包的基础
# 并提供了ndarray,matrix和ufunc

import numpy as np
# 创建数组
np.array([2,5,7]) 
np.arange(5)     # array([0, 1, 2, 3, 4])
np.zeros(2)     # array([0., 0.])
np.ones(2)     # array([1., 1.])
np.linspace(1,2)     
""" 
array([1.        , 1.02040816, 1.04081633, 1.06122449, 1.08163265,
       1.10204082, 1.12244898, 1.14285714, 1.16326531, 1.18367347,
       1.20408163, 1.2244898 , 1.24489796, 1.26530612, 1.28571429,
       1.30612245, 1.32653061, 1.34693878, 1.36734694, 1.3877551 ,
       1.40816327, 1.42857143, 1.44897959, 1.46938776, 1.48979592,
       1.51020408, 1.53061224, 1.55102041, 1.57142857, 1.59183673,
       1.6122449 , 1.63265306, 1.65306122, 1.67346939, 1.69387755,
       1.71428571, 1.73469388, 1.75510204, 1.7755102 , 1.79591837,
       1.81632653, 1.83673469, 1.85714286, 1.87755102, 1.89795918,
       1.91836735, 1.93877551, 1.95918367, 1.97959184, 2.        ]) """



a = np.arange(10)     # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
a[1]     # 1
a[0:3]     # array([0, 1, 2])

# 类似切片参数设定
s = slice(0,3)
a[s]     # array([0, 1, 2])


# 数据的切片与索引

a = np.array([[0,1,2],[3,4,5],[6,7,8]])
#  [[0 1 2]
#   [3 4 5]
#   [6 7 8]]

a[:2,:3]   # array([[0, 1, 2], [3, 4, 5]])
a[2]       # array([6, 7, 8])
a[2,:]     # array([6, 7, 8])
a[2:,:]    # array([[6, 7, 8]])

# 通过布尔运算得结果
a[a>6]     # array([7, 8])


# 数组的广播
# 广播是指...  多维数组的运算

a = np.array([[1,2],[3,4]])
b = np.array([1,2] )

# print(a+b )
# [[2 4]
#  [4 6]]

print(a+5 )
# [[6 7]
#  [8 9]]



# 数组常用操作

np.reshape(a, newshape)


# ufunc运算

# random模块
np.random.rand()
np.randomr.randn()
np.random.randint()








