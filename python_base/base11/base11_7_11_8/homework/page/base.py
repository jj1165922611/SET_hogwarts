#!/usr/bin/env python
# -*- coding: -*-
# @Time       : 2020-05-27
# @Author     : Joey Jiang
# @File       : base_page.py
# @Software   : PyCharm
# @Description: 企业微信web端自动化测试实战（一）
from selenium import webdriver
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self,driver=None):
        if driver==None:
            self.driver =webdriver.Chrome()
        else:
            self.driver=driver
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def find(self,by,locator):
        return self.driver.find_element(by,locator)
    def quit(self):
        self.driver.quit()