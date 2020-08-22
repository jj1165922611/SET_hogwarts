#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-08-22
# @Author     : Joey Jiang
# @File       : invite_member.py
# @Software   : PyCharm
# @Descrtption: 企业微信自动化测试实战
from appium.webdriver.common.mobileby import MobileBy

from python_base.base15.homework.page.add_contact import AddContactPage
from python_base.base15.homework.page.base import BasePage


class InviteMemberPage(BasePage):
    def add_contact(self):
        self.find(MobileBy.ID,"com.tencent.wework:id/h3o").click()
        return AddContactPage(self._driver)
    def get_toast(self):
        element=self.find(MobileBy.XPATH,"//*[@text='添加成功']")
        return element.text