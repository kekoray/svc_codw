

# re模块  
import re 

# 匹配以给定条件开头的字符串
print(re.match("www", "www.koray2021.ml").group())     # www

# 在整个字符串中寻找匹配规则的字符串
print(re.search("www", "yuiwwwyuiswww.ml"))     # <re.Match object; span=(3, 6), match='www'>
print(re.search("www", "yuiwwwyuiswww.ml").group())     # www
print(re.search("www", "yuiwwwyuiswww.ml").span())     # (3, 6) 跨度,包头不包尾

# 查找字符串中所有出现的正则表达式模式,返回列表
print(re.findall("w", "adjawadjw79w"))     # ['w', 'w', 'w']

# 字符串替换
print(re.sub(r"\d+", "101","abc = 22"))     # abc = 101

# 字符串切割
print(re.split("\.", "www.koray2021.ml"))     # ['www', 'koray2021', 'ml']

# 编译正则表达式,获得一个正则表达式对象,即提前写好正则规则
pattem = re.compile("\.")
print(pattem.split("www.koray2021.ml"))     # ['www', 'koray2021', 'ml']


 
print()
print()