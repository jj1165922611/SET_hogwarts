#!/usr/bin/env python
# -*-coding: utf-8 -*-
# @Time       : 2020-05-24
# @Author     : Joey Jiang
# @File       : test_base10_6_8.py
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
        input1=self.driver.find_element(By.XPATH,'/html/body/label[1]/input')
        input2=self.driver.find_element(By.XPATH,'/html/body/label[2]//input')
        action=ActionChains(self.driver)
        input1.click()
        action.send_keys("username").pause(1).send_keys(Keys.SPACE).pause(1)
        action.send_keys("tome").pause(1).send_keys(Keys.BACK_SPACE).pause(1)
        action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).pause(1)
        action.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).pause(1)
        input2.click()
        action.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).pause(1)
        action.perform()
        # 有问题