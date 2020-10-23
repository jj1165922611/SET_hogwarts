#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-10-17
# @Author     : Joey Jiang
# @File       : test_get_token.py
# @Software   : PyCharm
# @Description: apiobject模式应用
from python_hogwarts12.api_026.api_object.api.get_token import GetToken


class TestGetToken:
    def setup(self):
        self.get_token=GetToken()
    def test_get_token(self, data: dict):
        data = {
            "url": "1111",
            "method": "get",
            "params": {
                "copir":"1111",
                "cpor2":"2222"
            }
        }
        assert self.get_token.get_token().status_code=="200"



