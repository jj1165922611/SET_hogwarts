#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020/11/8 0008 20:10
# @Author     : Joey Jiang
# @File       : add_member_page.py
# @Software   : PyCharm
# @Description: 添加成员页
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from python_hogwarts_base2.base18_3.page.base_page import BasePage


class AddMemberPage(BasePage):

    def add_member(self,name,account,phone):
        self.wait_for_visibility((By.ID, "username"))
        self.driver.find_element_by_id("username").send_keys(name)
        self.driver.find_element_by_id("memberAdd_acctid").send_keys(account)
        self.driver.find_element_by_id("memberAdd_phone").send_keys(phone)
        return self
    def save_member(self):
        self.driver.find_element_by_link_text("保存").click()
    def cancel_member(self):
        pass