#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-21
# @Author     : Joey Jiang
# @File       : test_weixin_auto_login1.py
# @Software   : PyCharm
# @Description: 企业微信的自动化登录

from selenium import webdriver
import time,json


class TestLogin:
    def setup(self):
        # 1.使用webdriver的Chrome方法打开google浏览器
        self.driver = webdriver.Chrome()
        # 2.最大化浏览器窗口
        self.driver.maximize_window()
    '''
    *获取cookie
    *参数
        driver: 浏览器驱动
    '''
    def get_cookie(self):
        # 3.打开企业微信url
        self.driver.get("https://work.weixin.qq.com/")
        # 4.等待10秒进行扫码登录的操作
        time.sleep(10)
        # 5.使用get_cookies方法获取当前窗口中的cookies，并存入变量cookie。获取到的cookie数据类型为list
        cookie = self.driver.get_cookies()
        # 6.将获取到的cookies存入json文件中
        with open("cookie.json", "w") as f:
            json.dump(obj=cookie, fp=f)

    def test_set_cookie(self):
        self.get_cookie()
        # 7.读取文件中的cookies
        with open("cookie.json","rb") as f:
            cookies=json.load(f)
        # 8.获取cookies中的cookie
        for cookie in cookies:
            # 判断cookie的key是否为expirt
            if "expiry" in cookie:
                # 删除字典中的expiry键值
                cookie.pop("expiry")
            # 添加一个cookie
            self.driver.add_cookie(cookie)
        time.sleep(2)
        # 9.打开企业微信首页的url
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        time.sleep(2)
    def teardown(self):
        # 10.退出浏览器并释放资源
        self.driver.quit()