#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-06-08
# @Author     : Joey Jiang
# @File       : test_base19_4.py
# @Software   : PyCharm
# @Description: json/xml请求
'''
requests框架：json请求
    可以用关键字data参数发送，也可以用关键字json参数发送
'''
import requests


class TestRequests:
    def test_json(self):
        json={'H':'Header Demo'}
        r=requests.post("http://httpbin.testing-studio.com/post",json=json)
        print(r.json())
        assert r.status_code==200
