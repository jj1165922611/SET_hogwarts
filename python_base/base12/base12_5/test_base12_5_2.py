#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-30
# @Author     : Joey Jiang
# @File       : test_base12_5_1.py
# @Software   : PyCharm
# @Description: app控件交互
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


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
    def test_locator(self):
        '''
        1.打开【雪球】应用首页
        2.定位首页的搜索框
        3.判断搜索框是否可用, 并查看搜索框name属性
        4.打印搜索框这个元素的左上角坐标和它的宽高
        5.向搜索框输入：alibaba
        6.判断【阿里巴巴】是否可见
        7.如果可见打印“搜索成功”，如果不可见打印“搜索失败”
        '''
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/home_search").click()
        search_box=self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        if search_box.is_enabled():
            print(search_box.text)
            search_box.send_keys("alibaba")
            print(search_box.is_enabled())
            print(search_box.size)
            print(search_box.location)
            search_box.click()
        ele_alibaba= self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/name" and @text="阿里巴巴"]')
        print(ele_alibaba.is_displayed())
        if ele_alibaba.is_displayed():
            print("搜索成功")
        else:
            print("搜索失败")