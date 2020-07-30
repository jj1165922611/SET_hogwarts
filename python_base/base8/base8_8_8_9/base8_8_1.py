#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-10
# @Author     : Joey Jiang
# @File       : base8_8_1.py
# @SOftware   : Visual Studio Code
# @Description: python外部源文件处理（二）

from selenium import webdriver
import time
from openpyxl import load_workbook

class SeleniumPython:
    def __init__(self):
        self.wb=load_workbook("selenium.xlsx")
        self.sheet=self.wb["Sheet1"]
    def go_to_baidu(self):
        driver=webdriver.Chrome()
        driver.get("https://www.baidu.com/")
        driver.find_element_by_id("kw").send_keys(self.sheet["A2"].value)
        driver.find_element_by_id("su").click()
        time.sleep(3)
        driver.quit()
SeleniumPython().go_to_baidu()