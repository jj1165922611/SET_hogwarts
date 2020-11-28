#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020/11/21 8:25
# @Author     : Joey Jiang
# @File       : test_addcontact.py
# @Software   : PyCharm
# @Description: 添加成员功能测试
from python_hogwarts_base2.base24_6.page.app import App


class TestAddContact:
    def setup(self):
        self.app=App()
        self.main=self.app.start().goto_main()
    def teardown(self):
        self.app.stop()
    def test_addcontact(self):
        self.main.goto_addresslist().add_member().addcontact_manual()