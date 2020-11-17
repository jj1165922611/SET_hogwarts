#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020/11/17 21:04
# @Author     : Joey Jiang
# @File       : test_xpath_demo.py
# @Software   : PyCharm
# @Description: xpath定位
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestXpath:
    def setup(self):
        desired_cpas={}
        desired_cpas["platformName"]="Android"
        desired_cpas["platformVersion"]="6.0"
        desired_cpas["appPackage"]="com.xueqiu.android"
        desired_cpas["appActivity"]=".view.WelcomeActivityAlias"
        desired_cpas["deviceName"]="emulator-5554"
        desired_cpas["noReset"]="true"
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_cpas)
        self.driver.implicitly_wait(3)
    def teardown(self):
        self.driver.quit()
    def test_xpath(self):
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.ID,"com.xueqiu.android:id/home_search")))
        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()

        price=self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/stockCode' and @text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        print(price)
        assert float(price)>200

