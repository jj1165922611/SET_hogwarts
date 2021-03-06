#!/usr/bin/env python
# -*-coding: utf-8 -*-
# @Time       : 2020-05-24
# @Author     : Joey Jiang
# @File       : test_base10_7_5.py
# @Software   : PyCharm
# @Description: 多窗口处理与网页frame
'''
多frame切换
'''
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestFrame:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
    def teardown(self):
        self.driver.quit()
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try-cdnjs.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        self.driver.find_element(By.ID,"draggable").text
        self.driver.find_element(By.ID,"droppable").text
        # 有问题