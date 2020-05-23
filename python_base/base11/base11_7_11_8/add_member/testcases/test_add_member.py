#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-23
# @Author     : Joey Jiang
# @File       : test_add_member.py
# @Software   : PyCharm
# @Description: Page Object演练

from python_base.base11.base11_7_11_8.add_member.page.main import Main

class TestAddMember:
    def test_add_member(self):
        main=Main()
        assert "哈哈" in main.goto_add_member().add_member().add_member().get_member()