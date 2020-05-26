#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-23
# @Author     : Joey Jiang
# @File       : index_page.py
# @Software   : PyCharm
# @Description: Page Object演练
from python_base.base11.base11_7_11_8.login_register.page.login_page import LoginPage
from python_base.base11.base11_7_11_8.login_register.page.register_page import RegisterPage
class IndexPage():

    def goto_register(self):
        # 点击行为，点击之后跳转到注册页面
        return RegisterPage()
    def goto_login(self):
        # 点击行为，点击之后跳转到登录页面
        return LoginPage()
    def goto_download(self):
        pass