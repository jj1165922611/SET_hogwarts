#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-16
# @Author     : Joey Jiang
# @File       : test_base9_3_17.py
# @Software   : Visual Studio Code
# @Description: pytest测试框架
'''
生成测试用例报告
'''
import pytest

@pytest.mark.search
def test_search1():
    print("test_search1")
    raise NameError
@pytest.mark.search
def test_search2():
    print("test_search2")
@pytest.mark.login
def test_login1():
    print("test_login1")
@pytest.mark.login
def test_login2():
    print("test_login2")
if __name__ == "__main__":
    pytest.main(['-v','-s','test_base9_3_17.py'])
# 需要命令行执行 pytest -v -s --html=report.html --self-contained-html python_base/base9/base9_3/test_base9_3_17.py