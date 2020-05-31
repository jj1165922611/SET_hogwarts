#!/usr/bin/env python
# -*- coding: utf-8
# @Time       : 2020-05-28
# @Author     : Joey Jiang
# @File       : test_base_12_1.py
# @Software   : PyCharm
# @Description: appium环境安装与架构介绍
from appium import webdriver
class TestAppium:
    def test_appium(self):
        desired_caps={}
        desired_caps['platformName']='Android'
        desired_caps['platformVersion']='6.0'
        desired_caps['deviceName']='127.0.0.1:7555'
        desired_caps['appPackage']='com.android.settings'
        desired_caps['appActivity']='com.android.settings.Settings'
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        self.driver.quit()