#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-08-22
# @Author     : Joey Jiang
# @File       : department_search.py
# @Software   : PyCharm
# @Descrtption: 企业微信自动化测试实战
from appium.webdriver.common.mobileby import MobileBy

from python_base.base15.homework.page.base import BasePage


class DepartmentSearchPage(BasePage):
    def search_member(self,name):
        self.find(MobileBy.XPATH,"//*[@text='搜索']").send_keys(name)
        return self.find(MobileBy.XPATH,"//*[@text='无搜索结果']").text
