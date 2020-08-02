#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-13
# @Author     : Joey Jiang
# @File       : test_base9_3_10.py
# @Software   : Visual Studio Code
# @Description: pytest测试框架
'''
传递参数：params，传入的数据需要使用一个固定的参数名request来接收
'''
import pytest

@pytest.fixture(params=["a","b","c"])
def open_test(request):
    return request.param

class TestDemo:
    def setup(self):
        print("setup")
    def teardown(self):
        print("teardown")
    def test_one(self,open_test):
        print(f"test_one{open_test}")
    def test_two(self):
        print("test_two")
    def test_three(self):
        print("test_three")

if __name__ == "__main__":
    pytest.main(['-v','-s','test_base9_3_10.py'])