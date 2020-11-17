#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020/11/8 20:08
# @Author     : Joey Jiang
# @File       : main_page.py
# @Software   : PyCharm
# @Description: 主页
from selenium.webdriver.remote.webdriver import WebDriver

from python_hogwarts_base2.base18_3.page.base_page import BasePage
from python_hogwarts_base2.base18_3.page.contact_page import ContactPage


class MainPage(BasePage):

    def go_to_contact(self):
        # 点击进入通讯录页面
        self.driver.find_element_by_id("menu_contacts").click()
        return ContactPage(self.driver)