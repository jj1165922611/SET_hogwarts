#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-08-22
# @Author     : Joey Jiang
# @File       : set_detail.py
# @Software   : PyCharm
# @Descrtption: 企业微信自动化测试实战
from appium.webdriver.common.mobileby import MobileBy

from python_base.base15.homework.page.base import BasePage
from python_base.base15.homework.page.edit_contact import EditContactPage


class SetDetailPage(BasePage):
    def del_contact(self):
        self.find(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        return EditContactPage(self._driver)