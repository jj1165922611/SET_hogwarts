#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-27
# @Author     : Joey Jiang
# @File       : base_page.py
# @Software   : PyCharm
# @Description: 企业微信web端自动化测试实战（一）
import json
import os
import time
from decimal import Decimal

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By

'''
BasePage类是所有page object的父类，为子类提供公共的方法，比如driver的初始化和退出
'''
class BasePage:
    global _conf
    global _time
    global _url
    with open("../page/conf.yaml", "rb") as f:
        _conf = yaml.safe_load(f)
        _time=_conf['time']
        _url=_conf['url']

    def __init__(self,driver1: webdriver = None):
        if driver1 is None:
            self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(_time)
            self._driver.maximize_window()
            self._driver.get(_url)
        else:
            self._driver=driver1

    def find(self,by,locator):
        return self._driver.find_element(by,locator)

    def finds(self,by,locator):
        return self._driver.find_elements(by,locator)

    def by_id(self):
        return By.ID
    def by_name(self):
        return By.NAME
    def by_tag_name(self):
        return By.TAG_NAME
    def by_link_text(self):
        return By.LINK_TEXT
    def by_partial_link_text(self):
        return By.PARTIAL_LINK_TEXT
    def by_xpath(self):
        return By.XPATH
    def by_css_selector(self):
        return By.CSS_SELECTOR
    def by_class_name(self):
        return By.CLASS_NAME

    def quit(self):
        self._driver.quit()

    def set_cookie(self):
        # 1、判断cookie.json是否存在，以及最后修改时间是否小于当前时间一天
        now=time.time()
        cookie_path="../page/cookie.json"
        if os.path.exists(cookie_path):
            if Decimal((now-os.path.getmtime(cookie_path))/3600) < 24:
                # 3、添加cookie
                with open(cookie_path, 'rb') as f:
                    cookies = json.load(f)
                for cookie in cookies:
                    if "expiry" in cookie:
                        cookie.pop("expiry")
                    self._driver.add_cookie(cookie)
                self._driver.get(_url)
                return
        # 2、获得cookie
        self._driver.get(_url)
        cookie=self._driver.get_cookies()
        with open(cookie_path,'w') as fp:
            json.dump(obj=cookie,fp=fp)
        self._driver.get(_url)
        # 3、添加cookie
        with open(cookie_path, 'rb') as f:
            cookies = json.load(f)
        for cookie in cookies:
            if "expiry" in cookie:
                cookie.pop("expiry")
            self._driver.add_cookie(cookie)
        self._driver.get(_url)
