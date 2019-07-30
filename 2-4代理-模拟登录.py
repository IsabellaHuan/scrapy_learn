#coding=utf-8
# author: Huan Shuwen
# time : 2019/7/30 下午7:38
# file : 2-4代理-模拟登录
"""
NOTICE:

"""
# import urllib.request
# import urllib.parse
# # -------------代理
# # # 创建Handler
# handler = urllib.request.ProxyHandler({'http':'112.192.234.123:8088'})
# # opener
# opener = urllib.request.build_opener(handler)
#
# #创建请求
# url='http://www.baidu.com/s?wd=ip&ie=utf-8'
# headers = {
# 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
# }
# request = urllib.request.Request(url=url,headers=headers)
# response = opener.open(request)
# with open('ip.html','wb') as f:
#     f.write(response.read())
# # 125.123.122.158:9000
# # urllib.error.URLError: <urlopen error [Errno 60] Operation timed out>
# 60.191.57.78:14051
# ConnectionResetError: [Errno 54] Connection reset by peer
# 121.233.207.128:9999
# urllib.error.URLError: <urlopen error [Errno 61] Connection refused>
# ------------cookie1
# import urllib.request
# import urllib.parse
# url='https://weibo.com/6672443239/profile'
# headers = {
# 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
# }
# request = urllib.request.Request(url=url,headers=headers)
# response = urllib.request.urlopen(request)
# with open('weibo.html','wb') as fp:
#     fp.write(response.read())
# ------------cookie2
# 终极解决方案--自己抓包[自己浏览然后检查页面
# import urllib.request
# import urllib.parse
# url='https://weibo.com/6672443239/profile'
# headers = {
# 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
# 'Cookie': 'SINAGLOBAL=2878443622655.671.1562124884217; UOR=finance.ifeng.com,widget.weibo.com,www.nfcmag.com; login_sid_t=e685df070c10874dede4dade99538f80; cross_origin_proto=SSL; Ugrow-G0=d52660735d1ea4ed313e0beb68c05fc5; TC-V5-G0=28bf4f11899208be3dc10225cf7ad3c6; wb_view_log=1440*9002; _s_tentry=-; Apache=8966452316154.576.1564490442996; ULV=1564490443003:5:5:1:8966452316154.576.1564490442996:1563970425188; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFJGJv0zcY-bmd80_QbG0CI5JpX5K2hUgL.FoqcS0zXSheEe0.2dJLoIpjLxK-LBo5L12qLxK-L1K5L12BLxK-L12-LB.zt; ALF=1596026454; SSOLoginState=1564490454; SCF=AoJa7KhkDU4k07k2BLunw4Kr0kho2jzC8EHsvRf3STFsFzJqomNiKHP9ve4N8NBdOfX5WIphP5xELgn96CD8AQ4.; SUB=_2A25wREqGDeRhGeBI7FAV9C3OyDWIHXVTMDtOrDV8PUNbmtAKLVPtkW9NRmJ39C0GZntstP4EtBiKxtwxBqU0aGy-; SUHB=09PNoJZ3n9wMmP; un=18618118696; wvr=6; wb_view_log_6672443239=1440*9002; TC-Page-G0=153ff31dae1cf71cc65e7e399bfce283|1564490976|1564490970; webim_unReadCount=%7B%22time%22%3A1564491064810%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22allcountNum%22%3A5%2C%22msgbox%22%3A0%7D'
# }
# request = urllib.request.Request(url=url,headers=headers)
# response = urllib.request.urlopen(request)
# with open('weibo.html','wb') as fp:
#     fp.write(response.read())
#