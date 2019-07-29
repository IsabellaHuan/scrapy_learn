#coding=utf-8
# import uniout

# author: Huan Shuwen
# time : 2019/7/11 下午7:36
# file : 0711
"""
NOTICE:

"""
import urllib.request
import urllib.parse

url='http://www.baidu.com/'
#
# response = urllib.request.urlopen(url)
# print(response.read().decode())

# 伪装自己的UA,让服务端认为你是浏览器在上网
# 构建请求对象 urllib.requestt.Request()

#自己要伪装的头部
headers  ={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
}
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
print(response.read().decode())