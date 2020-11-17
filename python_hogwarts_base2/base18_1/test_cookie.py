#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020/11/8 18:32
# @Author     : Joey Jiang
# @File       : test_cookie.py
# @Software   : PyCharm
# @Description: 使用cookie自动化登录
import json
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestCookie:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
    def teardown(self):
        self.driver.quit()
    def get_cookie(self):
        ele=(By.XPATH,"//*[@node-type='import']")
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(ele))
        cookies=self.driver.get_cookies()
        with open("cookie.json","w") as f:
            json.dump(cookies,f)

    def test_import_contact(self):
        # 1、进入页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        #2、如果不存在cookie文件，调用get_cookie方法
        if not os.path.exists("cookie.json"):
            self.get_cookie()
        #3、否则添加cookie
        else:
            with open("cookie.json","rb") as f:
                cookies=json.load(f)
                for i in cookies:
                    self.driver.add_cookie(i)
        #4、添加cookie后需要重新进入页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        time.sleep(3)
        #5、点击导入通讯录
        self.driver.find_element(By.XPATH,"//*[@node-type='import']").click()