#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-08-22
# @Author     : Joey Jiang
# @File       : base.py
# @Software   : PyCharm
# @Descrtption: 企业微信自动化测试实战
import logging

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    logging.basicConfig(level=logging.INFO)
    _driver:WebDriver
    _black_list=[
        (By.XPATH,"//*[@text='下次再说']"),
        (By.XPATH,"//*[@text='确定']")
    ]
    _error_num=0
    _max_error_num=3
    def __init__(self,driver: WebDriver =None):
        self._driver=driver
    def find(self,locator,value :str=None):
        logging.info(locator)
        logging.info(value)
        try:
            if isinstance(locator,tuple):
                element=self._driver.find_element(*locator)
            else:
                element=self._driver.find_element(locator,value)
            self._error_num=0
            return element
        except Exception as e:
            if self._error_num>self._max_error_num:
                raise e
            self._error_num+=1
            for ele in self._black_list:
                logging.info(ele)
                ele_list=self._driver.find_elements(*ele)
                if len(ele_list)>0:
                    ele_list[0].click()
                    return self.find(locator,value)
                raise e


