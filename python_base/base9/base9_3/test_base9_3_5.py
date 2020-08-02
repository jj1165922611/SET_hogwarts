#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-12
# @Author     : Joey Jiang
# @File       : test_base9_3_5.py
# @Software   : Visual Studio Code
# @Description: pytest测试框架
'''
@pytest.fixture()装饰器
'''
import pytest
@pytest.fixture()
def login():
    print("这是一个登录方法")
class TestDemo:
    def test_one(self,login):
        print("这是一个方法one，需要登录")
    def test_two(self):
        print("这是一个方法two，不需要登录")

if __name__ == "__main__":
    pytest.main(['-v','-s','test_base9_3_5.py'])