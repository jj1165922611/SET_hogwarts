#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020/11/16 22:39
# @Author     : Joey Jiang
# @File       : test_method_attribute_demo.py
# @Software   : PyCharm
# @Description: 元素属性和方法
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestMethodAttribute:
    def setup(self):
        desired_caps={}
        desired_caps["platformName"]="Android"
        desired_caps["platformVersion"]="6.0"
        desired_caps["deviceName"]="emulator-5554"
        desired_caps["appPackage"]="com.xueqiu.android"
        desired_caps["appActivity"]=".view.WelcomeActivityAlias"
        desired_caps["noReset"]=True
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()
    def test_method_attribute(self):
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located((By.ID,"com.xueqiu.android:id/home_search")))
        ele=self.driver.find_element_by_id("com.xueqiu.android:id/home_search")
        while True:
            if ele.is_enabled():
                print(ele.get_attribute("text"))
                print(ele.size)
                print(ele.location)
                ele.click()
                break
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
        ele1=self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
        if ele1.is_displayed():
            print("搜索成功")
        else:
            print("搜索失败")