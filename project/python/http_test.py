
# requests模块是HTTP请求库

""" 
URL概述
URL(Uniform Resource Locator,统一资源定位器),它是WWW的统一资源定位标志,就是指网络地址

基本格式:
schema://host[:port#]/path/.../[?query-string][#anchor]


 """

import requests

# get请求
# requests.get("http://lazada.menglar.com/")

# post请求
response = requests.post("http://lazada.menglar.com/")
print(response.headers)
print(response.status_code)
print(response.encoding)
print(response.text)
print(response.content)


# 异常情况
