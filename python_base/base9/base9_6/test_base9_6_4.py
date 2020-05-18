#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-17
# @Author     : Joey Jiang
# @File       : test_9_6_4.py
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
