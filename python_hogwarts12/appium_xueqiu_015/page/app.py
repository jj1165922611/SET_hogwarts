#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-09-2
# @Author     : Joey Jiang
# @File       : app.py
# @Software   : PyCharm
# @Description: 打造自己的测试框架
from appium import webdriver

from python_hogwarts12.appium_xueqiu_015.page.basepage import BasePage


class App(BasePage):
    _appPackage="com.xueqiu.android"
    _appActivity=".view.WelcomeActivityAlias"
    def start(self):
        if self._driver is None:
            desired_caps={}
            desired_caps['platformName']="Android"
            desired_caps['platformVersion']="6.0"
            desired_caps['appPackage']=self._appPackage
            desired_caps['appActivity']=self._appActivity
            desired_caps['noReset']='true'
            self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        else:
            self._driver.launch_app()
        self._driver.implicitly_wait(5)
        return self
    def stop(self):
        pass
    def restart(self):
        pass
    def main(self):
        pass