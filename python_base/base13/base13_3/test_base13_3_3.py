#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-06-01
# @Author     : Joey Jiang
# @File       : test_base13_3_3.py
# @SOftware   : PyCharm
# @Description: 参数化用例
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestXueQiu:
    def setup(self):
        desired_caps={}
        desired_caps['platformName']='Android'
        desired_caps['platformVersion']='6.0'
        desired_caps['deviceName']='127.0.0.1:7555'
        desired_caps['appPackage']='com.xueqiu.android'
        desired_caps['appActivity']='.view.WelcomeActivityAlias'
        desired_caps['noReset']='true'
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        self.driver.implicitly_wait(30)
    def teardown(self):
        self.driver.quit()
    @pytest.mark.parametrize("company",[("阿里巴巴",),("小米",)])
    def test_search(self,company):
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/home_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(company)
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").click()
        ele=f'//*[@resource-id="com.xueqiu.android:id/name" and @text={company}]'
        self.driver.find_element_by_xpath(ele).click()
        price = self.driver.find_element_by_id('com.xueqiu.android:id/current_price').text
        print(price)
        # 有问题