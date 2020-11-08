#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2020-11-08
# @Author     : Joey Jiang
# @File       : test_image_input_demo.py
# @Software   : PyCharm
# @Description: 图片上传
import os

from selenium import webdriver


class TestImagInputDemo:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
    def teardown(self):
        self.driver.quit()
    def test_image_input(self):
        path=os.path.dirname(__file__)
        print(path)
        #1、进入百度图片首页
        self.driver.get("https://image.baidu.com/")
        #2、点击搜索框中的照相机图标
        self.driver.find_element_by_id("sttb").click()
        #3、选择本地上传，输入图片路径
        self.driver.find_element_by_id("stfile").send_keys(f"{path}\\1.png")