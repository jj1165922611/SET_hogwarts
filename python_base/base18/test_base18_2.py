#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-07-09
# @Author     : Joey Jiang
# @File       : test_base18_2.py
# @Software   : PyCharm
# @Description: 雪球app抓包与mock实战

'''
map local，不访问服务器，将响应数据保存为文件，修改后返回给客户端
'''
from mitmproxy import http

def request(flow :http.HTTPFlow) -> None:
    if "quote.json" in flow.request.pretty_url:
        with open("quote.json","rb") as f:
            flow.response=http.HTTPResponse.make(
               200,
                f.read(),
                {"Content-Type": "text/html"}
        )