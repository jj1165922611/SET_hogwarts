#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-06-08
# @Author     : Joey Jiang
# @File       : test_base19_5_1.py
# @Software   : PyCharm
# @Description: json/xml断言
'''
不使用jsonpath进行断言
'''
import requests

class TestRequests:
    def test_json(self):
        r=requests.get("https://ceshiren.com/categories.json")
        print("*"*20)
        print(r.raw.read(10))
        print("*"*20)
        assert r.json()['category_list']['categories'][0]['name'] == "霍格沃兹测试学院公众号"
