#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-13
# @Author     : Joey Jiang
# @File       : test_base9_3_7.py
# @Software   : Visual Studio Code
# @Description: pytest测试框架
'''
1、scope="module"本身是模块调用一次，因为加了yield，所以模块前执行yield前的内容，模块后执行yield后的内容
2、注意这种方式没有返回值，如果希望返回使用addfinalizer
'''
import pytest

@pytest.fixture(scope="module")
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
    def test_one(self,open):
        print("test_one")
    def test_two(self,open):
        print("test_two")
    def test_three(self,open):
        print("test_three")

if __name__ == "__main__":
    pytest.main(['-v','-s','test_base9_3_7.py'])