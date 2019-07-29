#coding=utf-8

# author: Huan Shuwen
# time : 2019/7/15 下午8:02
# file : 2-3-post
"""
NOTICE:

"""
#
# import urllib.request
# import urllib.parse
# # import ssl
# # ssl._create_default_https_context = ssl._create_unverified_context
#
# # 获取url的地址
# post_url = 'https://fanyi.baidu.com/v2transapi'
# word_list=['baby']
# for word in word_list:
#     form_data={
#         'from': 'en'
#         ,'to': 'zh'
#         ,'query': word
#         ,'transtype': 'realtime'
#         ,'simple_means_flag': '3'
#         ,'sign': '814534.560887'
#         ,'token': 'b825b3a7cc74b7087a38946ab32c1ba1'
#     }
#     # 发送请求的过程
#     # headers = {
#     #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
#     # }
#     headers={
#     'authority': 'fanyi.baidu.com'
#     ,'method': 'POST'
#     ,'path': '/v2transapi'
#     ,'scheme': 'https'
#     ,'accept': '*/*'
#     # ,'accept - encoding': 'gzip, deflate, br'
#     ,'accept - language': 'zh - CN, zh;q = 0.9'
#     ,'content - length': '121'
#     ,'content-type':'application/x-www-form-urlencoded; charset=UTF-8'
#     ,'cookie':'BAIDUID=F9776FE9B7812341DB8CF4AD5FB613C9:FG=1; BIDUPSID=F9776FE9B7812341DB8CF4AD5FB613C9; PSTM=1562124426; MCITY=-131%3A; BDSFRCVID=zgLOJeC62GAdrTnw50LBwijvleK5xmQTH6bHUCb0lCacKZHNW6w-EG0PHf8g0KubcjP6ogKK0mOTHUuF_2uxOjjg8UtVJeC6EG0P3J; H_BDCLCKID_SF=tJFf_IPXJCP3hKDk2Rb8hJ08-UAX5-RLfa6B2p7F5l8-hl3qbb5xhRb0D-TL--cBbDJ-aK5yaxjxOKQPyhoT-68jLUQ2BhT7BHkqL56N3KJmObL9bT3v5tDSMR0q2-biWbRL2MbdQ45P_IoG2Mn8M4bb3qOpBtQmJeTxoUtbWDFKMC0me5uhe5nQDeTEb-TLbIT2BTrJabC3JR3sXU6qLT5XQPQbbq3XbbIj2po52Rc-Db5ojJ7V0q0njx57LxJatIJm3ROcyqnFSIQ6qfonDh8nbG7MJUntKD7BbIQO5hvvhb6O3M7l5fKmDloOW-TB5bbPLUQF5l8-sq0x05bke4tX-NFeJT8OfxK; delPer=0; locale=zh; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; pgv_pvi=1084395520; pgv_si=s7108737024; H_PS_PSSID=1425_21089_29522_29518_29238_28519_29098_28833_29220_29459; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; PSINO=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1562846886,1563190502; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1563190502; yjs_js_security_passport=4da041312ce1aff06647360b42b59ef5b991c386_1563190504_js'
#     ,'origin':'https://fanyi.baidu.com'
#     ,'referer':'https://fanyi.baidu.com/'
#     ,'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
#     ,'x-requested-with':'XMLHttpRequest'
#     }
#     request = urllib.request.Request(url=post_url, headers=headers)
#     # post数据需要转义
#     form_data = urllib.parse.urlencode(form_data).encode()
#     response = urllib.request.urlopen(request, data=form_data)
#     print(response.read().decode())#
# import urllib.request
# import urllib.parse
# # import ssl
# # ssl._create_default_https_context = ssl._create_unverified_context
#
# # 获取url的地址
# post_url = 'https://fanyi.baidu.com/v2transapi'
# word_list=['baby']
# for word in word_list:
#     form_data={
#         'from': 'en'
#         ,'to': 'zh'
#         ,'query': word
#         ,'transtype': 'realtime'
#         ,'simple_means_flag': '3'
#         ,'sign': '814534.560887'
#         ,'token': 'b825b3a7cc74b7087a38946ab32c1ba1'
#     }
#     # 发送请求的过程
#     # headers = {
#     #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
#     # }
#     headers={
#     'authority': 'fanyi.baidu.com'
#     ,'method': 'POST'
#     ,'path': '/v2transapi'
#     ,'scheme': 'https'
#     ,'accept': '*/*'
#     # ,'accept - encoding': 'gzip, deflate, br'
#     ,'accept - language': 'zh - CN, zh;q = 0.9'
#     ,'content - length': '121'
#     ,'content-type':'application/x-www-form-urlencoded; charset=UTF-8'
#     ,'cookie':'BAIDUID=F9776FE9B7812341DB8CF4AD5FB613C9:FG=1; BIDUPSID=F9776FE9B7812341DB8CF4AD5FB613C9; PSTM=1562124426; MCITY=-131%3A; BDSFRCVID=zgLOJeC62GAdrTnw50LBwijvleK5xmQTH6bHUCb0lCacKZHNW6w-EG0PHf8g0KubcjP6ogKK0mOTHUuF_2uxOjjg8UtVJeC6EG0P3J; H_BDCLCKID_SF=tJFf_IPXJCP3hKDk2Rb8hJ08-UAX5-RLfa6B2p7F5l8-hl3qbb5xhRb0D-TL--cBbDJ-aK5yaxjxOKQPyhoT-68jLUQ2BhT7BHkqL56N3KJmObL9bT3v5tDSMR0q2-biWbRL2MbdQ45P_IoG2Mn8M4bb3qOpBtQmJeTxoUtbWDFKMC0me5uhe5nQDeTEb-TLbIT2BTrJabC3JR3sXU6qLT5XQPQbbq3XbbIj2po52Rc-Db5ojJ7V0q0njx57LxJatIJm3ROcyqnFSIQ6qfonDh8nbG7MJUntKD7BbIQO5hvvhb6O3M7l5fKmDloOW-TB5bbPLUQF5l8-sq0x05bke4tX-NFeJT8OfxK; delPer=0; locale=zh; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; pgv_pvi=1084395520; pgv_si=s7108737024; H_PS_PSSID=1425_21089_29522_29518_29238_28519_29098_28833_29220_29459; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; PSINO=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1562846886,1563190502; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1563190502; yjs_js_security_passport=4da041312ce1aff06647360b42b59ef5b991c386_1563190504_js'
#     ,'origin':'https://fanyi.baidu.com'
#     ,'referer':'https://fanyi.baidu.com/'
#     ,'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
#     ,'x-requested-with':'XMLHttpRequest'
#     }
#     request = urllib.request.Request(url=post_url, headers=headers)
#     # post数据需要转义
#     form_data = urllib.parse.urlencode(form_data).encode()
#     response = urllib.request.urlopen(request, data=form_data)
#     print(response.read().decode())

# 输入不同，sign和token不同
# 'https://www.jianshu.com/p/0fb8a5daf617?from=timeline&isappinstalled=0'
import requests
import re
import js2py
import json
class SignAndToken:
    def __init__(self):
        #加载主页
        self.session = requests.Session()
        self.headers={
            'authority': 'fanyi.baidu.com'
            , 'method': 'POST'
            , 'path': '/v2transapi'
            , 'scheme': 'https'
            , 'accept': '*/*'
            # ,'accept - encoding': 'gzip, deflate, br'
            , 'accept - language': 'zh - CN, zh;q = 0.9'
            , 'content - length': '121'
            , 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
            ,'cookie': 'BAIDUID=F9776FE9B7812341DB8CF4AD5FB613C9:FG=1; BIDUPSID=F9776FE9B7812341DB8CF4AD5FB613C9; PSTM=1562124426; MCITY=-131%3A; BDSFRCVID=zgLOJeC62GAdrTnw50LBwijvleK5xmQTH6bHUCb0lCacKZHNW6w-EG0PHf8g0KubcjP6ogKK0mOTHUuF_2uxOjjg8UtVJeC6EG0P3J; H_BDCLCKID_SF=tJFf_IPXJCP3hKDk2Rb8hJ08-UAX5-RLfa6B2p7F5l8-hl3qbb5xhRb0D-TL--cBbDJ-aK5yaxjxOKQPyhoT-68jLUQ2BhT7BHkqL56N3KJmObL9bT3v5tDSMR0q2-biWbRL2MbdQ45P_IoG2Mn8M4bb3qOpBtQmJeTxoUtbWDFKMC0me5uhe5nQDeTEb-TLbIT2BTrJabC3JR3sXU6qLT5XQPQbbq3XbbIj2po52Rc-Db5ojJ7V0q0njx57LxJatIJm3ROcyqnFSIQ6qfonDh8nbG7MJUntKD7BbIQO5hvvhb6O3M7l5fKmDloOW-TB5bbPLUQF5l8-sq0x05bke4tX-NFeJT8OfxK; delPer=0; locale=zh; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; pgv_pvi=1084395520; pgv_si=s7108737024; H_PS_PSSID=1425_21089_29522_29518_29238_28519_29098_28833_29220_29459; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; PSINO=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1562846886,1563190502; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1563190502; yjs_js_security_passport=4da041312ce1aff06647360b42b59ef5b991c386_1563190504_js'
            , 'origin': 'https://fanyi.baidu.com'
            , 'referer': 'https://fanyi.baidu.com/'
            ,'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
            , 'x-requested-with': 'XMLHttpRequest'
        }
        self.session.headers = self.headers
        response = self.session.get("https://fanyi.baidu.com/")
        #获取token
        self.token = re.findall("token: ('.*'),",response.content.decode())[0] #相当于先请求一次，获取token
        self.token=self.token[1:-1]
        print(self.token)
        #获取gtk
        # 获取window.gtk的值。
        self.gtk = re.findall(";window.gtk = ('.*?');", response.content.decode())[0]
        #初始化Javascript脚本执行上下文环境
        self.context = js2py.EvalJs()

    def sign(self, word):
        js = r'''
            function a(r) {
                    if (Array.isArray(r)) {
                        for (var o = 0, t = Array(r.length); o < r.length; o++)
                            t[o] = r[o];
                        return t
                    }
                    return Array.from(r)
                }
                function n(r, o) {
                    for (var t = 0; t < o.length - 2; t += 3) {
                        var a = o.charAt(t + 2);
                        a = a >= "a" ? a.charCodeAt(0) - 87 : Number(a),
                            a = "+" === o.charAt(t + 1) ? r >>> a : r << a,
                            r = "+" === o.charAt(t) ? r + a & 4294967295 : r ^ a
                    }
                    return r
                }
            function e(r) {
                        var o = r.match(/[\uD800-\uDBFF][\uDC00-\uDFFF]/g);
                        if (null === o) {
                            var t = r.length;
                            t > 30 && (r = "" + r.substr(0, 10) + r.substr(Math.floor(t / 2) - 5, 10) + r.substr(-10, 10))
                        } else {
                            for (var e = r.split(/[\uD800-\uDBFF][\uDC00-\uDFFF]/), C = 0, h = e.length, f = []; h > C; C++)
                                "" !== e[C] && f.push.apply(f, a(e[C].split(""))),
                                C !== h - 1 && f.push(o[C]);
                            var g = f.length;
                            g > 30 && (r = f.slice(0, 10).join("") + f.slice(Math.floor(g / 2) - 5, Math.floor(g / 2) + 5).join("") + f.slice(-10).join(""))
                        }
                        var u = void 0
                            , l = "" + String.fromCharCode(103) + String.fromCharCode(116) + String.fromCharCode(107);
                        u ='null !== i ? i : (i = window[l] || "") || ""';
                        for (var d = u.split("."), m = Number(d[0]) || 0, s = Number(d[1]) || 0, S = [], c = 0, v = 0; v < r.length; v++) {
                            var A = r.charCodeAt(v);
                            128 > A ? S[c++] = A : (2048 > A ? S[c++] = A >> 6 | 192 : (55296 === (64512 & A) && v + 1 < r.length && 56320 === (64512 & r.charCodeAt(v + 1)) ? (A = 65536 + ((1023 & A) << 10) + (1023 & r.charCodeAt(++v)),
                                S[c++] = A >> 18 | 240,
                                S[c++] = A >> 12 & 63 | 128) : S[c++] = A >> 12 | 224,
                                S[c++] = A >> 6 & 63 | 128),
                                S[c++] = 63 & A | 128)
                        }
                        for (var p = m, F = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(97) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(54)), D = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(51) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(98)) + ("" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(102)), b = 0; b < S.length; b++)
                            p += S[b],
                                p = n(p, F);
                        return p = n(p, D),
                            p ^= s,
                        0 > p && (p = (2147483647 & p) + 2147483648),
                            p %= 1e6,
                        p.toString() + "." + (p ^ m)
                    }
                '''
        # 在javascript脚本中把u的值替换成window.gtk
        js = js.replace('\'null !== i ? i : (i = window[l] || "") || ""\'', self.gtk)
        # 执行js
        self.context.execute(js)
        # 调用函数得到sign
        return self.context.e(word)
class TranslateTool:
    def __init__(self):
        self.sign_token=SignAndToken()
        self.url="https://fanyi.baidu.com/v2transapi/"
        self.headers={
            'authority': 'fanyi.baidu.com'
            ,'method': 'POST'
            ,'path': '/v2transapi'
            ,'scheme': 'https'
            ,'accept': '*/*'
            # ,'accept - encoding': 'gzip, deflate, br'
            ,'accept - language': 'zh - CN, zh;q = 0.9'
            ,'content - length': '121'
            ,'content-type':'application/x-www-form-urlencoded; charset=UTF-8'
            ,'cookie':'BAIDUID=F9776FE9B7812341DB8CF4AD5FB613C9:FG=1; BIDUPSID=F9776FE9B7812341DB8CF4AD5FB613C9; PSTM=1562124426; MCITY=-131%3A; BDSFRCVID=zgLOJeC62GAdrTnw50LBwijvleK5xmQTH6bHUCb0lCacKZHNW6w-EG0PHf8g0KubcjP6ogKK0mOTHUuF_2uxOjjg8UtVJeC6EG0P3J; H_BDCLCKID_SF=tJFf_IPXJCP3hKDk2Rb8hJ08-UAX5-RLfa6B2p7F5l8-hl3qbb5xhRb0D-TL--cBbDJ-aK5yaxjxOKQPyhoT-68jLUQ2BhT7BHkqL56N3KJmObL9bT3v5tDSMR0q2-biWbRL2MbdQ45P_IoG2Mn8M4bb3qOpBtQmJeTxoUtbWDFKMC0me5uhe5nQDeTEb-TLbIT2BTrJabC3JR3sXU6qLT5XQPQbbq3XbbIj2po52Rc-Db5ojJ7V0q0njx57LxJatIJm3ROcyqnFSIQ6qfonDh8nbG7MJUntKD7BbIQO5hvvhb6O3M7l5fKmDloOW-TB5bbPLUQF5l8-sq0x05bke4tX-NFeJT8OfxK; delPer=0; locale=zh; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; pgv_pvi=1084395520; pgv_si=s7108737024; H_PS_PSSID=1425_21089_29522_29518_29238_28519_29098_28833_29220_29459; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; PSINO=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1562846886,1563190502; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1563190502; yjs_js_security_passport=4da041312ce1aff06647360b42b59ef5b991c386_1563190504_js'
            ,'origin':'https://fanyi.baidu.com'
            ,'referer':'https://fanyi.baidu.com/'
            ,'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
            ,'x-requested-with':'XMLHttpRequest'
            }
    def translate(self,word):
        # token=self.sign_token.token
        token='b825b3a7cc74b7087a38946ab32c1ba1'
        sign=self.sign_token.sign(word)
        #构造请求数据
        data={
            'from': 'en',
            'to': 'zh',
            'query': word,
            'transtype': 'realtime',
            'simple_means_flag': 3,
            'sign': sign,
            'token': token
        }
        #response=requests.post(self.url,data=data,headers=self.headers)
        response=self.sign_token.session.post(self.url,data=data)
        return sign,token,response.content

tool=TranslateTool()
for word in ['are']:
    sign, token, re = tool.translate(word)
    re=json.loads(re.decode())
    print(sign)
    print(token)
    print(re)