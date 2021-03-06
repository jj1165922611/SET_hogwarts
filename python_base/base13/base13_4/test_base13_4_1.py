#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-06-01
# @Author     : Joey Jiang
# @File       : test_base13_4_1.py
# @Software   : PyCharm
# @Description: android webview测试
'''
纯web页面测试

代码注意：
    desired_caps
        browserName='Browser'或者browserName='Chrome'
        chromedriverExecutable='指定driver地址'
'''
from appium import webdriver

class TestWebView:
    def setup(self):
        des_caps={}
        des_caps['platformName']='Android'
        des_caps['platformVersion']='6.0'
        des_caps['deviceName']='127.0.0.1:7555'
        des_caps['noReset']=True
        des_caps['browserName']='Browser'
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",des_caps)
        self.driver.implicitly_wait(10)
    def teardown(self):
        self.driver.quit()
    def test_webview(self):
        self.driver.get("http://m.baidu.com")