#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020/11/8 20:05
# @Author     : Joey Jiang
# @File       : base_page.py
# @Software   : PyCharm
# @Description: base_page是所有页面的父类
import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class BasePage:
    def __init__(self,driver= None):
        if driver is None:
            option=Options()
            option.debugger_address="localhost:9222"
            self.driver=webdriver.Chrome(options=option)
            self.driver.maximize_window()
            self.driver.implicitly_wait(3)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        else:
            self.driver: WebDriver=driver
    def wait_for_visibility(self,locator,time=10):
        WebDriverWait(self.driver,time).until(expected_conditions.visibility_of_element_located(locator))
    def time(self,timeout=5):
        time.sleep(5)
    def quit(self):
        self.driver.quit()