#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-23
# @Author     : Joey Jiang
# @File       : contact.py
# @Software   : PyCharm
# @Description: Page Object演练
from selenium import webdriver
from selenium.webdriver.common.by import By


class Contact:
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def get_member(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        member_list=self.driver.find_elements(By.CSS_SELECTOR,"member_colRight_memberTable ww_table js_ww_table[2]")
        list=[]
        for i in member_list:
            member=i.get_attribute()


