#!/usr/bin/env python
# -*-coding: utf-8 -*-
# @Time       : 2020-05-24
# @Author     : Joey Jiang
# @File       : test_base10_6_11.py
# @Software   : PyCharm
# @Description: web控件的交互进阶

'''
TouchActions手势控制

报错：w3c
'''
from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By


class TestTouchAction:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
    def teardown(self):
        self.driver.quit()

    def test_touch_action(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element(By.ID, "kw").send_keys("selenium测试")
        ele1=self.driver.find_element(By.ID,"su")
        action=TouchActions(self.driver)
        action.tap(ele1)
        action.scroll(0,10000)
        action.perform()
        sleep(2)
        ele2 = self.driver.find_element(By.LINK_TEXT, "下一页>").click()
        sleep(2)
        # 有问题

