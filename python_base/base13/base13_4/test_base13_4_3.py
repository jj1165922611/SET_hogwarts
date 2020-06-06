#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-06-01
# @Author     : Joey Jiang
# @File       : test_base13_4_3.py
# @Software   : PyCharm
# @Description: android webview测试
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction


class TestWebView:
    def setup(self):
        des_caps={}
        des_caps['platformName']='Android'
        des_caps['platformVersion']='6.0'
        des_caps['deviceName']='emulator-5554'
        des_caps['appPackage']='com.touchboarder.android.api.demos'
        des_caps['appActivity']='com.touchboarder.androidapidemos.MainActivity'
        des_caps['noReset']=True
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",des_caps)
        self.driver.implicitly_wait(10)
    def teardown(self):
        self.driver.quit()
    def test_webview(self):
        self.driver.find_element(MobileBy.LINK_TEXT,"API Demos").click()
        action=TouchAction(self.driver)
        width,height=[int(i) for i in self.driver.get_window_size()]
        action.press(x=width*0.5,y=height*0.5).wait(1).move_to(x=width*0.5,y=0).release().perform()
        self.driver.find_element_by_id("android:id/text1").click()
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("WebView").instance(0));').click()

        # 有问题