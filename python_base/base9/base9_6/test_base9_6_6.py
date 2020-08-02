#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-17
# @Author     : Joey Jiang
# @File       : test_9_6_6.py
# @Software   : Pycharm
# @Description: 测试报告美化与定制

'''
@allure.issue("bugid","bug标题")
执行的时候需要加个参数:--allure-link-pattern=issue:http://www.baidu.com
'''
import pytest
import allure

@allure.issue("140","这是一个issue")
def test_with_issue_link():
    pass