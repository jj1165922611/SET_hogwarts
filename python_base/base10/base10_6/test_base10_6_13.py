#!/usr/bin/env python
# -*-coding: utf-8 -*-
# @Time       : 2020-05-24
# @Author     : Joey Jiang
# @File       : test_base10_6_13.py
# @Software   : PyCharm
# @Description: web控件的交互进阶
from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By


class TestForm:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
    def teardown(self):
        self.driver.quit()

    def test_touch_action(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element(By.XPATH,'//*[@id="user_login"]').send_keys("132131")
        self.driver.find_element(By.ID,"user_password").send_keys("131312")
        self.driver.find_element(By.ID,"user_remember_me").click()
        self.driver.find_element(By.XPATH,'//*[@id="new_user"]/div[4]/input').click()
        sleep(2)

