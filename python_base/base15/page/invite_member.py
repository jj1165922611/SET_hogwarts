#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-08-19
# @Author     : Joey Jiang
# @File       : invite_member.py
# @Software   : PyCharm
# @Description: 企业微信移动app实战
from python_base.base15.page.contact_add import ContactAddPage


class InviteMemberPage:
    def click_menualadd(self):
        return ContactAddPage()