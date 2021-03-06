#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-17
# @Author     : Joey Jiang
# @File       : test_9_6_2.py
# @Software   : Pycharm
# @Description: 测试报告美化与定制
'''
allure的特性
    @allure.feature():功能
    @allure.story():子功能
    with allure.step():测试步骤

'''
import pytest
import allure

@allure.feature("登录模块")
class TestLogin:
    @allure.story("登录成功")
    def test_login_success(self):
        print("这是登录测试用例，登录成功")
    @allure.story("登录失败")
    def test_login_fail(self):
        print("这是登录测试用例，登录失败")
    @allure.story("用户名缺失")
    def test_login_success_a(self):
        print("用户名缺失")
    @allure.story("密码缺失")
    def test_login_fail(self):
        with allure.step("点击用户名"):
            print("输入用户名")
        with allure.step("点击密码"):
            print("输入密码")
        print("点击登录")
        with allure.step("点击登录之后登录失败"):
            assert '1'==1
            print("登录失败")