#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-10-10
# @Author     : Joey Jiang
# @File       : test_base.py
# @Software   : PyCharm
# @Description: 通用测试用例封装
from python_hogwarts12.ui_framework_014.page.app import App


class TestBase:
    app =None
    def setup(self):
        self.app= App()