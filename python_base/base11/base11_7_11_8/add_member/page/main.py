#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-23
# @Author     : Joey Jiang
# @File       : main.py
# @Software   : PyCharm
# @Description: Page Object演练

from selenium import webdriver

from python_base.base11.base11_7_11_8.add_member.page.add_member import AddMember
from python_base.base11.base11_7_11_8.add_member.page.contact import Contact
class Main:
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
    def goto_add_member(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element_by_css_selector('[class="index_service_cnt_item_title"]').click
        return AddMember()
