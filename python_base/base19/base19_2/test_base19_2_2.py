#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-06-08
# @Author     : Joey Jiang
# @File       : test_base19_2_2.py
# @Software   : PyCharm
# @Description: 接口请求构造

import requests

class TestRequests:
    def test_post(self):
        payload={
            "level":1,
            "name":"hogwarts"
        }
        r=requests.post('http://httpbin.testing-studio.com/post',data=payload)
        print(r)
        print(r.status_code)
        print(r.encoding)
        print(r.text)
        print(r.json())
        assert r.status_code==200