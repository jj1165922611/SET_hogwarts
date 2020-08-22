#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-08-19
# @Author     : Joey Jiang
# @File       : main.py
# @Software   : PyCharm
# @Description: 企业微信移动app实战
from python_base.base15.page.address_list import AddressListPage


class Main:
    def goto_message(self):
        pass
    def goto_address(self):
        '''
        进入通讯录
        :return:
        '''
        return AddressListPage()
    def goto_workbench(self):
        pass
    def goto_profile(self):
        pass