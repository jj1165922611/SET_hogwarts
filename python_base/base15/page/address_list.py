#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-08-19
# @Author     : Joey Jiang
# @File       : address_list.py
# @Software   : PyCharm
# @Description: 企业微信移动app实战
from python_base.base15.page.invite_member import InviteMemberPage


class AddressListPage:
    def add_member(self):
        return InviteMemberPage()