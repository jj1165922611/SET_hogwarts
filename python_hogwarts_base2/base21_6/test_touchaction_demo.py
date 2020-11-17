#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020/11/17 19:34
# @Author     : Joey Jiang
# @File       : test_touchaction_demo.py
# @Software   : PyCharm
# @Description: 触摸自动化
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestTouchAction:
    def setup(self):
        desired_caps={}
        desired_caps["platformName"]="Android"
        desired_caps["platformVersion"]="6.0"
        desired_caps["appPackage"]="cn.kmob.screenfingermovelock"
        desired_caps["appActivity"]="com.samsung.ui.FlashActivity"
        desired_caps["deviceName"]="emulator-5554"
        desired_caps["noReset"]="true"
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        self.driver.implicitly_wait(3)
    def teardown(self):
        self.driver.quit()
    def test_touchaction(self):
        self.driver.find_element_by_xpath("//*[@resource-id='cn.kmob.screenfingermovelock:id/patternTxt']").click()
        ele=(By.ID,"cn.kmob.screenfingermovelock:id/btnOne")
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(ele))
        action=TouchAction(self.driver)
        action.press(x=181,y=272).wait(300).move_to(x=540,y=272).wait(300).\
            move_to(x=540,y=634).wait(300).move_to(x=540,y=994).wait(300).move_to(x=900,y=994).release()
        action.perform()

