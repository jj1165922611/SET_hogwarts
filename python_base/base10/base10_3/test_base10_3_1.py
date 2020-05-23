#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-23
# @Author     : Joey Jiang
# @File       : test_base10_3_1.py
# @Software   : PyCharm
# @Description: selenium用例编写
import time

from selenium import webdriver

class TestTesterHome:
    def setup(self):
        self.driver=webdriver.Chrome()
    def teardown(self):
        self.driver.quit()
    def test_case(self):
        self.driver.get("https://testerhome.com/")
        self.driver.find_element_by_link_text("社团").click()
        time.sleep(1)
        self.driver.find_element_by_link_text("霍格沃兹测试学院").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@id='main']/div/div/div/div/div/div[2]/div/a").click()
        time.sleep(1)