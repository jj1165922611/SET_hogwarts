#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-10-10
# @Author     : Joey Jiang
# @File       : search.py
# @Software   : PyCharm
# @Description: 打造自己的测试框架
from appium.webdriver.common.mobileby import MobileBy

from python_hogwarts12.appium_xueqiu_015.page.basepage import BasePage


class Search(BasePage):
    def search(self,name):
        self._params["name"]=name
        self.steps("../page/search.yaml")
        return self
    def is_choose(self,name):
        self._params["name"] = name
        return self.steps("../page/search.yaml")

