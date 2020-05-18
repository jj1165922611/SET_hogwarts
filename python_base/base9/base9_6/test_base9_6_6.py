#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-17
# @Author     : Joey Jiang
# @File       : test_9_6_6.py
# @Software   : Pycharm
# @Description: 测试报告美化与定制

import pytest
import allure

@allure.link("http://www.baidu.com")
def test_with_link():
    print("这是一条加了链接的测试用例")

@allure.link("http://www.baidu.com",name="链接")
def test_with_link2():
    print("这是一条加了链接的测试用例")

TEST_CASE_LINK="http://www.baidu.com"
@allure.testcase(TEST_CASE_LINK,'登录用例')
def test_with_link3():
    print("test_with_link3")

@allure.issue("140","这是一个issue")
def test_with_issue_link():
    pass