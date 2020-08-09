#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-08-09
# @Author     : Joey Jiang
# @File       : test_contact.py
# @Software   : PyCharm
# @Description: 通讯录->设置所在部门

'''
如果没有则使用po思想，编写通讯录页面的测试用例，不可以有强制等待,driver需要封装到basepage中
比如进入通讯录->设置所在部门

提醒：
企业微信页面定位有很多坑。碰到这些坑使用xpath可能是更好的选择。
'''
from python_base.base11.base11_7_11_8.homework.page.contact import ContactPage


class TestContact:
    def setup(self):
        self.contact=ContactPage()
        self.contact.set_cookie()
    def teardown(self):
        self.contact.quit()
    def test_set_up_department(self):
        name='川建国15'
        department_list=['航母制造集团','开发一部']
        result=self.contact.select_member(name)
        if result==1:
            self.contact.set_up_department(department_list=department_list)
            assert self.contact.get_departments(name=name) == department_list
        else:
            print("此成员尚未添加")
            assert False