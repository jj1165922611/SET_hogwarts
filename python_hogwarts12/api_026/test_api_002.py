#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-10-15
# @Author     : Joey Jiang
# @File       : test_api_002.py
# @Software   : PyCharm
# @Description: 基于加密接口的测试用例设计
import requests
import base64

def test_encode():
    res=requests.get("http://127.0.0.1:9999/demo.txt")
    print(res.text)
    print(base64.b64decode(res.content))