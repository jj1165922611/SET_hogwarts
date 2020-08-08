#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-21
# @Author     : Joey Jiang
# @File       : test_base11_6_4.py
# @Software   : PyCharm
# @Description: 企业微信的自动化登录
'''
读取json文件并使用cookie
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json
class TestCookie:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com")
    def test_get_cookie(self):
        with open("cookie.json","rb") as f:
            cookies=json.load(f)
        for cookie in cookies:
            if "expiry" in cookie:
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        time.sleep(2)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        time.sleep(3)
        self.driver.quit()