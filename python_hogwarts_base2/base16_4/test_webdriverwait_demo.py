#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-11-08
# @Author     : Joey Jiang
# @File       : test_webdriverwait_demo.py
# @Software   : PyCharm
# @Description: WebDriverWait使用

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

"""
until里面的条件可以是selenium提供的expected_conditions，
也可以是自定义的一个函数，这个函数必须带有参数
"""
class TestWebDriverWaitDemo:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
    def test_baidu1(self):
        self.driver.get("https://www.baidu.com")
        ele=(By.ID,"kw")
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(ele))
        self.driver.find_element(By.ID,"kw").send_keys("我是谁")
    def test_baidu2(self):
        self.driver.get("https://www.baidu.com")
        def wait(x):
            return len(self.driver.find_elements(By.ID,"kw"))>=1
        WebDriverWait(self.driver,10).until(wait)
        self.driver.find_element(By.ID,"kw").send_keys("我是谁")
    def teardown(self):
        self.driver.quit()