#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-31
# @Author     : Joey Jiang
# @File       : test_base12_6_3.py
# @Software   : PyCharm
# @Description: 触屏操作自动化、
'''
滑动：使用相对坐标
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
            window_rect = self.driver.get_window_rect()
            width=window_rect['width']
            height=window_rect['height']
            action=TouchAction(self.driver)
            x1=int(width/2)
            y1_start=int(height*0.8)
            y1_end=int(height/5)
            action.press(x=x1,y=y1_start).wait(200).move_to(x=x1,y=y1_end).release().perform()
