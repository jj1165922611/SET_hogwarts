#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-06-07
# @Author     : Joey Jiang
# @File       : test_base13_6_1.py
# @Software   : PyCharm
# @Description: 设备交互API
'''
模拟GSM电话：make_gsm_call
模拟发短信：send_sms
    注意：只能在模拟器上使用

appium自动启动模拟器：des_caps['avd']="模拟器名称"
    查看模拟器名称：emulator -list-avds
'''
from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions


class TestPhoneCallMsg:
    def setup(self):
        des_caps={}
        des_caps['platformName']='Android'
        des_caps['platformVersion']='6.0'
        des_caps['deviceName']='emulator-5554'
        des_caps['appPackage']='com.xueqiu.android'
        des_caps['appActivity']='.common.MainActivity'
        des_caps['noReset']=True
        des_caps['unicodeKeyboard']=True
        # des_caps['resetKeyboard']=True
        des_caps['avd']='Nexus'
        des_caps['chromedriverExecutable']='C:/Program Files/Appium/resources/app/node_modules/appium/node_modules/appium-chromedriver/chromedriver/win/chromedriver2.20.exe'
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",des_caps)
        self.driver.implicitly_wait(10)
    def teardown(self):
        self.driver.quit()
    def test_phone_msg(self):
        self.driver.make_gsm_call('5551234567', GsmCallActions.CALL)
        self.driver.send_sms("5501234567","hello")

