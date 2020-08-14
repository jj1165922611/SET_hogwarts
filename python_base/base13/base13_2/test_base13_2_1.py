#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
# @Time       : 2020-06-01
# @Author     : Joey Jiang
# @File       : test_base13_2_1.py
# @Software   : PyCharm
# @Description: 属性获取与断言
'''
获取属性的方法是get_attribute()
'''
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestGetAttribute:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        desired_caps['noReset'] = True
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(20)
    def teardown(self):
        self.driver.quit()
    def test_get_attribute(self):
        search_ele=self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/home_search")
        print(search_ele.get_attribute("content-desc"))
        print(search_ele.get_attribute("resource-id"))
        print(search_ele.get_attribute("enabled"))
        print(search_ele.get_attribute("clickable"))
        print(search_ele.get_attribute("bounds"))
