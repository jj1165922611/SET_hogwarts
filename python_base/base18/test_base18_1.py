#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-07-09
# @Author     : Joey Jiang
# @File       : test_base18_1.py
# @Software   : PyCharm
# @Description: 雪球app抓包与mock实战

'''
map local，不访问服务器，直接返回内容给客户端
'''
from mitmproxy import http

def request(flow :http.HTTPFlow) -> None:
    if flow.request.pretty_url=="https://m.baidu.com/":
        flow.response=http.HTTPResponse.make(
            200,
            "hello world",
            {"Content-Type": "text/html"}
        )