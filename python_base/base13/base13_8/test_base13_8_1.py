#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-06-07
# @Author     : Joey Jiang
# @File       : test_base13_8_1.py
# @Software   : PyCharm
# @Description: capalibility使用进阶
'''
策略相关
    noReset
    fullReset
    dontStopAppOnReset
性能相关
    skipServerInstallation
	skipDeviceInitialization
	skipUnlock
	skipLogCapture
	systemPort
	ignoreUnimportantViews
	relaxed-security
'''
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestCapability:
    def setup(self):
        desired_caps={}
        desired_caps['platformName']='Android'
        desired_caps['platformVersion']='6.0'
        desired_caps['deviceName']='emulator-5554'
        desired_caps['udid']='emulator-5554'
        desired_caps['appPackage']='com.xueqiu.android'
        desired_caps['appActivity']='.common.MainActivity'
        desired_caps['noReset']='true'
        desired_caps['newCommandTimeout']=300
        desired_caps['dontStopAppOnReset']=True
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        self.driver.implicitly_wait(10)
    def teardown(self):
        self.driver.quit()

    def test_capablility(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@text='推荐']").click()
