#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-24
# @Author     : Joey Jiang
# @File       : base_page.py
# @Software   : PyCharm
# @Description: selenium多浏览器处理
'''
创建Base类，在setup()方法中实现多浏览器处理的代码
'''
from selenium import webdriver
import os
class Base:
    def setup(self):
        browser=os.getenv("browser").lower()
        if browser=="firefox":
            self.driver=webdriver.Firefox()
        elif browser=="headless":
            self.driver=webdriver.PhantomJS()
        else:
            self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
    def teardown(self):
        self.driver.quit()