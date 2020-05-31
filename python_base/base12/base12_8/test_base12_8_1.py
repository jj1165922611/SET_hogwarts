#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-31
# @Author     : Joey Jiang
# @File       : test_base12_8_1.py
# @Software   : PyCharm
# @Description: 显式等待机制
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestUiautomator:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        desired_caps['noReset'] = True
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(20)

    def teardown(self):
        self.driver.quit()

    def test_uiautomator_scroll(self):
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/home_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
        self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/name" and @text="阿里巴巴"]').click()
        locator=(MobileBy.XPATH,'//*[@text="09988"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]')
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(locator))
        ele = self.driver.find_element_by_xpath(
            '//*[@text="09988"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]')
        assert float(ele.text) > 200