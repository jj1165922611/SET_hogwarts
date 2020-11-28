#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020/11/18 0018 21:15
# @Author     : Joey Jiang
# @File       : test_web_app.py
# @Software   : PyCharm
# @Description: 纯web页面测试
from appium import webdriver


class TestWebApp:
    def setup(self):
        desired_caps={}
        desired_caps["platformName"]="Android"
        desired_caps["platformVersion"]="6.0"
        desired_caps["deviceName"]="127.0.0.1:7555"
        desired_caps["browserName"]="Browser"
        # appium中可以查看到chromedriver的默认地址
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        self.driver.implicitly_wait(3)
    def teardown(self):
        self.driver.quit()
    def test_baidu(self):
        self.driver.get("https://m.baidu.com")
        self.driver.find_element_by_id("index-kw").send_keys("250")
        self.driver.find_element_by_id("index-bn").click()