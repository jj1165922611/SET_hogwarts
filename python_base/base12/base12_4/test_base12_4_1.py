#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-30
# @Author     : Joey Jiang
# @File       : test_base12_4_1.py
# @Software   : PyCharm
# @Description: app控件定位
'''
基本配置错误和手写错误
'''
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestLocator:
    def setup(self):
        desired_caps={}
        desired_caps['platformName']='Android'
        desired_caps['platfromVersion']='6.0'
        desired_caps['deviceName']='127.0.0.1:7555'
        desired_caps['appPackage']='com.xueqiu.android'
        desired_caps['appAcivity']=''
        desired_caps['noReset']=True
        self.driver=webdriver.Remote("gttp://127.0.0.1:4723/wd/hub",desired_caps)
    def teardown(self):
        self.driver.quit()
    def test_locator(self):
        self.driver.find_element(MobileBy.ID,"")

        # 好几个问题