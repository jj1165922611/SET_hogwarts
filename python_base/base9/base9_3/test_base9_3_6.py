#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-12
# @Author     : Joey Jiang
# @File       : test_base9_3_6.py
# @Software   : Visual Studio Code
# @Description: pytest测试框架
'''
建一个公共模块conftest，编写@pytest.fixture()装饰器方法 connect，其他测试工程师也能使用
'''
import pytest

class TestDemo:
    def test_one(self,connect):
        print("这是一个方法one，需要连接数据库")
    def test_two(self):
        print("这是一个方法two，不需要连接数据库")

if __name__ == "__main__":
    pytest.main(['-v','-s','test_base9_3_6.py'])