#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020/11/21 0021 8:43
# @Author     : Joey Jiang
# @File       : basepage.py
# @Software   : PyCharm
# @Description: po封装

'''
基类,最基本的方法，初始化driver，封装find、显示等待。。。
'''
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_and_click(self, locator):
        self.find(locator).click()

    def find_and_sendkeys(self, locator, value):
        self.find(locator).send_keys(value)

    def scroll_find(self, text):
        '''
        滚动查找元素
        :param text:
        :return:
        '''
        return self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).'
            'instance(0)).scrollIntoView(new UiSelector().'
            f'text("{text}").instance(0));')
