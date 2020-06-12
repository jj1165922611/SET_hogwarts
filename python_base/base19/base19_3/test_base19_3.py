#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-06-08
# @Author     : Joey Jiang
# @File       : test_base19_3.py
# @Software   : PyCharm
# @Description: 接口测试断言
import requests


class TestRequests:
    def test_json(self):
        json={'H':'Header Demo'}
        r=requests.post("http://httpbin.testing-studio.com/post",json=json)
        print("*"*20)
        print(r.raw.read(10))
        print("*"*20)
        print(r.json())
        assert r.status_code==200
