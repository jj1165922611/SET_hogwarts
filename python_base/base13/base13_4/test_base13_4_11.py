#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-06-01
# @Author     : Joey Jiang
# @File       : test_base13_4_9.py
# @Software   : PyCharm
# @Description: android webview测试
'''
webview测试

设备注意
    android模拟器6.0默认支持webview操作（mumu不可以，genimotion和SDK自带的emulator可以）
    其他模拟器或物理机需要打开app内开关（webview调试开关）

chromedriverExecutable指定具体哪一个driver

切换上下文进入webview页面

切换windows
'''
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
        des_caps['unicodeKeyboard']=True
        # des_caps['resetKeyboard']=True
        des_caps['avd']='Nexus'
        des_caps['chromedriverExecutable']='C:/Program Files/Appium/resources/app/node_modules/appium/node_modules/appium-chromedriver/chromedriver/win/chromedriver2.20.exe'
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",des_caps)
        self.driver.implicitly_wait(10)
    def teardown(self):
        self.driver.quit()
    def test_webview(self):
        print(self.driver.contexts)
        # 点击交易
        self.driver.find_element(MobileBy.XPATH,"//*[@text='交易']").click()
        # self.driver.find_element(MobileBy.XPATH,"//*[@text='沪深']").click()
        print(self.driver.contexts)
        # 切换上下文
        self.driver.switch_to.context(self.driver.contexts[-1])
        # 点击A股开户
        ele=(By.XPATH,'//*[@id="Layout_app_3V4"]/div/div/ul/li[1]/div[2]/h1')
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(ele))
        self.driver.find_element(*ele).click()
        # 注意此时app中新打开了一个窗口，所以如果不切换还停留在原来的窗口上，会定位不到元素。
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # 显示等待，直到新窗口中的元素可点击
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.ID,"phone-number")))
        # 输入用户名
        self.driver.find_element_by_id("phone-number").send_keys("17625416583")
        # 输入密码
        self.driver.find_element_by_id("code").send_keys("123456")
        # 点击立即开户
        self.driver.find_element(MobileBy.CSS_SELECTOR,"body > div > div > div.form-wrap > div > div.btn-submit").click()
        print(self.driver.contexts)
