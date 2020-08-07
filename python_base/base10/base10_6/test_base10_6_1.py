#!/usr/bin/env python
# -*-coding: utf-8 -*-
# @Time       : 2020-05-24
# @Author     : Joey Jiang
# @File       : test_base10_6_1.py
# @Software   : PyCharm
# @Description: web控件的交互进阶

'''
ActionChains()：

点击：click()
双击：double_click
右击：context_click

分布写法
'''
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestActionChains:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_action_chains_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        action=ActionChains(self.driver)
        # action.double_click(self.driver.find_element(By.XPATH, '//*[@name="f1"]//input[2]'))
        action.double_click(self.driver.find_element(By.XPATH, '//input[@value="dbl click me"]'))
        action.click(self.driver.find_element(By.XPATH, '//*[@name="f1"]//input[3]'))
        action.context_click(self.driver.find_element(By.XPATH, '//*[@name="f1"]//input[4]'))
        action.perform()
        ele=self.driver.find_element(By.CSS_SELECTOR,'[name="t2"]').get_attribute("value")
        print(ele)