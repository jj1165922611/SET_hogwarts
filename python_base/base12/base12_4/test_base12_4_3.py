#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-30
# @Author     : Joey Jiang
# @File       : test_base12_4_3.py
# @Software   : PyCharm
# @Description: app控件定位
'''
导入依赖
capability设置
初始化driver
执行代码
'''
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestLocator:
    def setup(self):
        desired_caps={}
        desired_caps['platformName']='Android'
        desired_caps['platformVersion']='6.0'
        desired_caps['deviceName']='127.0.0.1:7555'
        desired_caps['appPackage']='com.xueqiu.android'
        desired_caps['appActivity']='.view.WelcomeActivityAlias'
        desired_caps['noReset']=True
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        self.driver.implicitly_wait(20)
    def teardown(self):
        self.driver.quit()
    def test_locator(self):
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/home_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").click()
        self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/name" and @text="阿里巴巴"]').click()
        price=self.driver.find_element_by_id('com.xueqiu.android:id/current_price').text
        assert float(price)>200
