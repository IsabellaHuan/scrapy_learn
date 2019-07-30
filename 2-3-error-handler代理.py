#coding=utf-8

# author: Huan Shuwen
# time : 2019/7/30 下午7:37
# file : 2-3-error-handler代理
"""
NOTICE:
Handler
Opener
"""
# -----------基本用法
# import urllib.request
# import urllib.parse
# url = 'http://www.baidu.com/'
# headers = {
# 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
# }
# # 创建handler
# handler = urllib.request.HTTPHandler()
# # 使用handler构建opener
# opener = urllib.request.build_opener(handler)
# # opener是对象，直接用其方法就行
# # 构建请求对象
# request = urllib.request.Request(url=url,headers=headers)
# # 发送请求
# response = opener.open(request)
# print(response.read().decode())
# -----------代理
# 程序中的代理：正向代理【替客户端发送请求，获取数据】、反向代理【代理总服务器，提供数据
