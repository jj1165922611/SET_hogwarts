#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-17
# @Author     : Joey Jiang
# @File       : test_9_6_5.py
# @Software   : Pycharm
# @Description: 测试报告美化与定制

'''
@allure.testcase(地址,'登录用例')，显示'登录用例'，点进去是地址
'''
import pytest
import allure

TEST_CASE_LINK="http://www.baidu.com"
@allure.testcase(TEST_CASE_LINK,'登录用例')
def test_with_link3():
    print("test_with_link3")
