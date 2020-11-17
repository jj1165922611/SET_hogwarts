#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020/11/8 0008 20:14
# @Author     : Joey Jiang
# @File       : test_add_member.py
# @Software   : PyCharm
# @Description: 添加成员测试用例

import pytest
from python_hogwarts_base2.base18_3.page.main_page import MainPage


class TestAddMember:
    def setup(self):
        self.main=MainPage()
    def teardown(self):
        self.main.quit()
    @pytest.mark.parametrize("name,account,phone",[("我是谁","123","123456789100")])
    def test_add_member(self,name,account,phone):
        self.main.go_to_contact().go_to_add_member().add_member(name,account,phone)
