#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-10-06
# @Author     : Joey Jiang
# @File       : main.py
# @Software   : PyCharm
# @Description: pageobject改造
from appium.webdriver.common.mobileby import MobileBy

from python_hogwarts12.ui_framework_014.page.basepage import BasePage


class Main(BasePage):
    def goto_search(self):
        self.steps("../page/main.yaml")
        return self
