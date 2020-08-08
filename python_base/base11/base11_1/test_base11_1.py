#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-24
# @Author     : Joey Jiang
# @File       : test_base11_1.py
# @Software   : PyCharm
# @Description: selenium多浏览器处理
'''
测试类继承Base类后，可以直接使用父类中的方法。

命令行执行：
    windows：set browser=chrome
            pytest test_base11_1.py
    others：browser=chrome pytest test_base_11_1.py
'''
from selenium import webdriver
import os

from selenium.webdriver.common.by import By

from python_base.base11.base11_1.base import Base
class TestFrame(Base):
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try-cdnjs.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        print(self.driver.find_element(By.ID, "droppable").text)
        print(self.driver.find_element(By.ID, "draggable").text)