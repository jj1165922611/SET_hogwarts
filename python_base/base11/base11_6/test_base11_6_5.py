#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-21
# @Author     : Joey Jiang
# @File       : test_base11_6_2.py
# @Software   : PyCharm
# @Description: 企业微信的自动化登录
'''
获取cookie并存入json文件
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time,json

class TestCookie:
    def test_get_cookie(self):
        '''
        获取cookie
        :return:
        '''
        driver =webdriver.Chrome()
        driver.get("https://work.weixin.qq.com")
        time.sleep(10)
        cookie=driver.get_cookies()
        with open("cookie.json","w") as f:
            json.dump(obj=cookie,fp=f)
        driver.quit()