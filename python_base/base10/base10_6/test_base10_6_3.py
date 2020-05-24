#!/usr/bin/env python
# -*-coding: utf-8 -*-
# @Time       : 2020-05-24
# @Author     : Joey Jiang
# @File       : test_base10_6_3.py
# @Software   : PyCharm
# @Description: web控件的交互进阶
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

    def test_action_chains_drag_and_drop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        element=self.driver.find_element(By.ID,"dragger")
        targat1=self.driver.find_element(By.XPATH,'//*[@class="item dropped"][1]')
        targat2=self.driver.find_element(By.XPATH,'//*[@class="item dropped"][2]')
        targat3=self.driver.find_element(By.XPATH,'//*[@class="item dropped"][3]')
        # targat4=self.driver.find_element(By.XPATH,'//div[@class="item dragover dropped"]')
        action=ActionChains(self.driver)
        action.drag_and_drop(element,targat1)
        action.drag_and_drop(element,targat2)
        action.drag_and_drop(element,targat3)
        # action.drag_and_drop(element,targat4)
        action.perform()
        sleep(3)