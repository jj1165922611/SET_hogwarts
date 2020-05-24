#!/usr/bin/env python
# -*-coding: utf-8 -*-
# @Time       : 2020-05-24
# @Author     : Joey Jiang
# @File       : test_base10_6_6.py
# @Software   : PyCharm
# @Description: web控件的交互进阶
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestActionChains:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_action_chains_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        element=self.driver.find_element(By.XPATH,'/html/body/label[1]/input')
        action=ActionChains(self.driver)
        action.key_down(Keys.CONTROL).send_keys("aaaaa").key_up(Keys.CONTROL)
        action.send_keys(Keys.BACK_SPACE)
        action.perform()
        print(element.get_attribute("value"))
