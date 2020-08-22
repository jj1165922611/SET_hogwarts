#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-08-22
# @Author     : Joey Jiang
# @File       : app.py
# @Software   : PyCharm
# @Descrtption: 企业微信自动化测试实战
from appium import webdriver

from python_base.base15.homework.page.base import BasePage
from python_base.base15.homework.page.main import Main


class App(BasePage):
    _appPackage='com.tencent.wework'
    _appActivity='com.tencent.wework.launch.WwMainActivity'
    def start(self):
        if self._driver==None:
            descriped_caps={}
            descriped_caps['platformName']='Android'
            descriped_caps['platformVersion']='6.0'
            descriped_caps['deviceName']='127.0.0.1:7555'
            descriped_caps['appPackage']=self._appPackage
            descriped_caps['appActivity']=self._appActivity
            descriped_caps['noReset']=True
            self._driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',descriped_caps)
        else:
            self._driver.start_activity(self._appPackage,self._appActivity)
        self._driver.implicitly_wait(6)
        return self
    def restart(self):
        pass
    def stop(self):
        pass
    def main(self):
        return Main(self._driver)