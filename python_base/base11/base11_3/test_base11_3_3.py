#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-25
# @Author     : Joey Jiang
# @File       : test_base11_3_3.py
# @Software   : PyCharm
# @Description: 文件上传弹框处理
'''
弹框处理

获取弹窗：switch_to.alert()

text\accept()\dismiss()\send_keys()
'''
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestAlert:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
    def teardown(self):
        self.driver.quit()
    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        sleep(10) # 点击页面中的显示异常
        self.driver.switch_to.frame("iframeResult")
        ele1=self.driver.find_element(By.ID,"draggable")
        ele2=self.driver.find_element(By.ID,"droppable")
        action=ActionChains(self.driver)
        action.drag_and_drop(ele1,ele2)
        action.perform()
        sleep(2)
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.parent_frame()
        print(self.driver.find_element(By.ID, "submitBTN").text)
