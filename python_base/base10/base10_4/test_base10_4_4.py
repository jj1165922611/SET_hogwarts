#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-23
# @Author     : Joey Jiang
# @File       : test_base10_4_4.py
# @Software   : PyCharm
# @Description: 隐式等待与显式等待
import time

from selenium import webdriver
import time,pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
class TestWait:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)
    def test_wait(self):
        self.driver.get("https://home.testing-studio.com/")
        # time.sleep(3)
        self.driver.find_element_by_xpath('//*[@title="归入各种类别的所有主题"]').click()
        print("Hello")
        # time.sleep(2)
        # def wait(x):
        #     return len(self.driver.find_elements(By.XPATH,'//*[@class="table-heading"]'))>=1
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@class="table-heading"]')))
        self.driver.find_element_by_xpath('//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()
    def teardown(self):
        self.driver.quit()