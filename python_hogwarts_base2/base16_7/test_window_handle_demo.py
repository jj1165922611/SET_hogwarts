#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-11-08
# @Author     : Joey Jiang
# @File       : test_window_handle_demo.py
# @Software   : PyCharm
# @Description: 多窗口切换
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWindowHandle:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
    def teardown(self):
        self.driver.quit()
    def test_handle(self):
        #1、进入百度首页
        self.driver.get("https://www.baidu.com")
        #2、点击登录按钮
        self.driver.find_element_by_link_text("登录").click()
        current_window=self.driver.current_window_handle
        #3、在弹框中点击立即注册
        self.driver.find_element_by_link_text("立即注册").click()
        window_handles=self.driver.window_handles
        #4、在新打开的窗口中输入注册信息
        self.driver.switch_to.window(window_handles[-1])
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located((By.ID,"TANGRAM__PSP_4__userName")))
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("我是谁")
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("123145")
        #5、返回登录页，输入用户名和密码进行登录
        self.driver.switch_to.window(current_window)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.ID, "TANGRAM__PSP_11__footerULoginBtn")))
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()