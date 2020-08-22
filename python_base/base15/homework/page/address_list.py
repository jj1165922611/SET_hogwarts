#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-08-22
# @Author     : Joey Jiang
# @File       : address_list.py
# @Software   : PyCharm
# @Descrtption: 企业微信自动化测试实战
from appium.webdriver.common.mobileby import MobileBy

from python_base.base15.homework.page.base import BasePage
from python_base.base15.homework.page.contact_detail_info import ContactDetailInfoPage
from python_base.base15.homework.page.department_search import DepartmentSearchPage
from python_base.base15.homework.page.invite_member import InviteMemberPage


class AddressListPage(BasePage):
    def search(self):
        pass
    def add_member(self):
        self.find(MobileBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员").instance(0));').click()
        return InviteMemberPage(self._driver)
    def detail_member(self,name):
        self.find(MobileBy.ANDROID_UIAUTOMATOR,
                  f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("{name}").instance(0));').click()
        return  ContactDetailInfoPage(self._driver)
    def search_department(self):
        self.find(MobileBy.ID,"com.tencent.wework:id/gw1").click()
        return DepartmentSearchPage(self._driver)

