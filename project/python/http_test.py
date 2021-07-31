
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
# response =  requests.get("https://www.baidu.com/",headers=headers,params=kw)
# # post请求
# # response = requests.post(url,headers)

# # 查看URL
# print(response.url)     # https://www.baidu.com/?wd=python

# # 获取请求状态码
# print(response.status_code)     # 200
# # 获取请求头
# print(response.headers)
# #
# print(response.encoding)
# # 获取
# # print(response.text)
# # print(response.content.decode())


#  ====================  案例
import requests
from urllib import parse
import json
import pandas as pd
import matplotlib.pyplot as plt

# url = 'https://api.inews.qq.com/newsqa/v1/automation/foreign/daily/list?country=%E7%BE%8E%E5%9B%BD&'

# 解析url
# https://api.inews.qq.com/newsqa/v1/automation/foreign/daily/list?country=美国&
# print(parse.unquote(url))

# url = 'https://api.inews.qq.com/newsqa/v1/automation/foreign/daily/list?country=%s&'
# country = input("请输入查询国家 : ")
# print("爬取url解析 : ", url % (parse.quote(country)))


URL = 'https://api.inews.qq.com/newsqa/v1/automation/foreign/daily/list?country=%s&'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Origin': 'https://news.qq.com',
    'Referer': 'https://news.qq.com/'
}


def get_respones(country):
    url = URL % (parse.quote(country))
    print("爬取url解析 : ", url)
    data = {"country": country, }
    respones = requests.post(url, data=data, headers=headers)
    return respones


# if __name__ == "__mian__":

# country = input("请输入查询国家 : ")
country = "美国"
res = get_respones(country)
# print(res.text)

data = json.loads(res.text)
# print(data['data'])

df = pd.DataFrame(data['data'])
print(df)

plt.figure(figsize=(10, 8))
plt.plot([i for i in range(551)], df["confirm"])
plt.show()
