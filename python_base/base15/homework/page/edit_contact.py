#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-08-22
# @Author     : Joey Jiang
# @File       : edit_contact.py
# @Software   : PyCharm
# @Descrtption: 企业微信自动化测试实战
from appium.webdriver.common.mobileby import MobileBy
from python_base.base15.homework.page.base import BasePage


class EditContactPage(BasePage):
    def del_member(self):
        from python_base.base15.homework.page.address_list import AddressListPage
        self.find(MobileBy.ANDROID_UIAUTOMATOR,
                  'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("删除成员").instance(0));').click()
        self.find(MobileBy.XPATH,"//*[@text='确定']").click()
        return AddressListPage(self._driver)