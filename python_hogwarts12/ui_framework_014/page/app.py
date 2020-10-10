#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-10-06
# @Author     : Joey Jiang
# @File       : basepage.py
# @Software   : PyCharm
# @Description: pageobject改造
import yaml
from appium import webdriver

from python_hogwarts12.ui_framework_014.page.basepage import BasePage
from python_hogwarts12.ui_framework_014.page.main import Main


class App(BasePage):
    _appPackage="com.xueqiu.android"
    _appActivity=".view.WelcomeActivityAlias"
    def start(self):
        if self._driver is None:
            desired_caps=dict()
            desired_caps["platformName"]='Android'
            desired_caps["platformVersion"]='6.0'
            desired_caps["deviceName"]='emulator 4444'
            desired_caps["appPackage"]=self._appPackage
            desired_caps["appActivity"]=self._appActivity
            desired_caps['noReset']='true'
            desired_caps['udid']=yaml.safe_load(open("../page/configuration.yaml"))['caps']['udid']
            self._driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        else:
            self._driver.launch_app()
        # 隐式等待时间为3秒
        self._driver.implicitly_wait(10)
        # 返回类的实例
        return self
    def main(self) -> Main:
        return Main(self._driver)