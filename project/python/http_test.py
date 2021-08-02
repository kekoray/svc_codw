
# requests模块是HTTP请求库

""" 
URL概述
URL(Uniform Resource Locator,统一资源定位器),它是WWW的统一资源定位标志,就是指网络地址

基本格式:
schema://host[:port#]/path/.../[?query-string][#anchor]


 """
import requests


# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}

# kw = {"wd" : "python"}

# # get请求
response =  requests.get("https://www.baidu.com/",headers=headers,params=kw)
# # post请求
# # response = requests.post(url,headers)

# # 查看URL
# print(response.url)     # https://www.baidu.com/?wd=python

   



""" Response对象 """

# 返回响应主体,Unicode类型数据,主要取文本
response.text
# 返回响应主体,bytes的二进制数据,主要取图片和文件等,中文显示为字符
response.content
# 返回状态码
response.status_code  
# 返回状态原因
response.reason
# 返回响应头
response.headers
# 返回请求消息的报头
response.request.headers
# 返回编码方式
response.encoding
# 返回cookies
response.cookies
# 返回请求的URL
response.url
response.history
response.raw

# 失败请求抛出异常
response.raise_for_status()



response.content.decode("utf-8")



