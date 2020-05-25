#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-25
# @Author     : Joey Jiang
# @File       : test_base11_3_2.py
# @Software   : PyCharm
# @Description: 文件上传弹框处理
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestFileUpload:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
    def teardown(self):
        self.driver.quit()
    def test_file_upload(self):
        self.driver.get("https://image.baidu.com")
        sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="sttb"]/img[1]').click()
        self.driver.find_element(By.ID,"stfile").send_keys("G:/python/1.png")
        sleep(3)
