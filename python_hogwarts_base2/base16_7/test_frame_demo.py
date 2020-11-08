#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-11-08
# @Author     : Joey Jiang
# @File       : test_frame_demo.py
# @Software   : PyCharm
# @Description: 网页frame

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestFrameDemo:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
    def teardown(self):
        self.driver.quit()
    def test_frame(self):
        #1、进入页面
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        #2、处理下页面的异常
        self.driver.find_element_by_link_text("显示异常").click()
        #3、切换到iframe
        self.driver.switch_to.frame("iframeResult")
        #4、打印"请拖拽我"
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located((By.ID,"draggable")))
        print(self.driver.find_element_by_id("draggable").text)
        #5、切换回父节点
        self.driver.switch_to.parent_frame()
        #6、打印"点击运行"
        print(self.driver.find_element_by_id("submitBTN").text)