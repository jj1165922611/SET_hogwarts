#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020/11/21 8:22
# @Author     : Joey Jiang
# @File       : addresslist_page.py
# @Software   : PyCharm
# @Description: 通讯录页面
from python_hogwarts_base2.base24_6.page.basepage import BasePage
from python_hogwarts_base2.base24_6.page.member_invite_page import MemberInvitePage


class AddresslistPage(BasePage):
    def add_member(self):
        return MemberInvitePage()
