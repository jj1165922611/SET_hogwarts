#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-31
# @Author     : Joey Jiang
# @File       : test_base12_6_5.py
# @Software   : PyCharm
# @Description: 触屏操作自动化
'''
手势解锁
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
        desired_caps['appPackage']='cn.kmob.screenfingermovelock'
        desired_caps['appActivity']='com.samsung.ui.FlashActivity'
        desired_caps['noReset']=True
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        self.driver.implicitly_wait(20)
    def teardown(self):
        self.driver.quit()
    def test_touch_action_gestures(self):
        ele=self.driver.find_element(MobileBy.ID, "cn.kmob.screenfingermovelock:id/setPatternLayout")
        if ele.is_enabled():
            ele.click()
        action=TouchAction(self.driver)
        action.press(x=95,y=140).wait(200).move_to(x=290,y=140).wait(200).move_to(x=480,y=140).wait(200)\
            .move_to(x=480,y=335).wait(200).move_to(x=480,y=525).release().perform()
    # 有问题
