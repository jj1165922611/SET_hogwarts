#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-11-06
# @Author     : Joey Jiang
# @File       : test_fixture_login.py
# @Software   : PyCharm
# @Description: 测试用例执行时，有的用例需要登录才能执行，有些用例不需要登录。
import pytest
@pytest.fixture(scope="function")
def login():
    print("账号登录。。。")
    yield
    print("账号退出。。。")

class TestFixtureLogin:

    def test_case1(self,login):
        print("test_case1")

    def test_case2(self,login):
        print("test_case2")

    def test_case3(self):
        print("test_case3")

    def test_case4(self, login):
        print("test_case4")