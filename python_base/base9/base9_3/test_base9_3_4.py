#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-12
# @Author     : Joey Jiang
# @File       : test_base9_3_4.py
# @Software   : Visual Studio Code
# @Description: pytest测试框架
import pytest


class TestDemo:
    def setup_class(self):
        print("这是一个setup_class方法")
    def teardown_class(self):
        print("这是一个teardown_class方法")
    def setup_method(self):
        print("这是一个setup_method方法")
    def teardown_method(self):
        print("这是一个teardown_method方法")
    def setup(self):
        print("这是一个setup方法")
    def teardown(self):
        print("这是一个teardown方法")
    def test_one(self):
        print("这是一个方法one")
    def test_two(self):
        print("这是一个方法two")
def setup_function():
    print("这是一个setup_function函数")
def teardown_function():
    print("这是一个teardown_function函数")
def test_login():
    print("这是一个函数")
def setup_module():
    print("这是一个setup_module函数")
def teardown_module():
    print("这是一个teardown_module函数")
if __name__ == "__main__":
    pytest.main(['-v','-s','test_base9_3_4.py'])