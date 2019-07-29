#coding=utf-8
# import uniout

# author: Huan Shuwen
# time : 2019/7/11 下午8:16
# file : 2-1-postt
"""
NOTICE:

"""
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context


import urllib.request
import urllib.parse

# 获取url的地址
post_url = 'https://fanyi.baidu.com/sug'
# 构建post表单数据
# word=input('输入你要查询的英文单词:')
word_list=['a','b','c','d','e','f','g']
for word in word_list:
    form_data={
        'kw':word,
    }
    # 发送请求的过程
    headers={
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    request = urllib.request.Request(url=post_url,headers=headers)
    # post数据需要转义
    form_data = urllib.parse.urlencode(form_data).encode()
    response = urllib.request.urlopen(request,data=form_data)
    print(response.read().decode())