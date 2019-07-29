#coding=utf-8

# author: Huan Shuwen
# time : 2019/7/16 下午7:45
# file : 2-2-1-ajax
"""
NOTICE:

"""

# import urllib.request
# import urllib.parse
#
# url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'
#
# page = int(input('输入想要的页码:'))
# limit = int(input('显示数据量:'))
# print(page)
# print(limit)
# data={
#     'start': (page-1)*limit
#     ,'limit': limit
# }
# query_string = urllib.parse.urlencode(data)
# url+=query_string
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
# }
# request = urllib.request.Request(url=url,headers=headers)
# response = urllib.request.urlopen(request)
# print(response.read().decode())


# import urllib.request
# import urllib.parse
#
# url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
# cname = input('城市:')
# page = int(input('页码:'))
# number = int(input('数量:'))
# formdata={
# 'cname': ''
# ,'pid':''
# ,'keyword': cname
# ,'pageIndex': page
# ,'pageSize': number
# }
# headers={
# 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
# }
#
# formdata = urllib.parse.urlencode(formdata).encode()
#
# request = urllib.request.Request(url=url,headers=headers)
# response = urllib.request.urlopen(request,data=formdata)
# print(response.read().decode())


import urllib.request
import urllib.parse

url = 'http://tieba.baidu.com/f?kw=python&ie=utf-8&'

kw = int(input('搜索词:'))
start_page = int(input('起始页码:'))
end_page = int(input('结束页码:'))
number = int(input('数量:'))
formdata={
'cname': ''
,'pid':''
,'keyword': cname
,'pageIndex': page
,'pageSize': number
}
headers={
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

formdata = urllib.parse.urlencode(formdata).encode()

request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request,data=formdata)
print(response.read().decode())