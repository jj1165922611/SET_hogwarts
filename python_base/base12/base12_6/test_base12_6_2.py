#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-31
# @Author     : Joey Jiang
# @File       : test_base12_6_2.py
# @Software   : PyCharm
# @Description: 触屏操作自动化
'''
滑动：使用绝对坐标
'''
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction


class TestLocator:
    def setup(self):
        desired_caps={}
        desired_caps['platformName']='Android'
        desired_caps['platformVersion']='6.0'
        desired_caps['deviceName']='127.0.0.1:7555'
        desired_caps['appPackage']='com.xueqiu.android'
        desired_caps['appActivity']='.view.WelcomeActivityAlias'
        desired_caps['noReset']=True
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        self.driver.implicitly_wait(20)
    def teardown(self):
        self.driver.quit()
    def test_touch_action(self):
        ele=self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/home_search")
        if ele.is_enabled():
            action=TouchAction(self.driver)
            action.press(x=36,y=688).wait(200).move_to(x=36,y=32).release().perform()
        # 不推荐使用绝对坐标定位