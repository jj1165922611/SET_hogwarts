#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-21
# @Author     : Joey Jiang
# @File       : test_base9_9_2.py
# @Software   : PyCharm
# @Description: pytest测试实战（三）

'''

'''
import pytest
@pytest.fixture()
def login():
    print("登录操作")

class TestCart:
    def test_cart1(self,login):
        print("test_cart1需要登录")
    def test_cart2(self,login):
        print("test_cart2需要登录")
    def test_cart3(self):
        print("test_cart3不需要登录")