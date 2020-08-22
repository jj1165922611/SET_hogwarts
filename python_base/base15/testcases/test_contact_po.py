#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-08-19
# @Author     : Joey Jiang
# @File       : test_contact_po.py
# @Software   : PyCharm
# @Description: 企业微信移动app实战
from python_base.base15.page.app import App


class TestContactPO:
    def setup(self):
        self.app=App()

    def test_addcontact(self):
        self.app.main().goto_address().add_member().click_menualadd().set_name().set_gender().set_phonenum().click_save()