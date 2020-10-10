#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-10-10
# @Author     : Joey Jiang
# @File       : market.py
# @Software   : PyCharm
# @Description: 打造自己的测试框架
from appium.webdriver.common.mobileby import MobileBy

from python_hogwarts12.appium_xueqiu_015.page.basepage import BasePage
from python_hogwarts12.appium_xueqiu_015.page.search import Search


class Market(BasePage):
    def goto_search(self):
        self.find(MobileBy.ID,"com.xueqiu.android:id/action_search").click()
        return Search(self._driver)