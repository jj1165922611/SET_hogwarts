#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-23
# @Author     : Joey Jiang
# @File       : test_10_5_1.py
# @Software   : PyCharm
# @Description: web控件定位与常见操作
'''
xpath和css selector

xpath完全支持selenium和appium
css selector完全支持selenium；appium因为Android的原生控件没有使用css样式，所以一般出现webview表示手机软件中嵌套网页时才可以使用
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
    def teardown(self):
        self.driver.quit()
    def test_locator(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys("selenium")
        self.driver.find_element(By.CSS_SELECTOR,'[id=su]').click()
        WebDriverWait(self.driver,3).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@id="s_tab"]//a[2]')))
        ele=self.driver.find_elements(By.CSS_SELECTOR,'#s_tab a:nth-child(2)')
        print(ele)