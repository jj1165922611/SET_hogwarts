#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-06-01
# @Author     : Joey Jiang
# @File       : test_base13_4_9.py
# @Software   : PyCharm
# @Description: android webview测试
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWebViewCase2:
    def setup(self):
        des_caps={}
        des_caps['platformName']='Android'
        des_caps['platformVersion']='6.0'
        des_caps['deviceName']='emulator-5554'
        des_caps['appPackage']='com.xueqiu.android'
        des_caps['appActivity']='.common.MainActivity'
        des_caps['noReset']=True
        des_caps['avd']='Nexus'
        des_caps['chromedriverExecutable']='C:/Program Files/Appium/resources/app/node_modules/appium/node_modules/appium-chromedriver/chromedriver/win/chromedriver2.20.exe'
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",des_caps)
        self.driver.implicitly_wait(10)
    def teardown(self):
        self.driver.quit()
    def test_webview(self):
        print(self.driver.contexts)
        self.driver.find_element(MobileBy.XPATH,"//*[@text='交易']").click()
        # self.driver.find_element(MobileBy.XPATH,"//*[@text='沪深']").click()
        print(self.driver.contexts)
        self.driver.switch_to.context(self.driver.contexts[-1])
        ele=(By.XPATH,'//*[@id="Layout_app_3V4"]/div/div/ul/li[1]/div[2]/h1')
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(ele))
        self.driver.find_elements(*ele).click()
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.driver.find_element_by_id("phone-number").send_keys("17625416583")
        self.driver.find_element_by_id("code").send_keys("123456")
        self.driver.find_element_by_link_text("立即开户").click()
        print(self.driver.contexts)
        # 有问题