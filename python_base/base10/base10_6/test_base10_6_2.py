#!/usr/bin/env python
# -*-coding: utf-8 -*-
# @Time       : 2020-05-24
# @Author     : Joey Jiang
# @File       : test_base10_6_2.py
# @Software   : PyCharm
# @Description: web控件的交互进阶
'''
ActionChains()：

鼠标移动到某个元素上:move_to_element()

分布写法
'''
from time import sleep

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

    def test_action_chains_move_to(self):
        self.driver.get("https://www.baidu.com")
        element=self.driver.find_element(By.ID,"s-usersetting-top")
        action=ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()
        sleep(3)