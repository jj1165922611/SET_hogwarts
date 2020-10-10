#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-10-06
# @Author     : Joey Jiang
# @File       : basepage.py
# @Software   : PyCharm
# @Description: pageobject改造
import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

'''
*By
    ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"
*MobileBy
    IOS_PREDICATE = '-ios predicate string'
    IOS_UIAUTOMATION = '-ios uiautomation'
    IOS_CLASS_CHAIN = '-ios class chain'
    ANDROID_UIAUTOMATOR = '-android uiautomator'
    ANDROID_VIEWTAG = '-android viewtag'
    ANDROID_DATA_MATCHER = '-android datamatcher'
    ANDROID_VIEW_MATCHER = '-android viewmatcher'
    WINDOWS_UI_AUTOMATION = '-windows uiautomation'
    ACCESSIBILITY_ID = 'accessibility id'
    IMAGE = '-image'
    CUSTOM = '-custom'
'''
class BasePage:
    _driver: WebDriver = None  # 子类中就可以使用
    _by = "by"
    _locator = "locator"
    _send_keys = "send_keys"
    _action = "action"
    _click = "click"

    _black_list=[
        (MobileBy.XPATH,"//*[@text='下次再说']"),
        (MobileBy.XPATH,"//*[@text='确定']"),
        (MobileBy.XPATH,"//*[@text='取消']"),
    ]

    _error_num=0
    _max_num=5
    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator, value: str = None):
        try:
            if isinstance(locator, tuple):
                ele = self._driver.find_element(*locator)
            else:
                ele = self._driver.find_element(locator, value)
            self._error_num=0
            return ele
        except Exception as e:
            if self._error_num>=self._max_num:
                raise e
            self._error_num+=1
            for black in self._black_list:
                elements=self._driver.find_elements(black)
                if len(elements)>0:
                    elements[0].click()
                    break
            return self.find(locator,value)

    def steps(self, file):
        by = self._by
        locator = self._locator
        action = self._action
        click = self._click
        send_keys = self._send_keys
        with open(file, "rb") as f:
            steps = yaml.safe_load(f)
        for step in steps:
            ele = None
            if by in step.keys():
                ele = self.find(step[by], step[locator])
            if action in step.keys():
                if step[action] == click:
                    ele.click()
            if send_keys in step.keys():
                ele.send_keys(step[send_keys])
