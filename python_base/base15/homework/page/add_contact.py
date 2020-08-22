#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-08-22
# @Author     : Joey Jiang
# @File       : add_contact.py
# @Software   : PyCharm
# @Descrtption: 企业微信自动化测试实战
from appium.webdriver.common.mobileby import MobileBy

from python_base.base15.homework.page.base import BasePage


class AddContactPage(BasePage):
    def set_name(self,name):
        self.find(MobileBy.XPATH,"//*[@text='姓名　']/..//*[@text='必填']").send_keys(name)
        return self
    def set_gender(self,gender):
        self.find(MobileBy.XPATH, "//*[@text='性别']/..//*[@class='android.widget.RelativeLayout']").click()
        if gender=="男":
            self.find(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.find(MobileBy.XPATH, "//*[@text='女']").click()
        return self
    def set_phonenum(self,phonenum):
        self.find(MobileBy.XPATH, "//*[@text='手机　']/..//*[@text='手机号']").send_keys(phonenum)
        return self
    def click_save(self):
        self.find(MobileBy.XPATH,"//*[@text='保存']").click()
        from python_base.base15.homework.page.invite_member import InviteMemberPage
        return InviteMemberPage(self._driver)