#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-24
# @Author     : Joey Jiang
# @File       : test_base11_2_1.py
# @Software   : PyCharm
# @Description: 执行javaScript脚本
'''
execute_script()执行js脚本

在浏览器开发者模式->console中调试
'''
from time import sleep

from selenium import webdriver

class TestExecuteScript:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
    def teardown(self):
        self.driver.quit()
    def test_execute_script(self):
        self.driver.get("https://www.baidu.com")
        self.driver.execute_script("document.getElementById('kw').value='Selenium框架'")
        self.driver.execute_script("document.getElementById('su').click()")
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        sleep(2)
        self.driver.find_element_by_css_selector("#page > div > a.n").click()
        sleep(3)