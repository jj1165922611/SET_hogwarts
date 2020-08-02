#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-13
# @Author     : Joey Jiang
# @File       : test_base9_3_9.py
# @Software   : Visual Studio Code
# @Description: pytest测试框架
'''
因为@pytest.fixture()默认scope是function。autouse是每个用例都调用open()函数，
所以会在每个用例执行前打印"打开浏览器"，每个用例执行后打印"执行teardown方法"和"关闭浏览器"
'''
import pytest

@pytest.fixture(autouse=False)
def open():
    print("打开浏览器")
    yield
    print("执行teardown方法")
    print("关闭浏览器")
class TestDemo:
    def setup(self):
        print("setup")
    def teardown(self):
        print("teardown")
    def test_one(self):
        print("test_one")
    def test_two(self):
        print("test_two")
    def test_three(self):
        print("test_three")

if __name__ == "__main__":
    pytest.main(['-v','-s','base9_3/test_base9_3_9.py'])