#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-28
# @Author     : Joey Jiang
# @File       : test_base12_3.py
# @Software   : PyCharm
# @Description: 元素定位与隐式等待
'''
导入依赖
capability设置
初始化driver
执行代码
'''
from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By


class TestXueQiu:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['noReset'] = 'true'
        desired_caps['dontStopAppOnReset'] = 'true'
        desired_caps['skipDeviceInitialization']=True
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        self.driver.implicitly_wait(20)
    def teardown(self):
        self.driver.quit()
    def test_xue_qiu(self):
        self.driver.find_element(By.ID,"com.xueqiu.android:id/home_search").click()
        self.driver.find_element(By.ID,"com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(By.ID,"com.xueqiu.android:id/search_input_text").click()
        self.driver.back()
        self.driver.back()
        sleep(5)
