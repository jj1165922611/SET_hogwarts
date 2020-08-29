#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-06-08
# @Author     : Joey Jiang
# @File       : test_base19_3.py
# @Software   : PyCharm
# @Description: 接口测试断言
'''
requests框架：响应结果断言
'''
import requests


class TestRequests:
    def test_headers(self):
        headers={'H':'Header Demo'}
        r=requests.get("http://httpbin.testing-studio.com/get",headers=headers)
        print("*"*20)
        print(r.raw.read(10))
        print("*"*20)
        print(r.text)
        print(r.json())
        assert r.json()['headers']['H']=='Header Demo'
