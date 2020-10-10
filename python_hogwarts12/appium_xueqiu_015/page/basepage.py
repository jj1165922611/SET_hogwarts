#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-09-29
# @Author     : Joey Jiang
# @File       : basepage.py
# @Software   : PyCharm
# @Description: 打造自己的测试框架
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    _black_list=[
        (MobileBy.XPATH,'//*[@text="确定"]'),
        (MobileBy.XPATH,'//*[@text="下次再说"]')
    ]
    _error_num=0
    _max_num=5
    def __init__(self,driver: WebDriver=None):
        self._driver=driver

    def find(self,locator,value):
        try:
            if isinstance(locator,tuple):
                ele=self._driver.find_element(*locator)
            else:
                ele=self._driver.find_element(locator,value)
            self._error_num=0
            return ele
        except Exception as e:
            if self._error_num >=self._max_num:
                raise e
            self._error_num+=1
            for black in self._black_list:
                ele=self._driver.find_elements(*black)
                if len(ele)>0:
                    ele[0].click()
                return self.find(locator.value)
            raise e