#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-06-09
# @Author     : Joey Jiang
# @File       : test_19_8_1.py
# @Software   : PyCharm
# @Description: 认证体系
'''
http basic，基本认证
'''
import requests


class TestAuth:
    def test_auth(self):
        r=requests.get("http://httpbin.testing-studio.com/basci-auth/banana/123",auth=("banana","123"))
        print(r)
        # 有问题