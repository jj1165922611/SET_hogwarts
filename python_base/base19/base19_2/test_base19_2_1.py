#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-06-08
# @Author     : Joey Jiang
# @File       : test_base19_2_1.py
# @Software   : PyCharm
# @Description: 接口请求构造

'''
requests框架：发送get请求。使用params参数
'''
import requests

class TestRequests:
    def test_query(self):
        payload={
            "level":1,
            "name":"hogwarts"
        }
        r=requests.get('http://httpbin.testing-studio.com/get',params=payload)
        print(r)
        print(r.status_code)
        print(r.encoding)
        print(r.text)
        print(r.json())
        assert r.status_code==200