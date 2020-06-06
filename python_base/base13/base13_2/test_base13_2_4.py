#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
# @Time       : 2020-06-01
# @Author     : Joey Jiang
# @File       : test_base13_2_3.py
# @Software   : PyCharm
# @Description: 属性获取与断言
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *

class TestHamcrest:
    def test_hamcrest(self):
        assert_that(16,close_to(2,14),"这是一个提示")
        assert_that(16,close_to(2,13),"这是一个提示")
        assert_that(16,close_to(2,15),"这是一个提示")
        assert_that("contains String",contains_string("cont"))