#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-24
# @Author     : Joey Jiang
# @File       : test_base11_2_10.py
# @Software   : PyCharm
# @Description: 执行javaScript脚本
'''
时间控件

使用强制等待
    页面上的值改变了
    控制台的输出是对的
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
        self.driver.get("https://www.12306.cn/index/")
        self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        sleep(2)
        self.driver.execute_script("document.getElementById('train_date').value='2020-12-30'")
        sleep(2)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))