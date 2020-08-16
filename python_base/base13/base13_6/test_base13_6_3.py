#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-06-07
# @Author     : Joey Jiang
# @File       : test_base13_6_3.py
# @Software   : PyCharm
# @Description: 设备交互API
'''
截图
'''
from time import sleep

from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions


class TestScreenShot:
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
    def test_screen_shot(self):
        self.driver.set_network_connection(0)
        self.driver.get_screenshot_as_file("G:/python/SET_hogwarts/python_base/base13/base13_6/test_base13_6_3.png")
        sleep(3)
        self.driver.set_network_connection(4)
