#!/usr/bin/env python
# -*-coding: utf-8 -*-
# @Time       : 2020-05-24
# @Author     : Joey Jiang
# @File       : test_base10_7_1.py
# @Software   : PyCharm
# @Description: 多窗口处理与网页frame
'''
立即注册的定位方式不对
'''
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestWindow:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
    def teardown(self):
        self.driver.quit()
    def test_window(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element(By.XPATH,'//*[@id="u1"]/a[2]').click()
        # 定位方式不对
        self.driver.find_element(By.LINK_TEXT,'//*[@id="passport-login-pop-dialog"]/div/div/div/div[3]/a').click()
        current_handle=self.driver.current_window_handle
        all_handle=self.driver.window_handles
        self.driver.switch_to.window(all_handle[1])
        sleep(3)
        self.driver.find_element(By.ID, 'TANGRAM__PSP_4__userName').send_keys("哈哈")
        self.driver.find_element(By.ID, 'TANGRAM__PSP_4__phone').send_keys("17123213212")
        self.driver.find_element(By.ID, 'TANGRAM__PSP_4__password').send_keys("123456jj")
        self.driver.find_element(By.ID, 'TANGRAM__PSP_4__verifyCode').send_keys("123456")
        self.driver.find_element(By.ID, 'TANGRAM__PSP_4__isAgree').click()
        self.driver.find_element(By.ID, 'TANGRAM__PSP_4__submit').click()
        self.driver.switch_to.window(current_handle)
        sleep(2)
        # 有问题