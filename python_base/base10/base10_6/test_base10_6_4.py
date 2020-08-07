#!/usr/bin/env python
# -*-coding: utf-8 -*-
# @Time       : 2020-05-24
# @Author     : Joey Jiang
# @File       : test_base10_6_4.py
# @Software   : PyCharm
# @Description: web控件的交互进阶
'''
ActionChains()：

拖拽元素:drag_and_drop(source,target)
pause()可以实现动作之间的等待

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

    def teardown(self):
        self.driver.quit()

    def test_action_chains_drag_and_drop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        element=self.driver.find_element(By.ID,'dragger')
        target1=self.driver.find_element(By.XPATH,'/html/body/div[2]')
        target2=self.driver.find_element(By.XPATH,'/html/body/div[3]')
        target3=self.driver.find_element(By.XPATH,'/html/body/div[4]')
        target4=self.driver.find_element(By.XPATH,'/html/body/div[5]')
        actions=ActionChains(self.driver)
        actions.drag_and_drop(element,target1).pause(1)
        actions.drag_and_drop(element,target2).pause(1)
        actions.drag_and_drop(element,target3).pause(1)
        # actions.drag_and_drop(element,target4).pause(1)
        actions.click_and_hold(element).move_to_element(target4).release().pause(1)
        actions.perform()