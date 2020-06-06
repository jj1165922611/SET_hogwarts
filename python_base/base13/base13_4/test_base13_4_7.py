#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-06-01
# @Author     : Joey Jiang
# @File       : test_base13_4_6.py
# @Software   : PyCharm
# @Description: android webview测试
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestWebView:
    def setup(self):
        des_caps={}
        des_caps['platformName']='Android'
        des_caps['platformVersion']='6.0'
        des_caps['deviceName']='emulator-5554'
        des_caps['appPackage']='io.appium.android.apis'
        des_caps['appActivity']='.ApiDemos'
        des_caps['noReset']=True
        des_caps['chromedriverExecutableDir']='C:/Program Files/Appium/resources/app/node_modules/appium/node_modules/appium-chromedriver/chromedriver/win'
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",des_caps)
        self.driver.implicitly_wait(10)
    def teardown(self):
        self.driver.quit()
    def test_webview(self):
        print(self.driver.contexts)
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Views").instance(0));').click()
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("WebView").instance(0));').click()
        print(self.driver.contexts)
        context=self.driver.contexts[-1]
        print(context)
        self.driver.switch_to.context(context)
        self.driver.find_element_by_id("i_am_a_textbox").send_keys("i_am_a_textboxhhhhhhhh")
        print(self.driver.contexts)
