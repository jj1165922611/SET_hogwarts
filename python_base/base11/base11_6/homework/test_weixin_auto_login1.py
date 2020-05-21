#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-21
# @Author     : Joey Jiang
# @File       : test_weixin_auto_login1.py
# @Software   : PyCharm
# @Description: 企业微信的自动化登录

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
class TestLogin:
    def setup(self):
        # 1.实例化Options类
        option = Options()
        # 2.将url"localhost:9222"赋值给类中的属性debugger_address
        option.debugger_address = "localhost:9222"
        # 3.使用webdriverd的Chrome方法打开Google浏览器，并打开传入参数中的url
        self.driver = webdriver.Chrome(options=option)
        # 4.浏览器窗口最大化
        self.driver.maximize_window()
    def test_login(self):
        # 5.打开企业微信的url
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
    def teardown(self):
        # 6.退出浏览器并释放资源
        self.driver.quit()