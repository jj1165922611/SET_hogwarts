#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020/11/17 23:03
# @Author     : Joey Jiang
# @File       : test_toast.py
# @Software   : PyCharm
# @Description: 特殊控件toast定位
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestToast:
    def setup(self):
        desired_caps={}
        desired_caps["platformName"]="Android"
        desired_caps["platformVersion"]="6.0"
        desired_caps["deviceName"]="emulator-5554"
        desired_caps["appPackage"]="com.touchboarder.android.api.demos"
        desired_caps["appActivity"]="com.touchboarder.androidapidemos.MainActivity"
        desired_caps["noReset"]="true"
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        self.driver.implicitly_wait(3)
    def teardown(self):
        self.driver.quit()
    def test_toast(self):
        locator1=(MobileBy.XPATH,"//*[@resource-id='android:id/text1' and @text='API Demos']")
        ele1=WebDriverWait(self.driver,10).until(lambda x:self.driver.find_element(*locator1))
        ele1.click()
        locator2=(MobileBy.XPATH,"//*[@resource-id='android:id/text1' and @text='Views']")
        ele2=WebDriverWait(self.driver,10).until(lambda x:self.driver.find_element(*locator2))
        ele2.click()

        ele3=self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Popup Menu").instance(0));')
        ele3.click()

        self.driver.find_element(MobileBy.XPATH,"//*[@text='Make a Popup!']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='android:id/title' and @text='Search']").click()
        print(self.driver.page_source)
        print(self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text)
