#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-31
# @Author     : Joey Jiang
# @File       : test_base13_1_3.py
# @Software   : PyCharm
# @Description: 特殊控件toast识别
'''
toast定位

使用xpath查找
		class定位
		contains包含文本
'''
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestToast:
    def setup(self):
        desired_caps={}
        desired_caps['platformName']='Android'
        desired_caps['platformVersion']='6.0'
        desired_caps['deviceName']='127.0.0.1:7555'
        desired_caps['appPackage']='com.touchboarder.android.api.demos'
        desired_caps['appActivity']='com.touchboarder.androidapidemos.MainActivity'
        desired_caps['noReset']=True
        desired_caps['automationName']='uiautomator2'
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()

    def test_toast(self):
        self.driver.find_element(MobileBy.XPATH,'//*[@text="API Demos"]').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="Views"]').click()
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).'
            'scrollIntoView(new UiSelector().text("Popup Menu").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="Make a Popup!"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="Search"]').click()
        # print(self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text)
        print(self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"Clicked popup")]').text)