#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-07-09
# @Author     : Joey Jiang
# @File       : test_base18_2.py
# @Software   : PyCharm
# @Description: 雪球app抓包与mock实战

from mitmproxy import http

def request(flow :http.HTTPFlow) -> None:
    if "quote.json" in flow.request.pretty_url:
        flow.response=http.HTTPResponse.make(
            200,
            "hello world",
            {"Content-Type": "text/html"}
        )