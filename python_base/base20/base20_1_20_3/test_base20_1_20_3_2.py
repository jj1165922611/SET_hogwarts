#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-06-11
# @Auhtor     : Joey Jiang
# @File       : test_base20_1_20_3_2.py
# @Software   : PyCharm
# @Description: 企业微信接口测试实战

import requests

class TestToken:

    def test_token(self):
        params={
            'corpid':'wwaa5e12b39afbafe3',
            'corpsecret':'2_YAsegpEFFziREvf3GB5Vr2bIgAP7cBIWr35DN_b-s'
        }
        url='https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        r=requests.get(url,params=params)
        print(r.json())
        print("*"*20)
    def test_create_department(self):
        pass
    def test_update_department(self):
        pass
    def test_delete_department(self):
        pass
    def test_getlist_department(self):
        pass