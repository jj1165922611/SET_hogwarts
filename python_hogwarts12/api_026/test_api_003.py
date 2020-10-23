#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-10-15
# @Author     : Joey Jiang
# @File       : test_api_003.py
# @Software   : PyCharm
# @Description: 基于加密接口的测试用例设计
import requests
import base64

class TestApi:
    data={
        "method":"get",
        "url":"http://testing-studio:9999/demo1.txt",
        "headers":None
    }
    env = {
        "default": "dev",
        "testing-studio": {
            "test": "127.0.0.1",
            "dev": "192.168.0.1"
        }
    }
    def test_send(self):
        data=self.data
        env=self.env
        url=str(data["url"])
        url=url.replace("testing-studio",env["testing-studio"][env["default"]])
        print(url)

        # requests.request(method=data["method"],url=data["url"],headers=data["headers"])
