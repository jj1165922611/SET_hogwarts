#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020/11/8 17:55
# @Author     : Joey Jiang
# @File       : test_reuse_browser.py
# @Software   : PyCharm
# @Description: 复用浏览器

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
class TestReuseBrowser:
    def setup(self):
        option=Options()
        option.debugger_address="localhost:9222"
        self.driver=webdriver.Chrome(options=option)
    def teardown(self):
        self.driver.quit()
    def test_reuse_browser(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")

