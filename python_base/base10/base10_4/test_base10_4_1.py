#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-23
# @Author     : Joey Jiang
# @File       : test_base10_4_1.py
# @Software   : PyCharm
# @Description: 隐式等待与显式等待
'''
直接等待：强制等待，线程休眠一段时间

time.sleep(3)
'''
import time

from selenium import webdriver
import time,pytest
class TestWait:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
    def test_wait(self):
        self.driver.get("https://home.testing-studio.com/")
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@title="归入各种类别的所有主题"]').click()
        print("Hello")
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()
    def teardown(self):
        self.driver.quit()