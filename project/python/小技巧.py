#  =======================================================

print("*"*20)

""" 小技巧 """

# 变量值互换
a = 3
b = 2
a, b = b, a

# 三元表达式(if-else简化),比较2个数字的大小
a = 8
b = 9
print(a if a > b else b)     


# 推导式生成数据
# 列表
print([i**2 for i in range(-5, 5) if i % 2])
# 集合
print({i**2 for i in range(-5, 5) if i % 2})
# 字典
print({x: y for x, y in zip(["a", "b"], (1, 2))})


# 小整数对象池
# python为了优化速度,使用[-5,256]范围的小整数对象池,避免了整数频繁申请和销毁内存空间,这些整数对象会提前建立好,不会被回收.
a = 0
b = 0
print(id(a) == id(b))     # True

# 当字符串中不存在空格和特殊字符时
c = "kk$"
d = "kk$"
print(id(c) is id(d))     # False



# 数据解包
# 需求:获取一个列表中的数据
# 1.for循环
for i in [1,2,3]:
    print(i)
# 2.使用相同数量的变量接收
a = [1,2,3]
# 3.使用星号*解包
L = [1,3,3]
print(*L)

print(0 if 1 > 66 else 99)
print(0 if 1 > 66 or 1>-1 else 99)
print(0 if 1>66 else ( 99 if 1>99 else 100 ))
print(0 if 1>66 else (99 if 1<99 else 0))