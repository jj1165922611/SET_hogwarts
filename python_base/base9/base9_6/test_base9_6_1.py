#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-16
# @Author     : Joey Jiang
# @File       : test_9_6_1.py
# @Software   : Pycharm
# @Description: 测试报告美化与定制

'''
allure官网提供的pytest结合allure示例
'''
import pytest

def test_success():
    """this test succeeds"""
    assert True


def test_failure():
    """this test fails"""
    assert False


def test_skip():
    """this test is skipped"""
    pytest.skip('for a reason!')


def test_broken():
    raise Exception('oops')