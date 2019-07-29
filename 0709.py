#coding=utf-8
# import uniout

# author: Huan Shuwen
# time : 2019/7/9 下午8:02
# file : 0709
"""
NOTICE:

"""
import urllib.request
# url = 'http://www.baidu.com'
# response = urllib.request.urlopen(url)
# print(dict(response.getheaders()))
# print(response.read())
# print(response.read().decode())
# print(response.geturl())
# print(response.getcode())# 状态码
# print(response.readlines())

# with open('baidu1.html','wb') as fp:
#     fp.write(response.read())

# image_url='https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1563280295&di=d1bf1c25c64719c7e62583348c58ccc4&imgtype=jpg&er=1&src=http%3A%2F%2Fdik.img.kttpdq.com%2Fpic%2F13%2F8791%2F1b33a602c5282b75.jpg'
# response = urllib.request.urlopen(image_url)
# # 图片只能二进制本地
# with open('流氓兔.jpg','wb') as fp:
#     fp.write(response.read())

# urllib.request.urlretrieve(image_url,'image.jpg')
# image_url='https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1562685849217&di=7c89d3224316fc86bbd1fc546f3508d4&imgtype=0&src=http%3A%2F%2Fe.hiphotos.baidu.com%2Fexp%2Fw%3D500%2Fsign%3Da3769f05222dd42a5f0901ab333a5b2f%2F2fdda3cc7cd98d1075b5c65d263fb80e7bec907d.jpg'
# url='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%91%A8%E6%9D%B0%E4%BC%A6&oq=%25E6%25B5%2581%25E6%25B0%2593%25E5%2585%2594&rsv_pq=b5195e06001996b8&rsv_t=d3b8UuG2VomM5Zye1G1jz%2BguSPn6hHLUWb2NRInp0CurZ9oE2U4Y%2BS1U3jU&rqlang=cn&rsv_enter=1&inputT=1693&rsv_sug3=21&rsv_sug1=19&rsv_sug7=100&bs=%E6%B5%81%E6%B0%93%E5%85%94'
import urllib.parse
# quote 编码 中文->%xx
# unquote 解码 %xx->中文
# urllib.parse.urlencode 给字典拼接参数并且把非法字符进行编码


# get
import urllib.request
import urllib.parse










