#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-23
# @Author     : Joey Jiang
# @File       : test_add_member.py
# @Software   : PyCharm
# @Description: Page Object演练

from python_base.base11.base11_7_11_8.add_member.page.main import Main

class TestAddMember:
    def setup(self):
        self.main=Main()
    def test_add_member(self):
        # 7.添加断言，判断值是否在列表中。如在表示用例通过，不如在fail
        assert "川建国7" in self.main.goto_add_member().add_member().get_member()

    def test_add_member_fail(self):
        assert "川建国" not in self.main.goto_add_member().add_member_fail().get_member()
        '''
        添加成员的传统的测试用例步骤（不使用PO思想）：
        1.进入首页点击添加成员
        2.在添加成员页面输入姓名
        3.输入账号
        4.输入手机号
        5.点击保存
        6.获取成员列表的值
        7.添加断言，判断值是否在列表中。如在表示用例通过，不在fail
        
        使用PO封装思想：
        1.在首页点击添加成员   “Main的goto_add_member接口”
        2.在添加成员页面输入姓名、账号、手机号，点击保存   “AddMember的add_member接口”
        3.获取成员列表的值   “Contact的get_member接口”
        4.在测试用例方法中添加断言   ”TestAddMember的test_add_member测试用例“
        
        按照编写测试用例顺序实现PO封装：   
        1.新建Mian、AddMember、Contact的类，接口方法可以空置，只写return
        2.编写TestAddMember类的test_add_member测试用例
        3.实现PO类的方法
        4.调试
        '''
