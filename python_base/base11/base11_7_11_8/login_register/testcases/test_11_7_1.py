#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-23
# @Author     : Joey Jiang
# @File       : test_11_7_1.py
# @Software   : PyCharm
# @Description: Page Object演练
from python_base.base11.base11_7_11_8.login_register.page.index_page import IndexPage

class TestRegister:
    def test_login_register(self):
        index=IndexPage()
        index.goto_login()