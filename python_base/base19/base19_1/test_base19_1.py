#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-06-08
# @Author     : Joey Jiang
# @File       : test_base19_1.py
# @Software   : PyCharm
# @Description: 接口测试框架

import requests

class TestRequests:
    def test_get(self):
        r=requests.get('http://httpbin.testing-studio.com/get')
        print(r)
        print(r.status_code)
        print(r.encoding)
        print(r.text)
        print(r.json())
        assert r.status_code==200