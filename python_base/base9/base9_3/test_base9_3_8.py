#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-13
# @Author     : Joey Jiang
# @File       : test_base9_3_8.py
# @Software   : Visual Studio Code
# @Description: pytest测试框架
import pytest

@pytest.fixture(autouse=True)
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
    pytest.main(['-v','-s','python_base/base9/base9_3/test_base9_3_8.py'])