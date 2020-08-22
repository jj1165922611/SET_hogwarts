#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-08-19
# @Author     : Joey Jiang
# @File       : contact_add_error.py
# @Software   : PyCharm
# @Description: 企业微信移动app实战
'''
问题是InviteMemberPage被全局导入，导致了InviteMemberPage被循环导入，报错
'''
from python_base.base15.page.invite_member import InviteMemberPage


class ContactAddPage:
    def set_name(self):
        return self
    def set_gender(self):
        return self
    def set_phonenum(self):
        return self
    def click_save(self):
        return InviteMemberPage()