#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-06-09
# @Author     : Joey Jiang
# @File       : test_base19_7_1.py
# @Software   : PyCharm
# @Description: header cookie处理
import requests
class TestCookie:
    def test_cookie(self):
        url="http://httpbin.testing-studio.com/get"
        header={
            'User-Agent': 'python-requests/2.23.0',
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'Cookie': 'hogwarts=true'
        }
        r=requests.get(url,headers=header)
        print(r.request.headers)