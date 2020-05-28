#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-28
# @Author     : Joey Jiang
# @File       : test_14_6_14_7_14_8.py
# @Software   : PyCharm
# @Description: 雪球财经App测试实战1
from time import sleep

from appium import webdriver

class TestQiYeWeiXin:
    def setup(self):
        desired_caps={}
        desired_caps['platformName']='Android'
        desired_caps['platformVersion']='6.0'
        desired_caps['deviceName']='127.0.0.1:7555'
        desired_caps['appPackage']='com.tencent.wework'
        desired_caps['appActivity']='.launch.WwMainActivity'
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        self.driver.implicitly_wait(30)
    def teardown(self):
        self.driver.quit()
    def test_qi_ye_wei_xin(self):
        sleep(1)
        el1 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[2]/android.widget.TextView")
        sleep(1)
        el1.click()
        sleep(1)
        el2 = self.driver.find_element_by_id("com.tencent.wework:id/gw1")
        sleep(1)
        el2.click()
        sleep(1)
        el3 = self.driver.find_element_by_id("com.tencent.wework:id/fl3")
        sleep(1)
        el3.send_keys("川建国2")
        sleep(1)
        el3.click()
        sleep(1)
        el4 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout")
        sleep(1)
        el4.click()
        sleep(1)
        el5 = self.driver.find_element_by_id("com.tencent.wework:id/ac1")
        sleep(1)
        el5.click()
        sleep(1)
        el6 = self.driver.find_element_by_id("com.tencent.wework:id/dxy")
        sleep(1)
        el6.send_keys("测试code")
        sleep(1)
        el6.click()
        sleep(1)
        el7 = self.driver.find_element_by_id("com.tencent.wework:id/dxu")
        sleep(1)
        el7.click()
        sleep(5)