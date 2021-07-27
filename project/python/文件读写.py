# 文件读写

# open(filename,mode(文件打开模式),encoding(编码格式))

# 读取 ========
import pandas as pd
import cv2
f = open('book.txt', 'r')
# 读取全部内容
print(f.read())
# 返回文件中的制定大小的内容
print(f.read(10))
# 一次只读一行
print(f.readline())     # 123456
# 按行读取所有,返回列表,每一项为一个f.readline()
print(f.readlines())     # ['123456\n', '7890\n', 'abcdefg ']
# 返回当前文件读取位置
print(f.tell())


# 写入 ========
# 覆盖写入
d = open('book.txt', 'w')
# 追加写入
d = open('book.txt', 'a')
# 写入字符串数据
d.write("write...\n")

# 定位文件读写位置,off表示偏移量,where为0表示起始位置开始,1表示当前位置,2表示结尾位置
print(d.seek(3, 0))


# 将缓存内容写入硬盘
f.flush()

# # 关闭文件
f.close()


#  =======================================================
# with: 上下文管理器,自动关闭文件,不需要调用close
with open('book.txt', 'r') as w:
    pass

# 常见文件格式操作


# 1.图片文件
# 读取图片,读取模式是*b的二进制读取方式,返回图片的二进制数据
with open('img.jpg', 'rb') as w:
    print(w.read())

# 使用

# 2.音频文件


# 3.数据文件
# csv格式
pd.read_csv("....csv", names=["name,age"])



