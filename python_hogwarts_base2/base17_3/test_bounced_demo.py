#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020/11/8 15:35
# @Author     : Joey Jiang
# @File       : test_bounced_demo.py
# @Software   : PyCharm
# @Description: 弹框处理
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestBouncedDemo:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
    def teardown(self):
        self.driver.quit()
    def test_bounced_demo(self):
        #1、进入页面
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        #2、解决异常
        self.driver.find_element_by_link_text("显示异常").click()
        #3、进入iframe
        self.driver.switch_to.frame("iframeResult")
        ele=(By.ID,"draggable")
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(ele))
        #4、拖拽元素到指定位置
        drag=self.driver.find_element_by_id("draggable")
        drop=self.driver.find_element_by_id("droppable")
        action=ActionChains(self.driver)
        action.drag_and_drop(drag,drop)
        action.perform()
        #5、处理弹框
        alert=self.driver.switch_to.alert
        alert.accept()
        #6、点击"点击运行"
        self.driver.switch_to.parent_frame()
        self.driver.find_element_by_id("submitBTN").click()