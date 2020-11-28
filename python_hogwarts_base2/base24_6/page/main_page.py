#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020/11/21 8:18
# @Author     : Joey Jiang
# @File       : main_page.py
# @Software   : PyCharm
# @Description: 主页面
from python_hogwarts_base2.base24_6.page.addresslist_page import AddresslistPage
from python_hogwarts_base2.base24_6.page.basepage import BasePage


class MainPage(BasePage):
    def goto_addresslist(self):
        return AddresslistPage()

    def goto_workbench(self):
        pass