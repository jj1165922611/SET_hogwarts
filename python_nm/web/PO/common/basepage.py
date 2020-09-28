#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-09-17
# @Author     : Joey Jiang
# @File       : basepage.py
# @Software   : PyCharm
# @Description: 所有页面的父类
import logging

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self,driver: WebDriver=None):
        if driver==None:
            self.driver=webdriver.Chrome()
        else:
            self.driver=driver
    def wait_ele_visiable(self,ele):
        logging.info("元素已经出现")
        try:
            WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(ele))
        except:
            self.sava_screenshot()
            logging.exception("等待元素出现失败")
            raise
    def find_element(self,ele):
        logging.info(f"查找元素{ele}")
        try:
           return self.driver.find_element(*ele)
        except:
            self.save_screenshot()
            logging.exception(f"查找元素{ele}失败")
            raise
    def click(self,ele,page):
        logging.info(f"在{page}页面点击元素")
        try:
            self.wait_ele_visiable(ele)
            self.find_element(ele).click()
        except:
            self.sava_screenshot()
            logging.exception("不错")
            raise
    def sava_screenshot(self):
        pass