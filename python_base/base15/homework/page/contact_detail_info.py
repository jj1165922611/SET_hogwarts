#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-08-22
# @Author     : Joey Jiang
# @File       : contact_detail_info.py
# @Software   : PyCharm
# @Descrtption: 企业微信自动化测试实战
from appium.webdriver.common.mobileby import MobileBy

from python_base.base15.homework.page.base import BasePage
from python_base.base15.homework.page.set_detail import SetDetailPage

class ContactDetailInfoPage(BasePage):
    def edit_info(self):
        self.find(MobileBy.ID, "com.tencent.wework:id/gvr").click()
        return SetDetailPage(self._driver)