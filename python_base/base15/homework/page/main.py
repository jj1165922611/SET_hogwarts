#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-08-22
# @Author     : Joey Jiang
# @File       : main.py
# @Software   : PyCharm
# @Descrtption: 企业微信自动化测试实战
from appium.webdriver.common.mobileby import MobileBy

from python_base.base15.homework.page.address_list import AddressListPage
from python_base.base15.homework.page.base import BasePage


class Main(BasePage):
    def goto_message(self):
        pass
    def goto_contact(self):
        self.find(MobileBy.XPATH,'//*[@text="通讯录"]').click()
        return AddressListPage(self._driver)
    def goto_workbench(self):
        pass
    def goto_my(self):
        pass