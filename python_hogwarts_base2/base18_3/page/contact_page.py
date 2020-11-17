#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020/11/8 20:09
# @Author     : Joey Jiang
# @File       : contact_page.py
# @Software   : PyCharm
# @Description: 联系人页
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from python_hogwarts_base2.base18_3.page.add_member_page import AddMemberPage
from python_hogwarts_base2.base18_3.page.base_page import BasePage


class ContactPage(BasePage):

    def go_to_add_member(self):
        # 点击进入添加成员页面
        self.wait_for_visibility((By.ID,"member_list"))
        self.driver.find_element_by_link_text("添加成员").click()
        return AddMemberPage(self.driver)
    def get_member_list(self):
        pass