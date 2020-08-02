#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-17
# @Author     : Joey Jiang
# @File       : test_9_6_7.py
# @Software   : Pycharm
# @Description: 测试报告美化与定制

'''
1、重要性级别
Block:阻塞
Critical:严重的
Nromal:正常问题
Minor:不太重要
Trivial:不重要
2、执行时pytest -s -v 文件名 --allure-severities 分类1,分类2
'''
import pytest
import allure


def test_with_no_severity_label():
    pass

@allure.severity(allure.severity_level.TRIVIAL)
def test_with_trivial_severity():
    pass
@allure.severity(allure.severity_level.NORMAL)
def test_with_normal_severity():
    pass
@allure.severity(allure.severity_level.NORMAL)
class TestWithNormalSeverity:
    def test_method_normal_severity(self):
        pass
    @allure.severity(allure.severity_level.CRITICAL)
    def test_method_critical_severity(self):
        pass

if __name__ == '__main__':
    pytest.main(["-v","-s","test_base9_6_7.py"])