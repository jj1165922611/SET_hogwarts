#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-26
# @Author     : Joey Jiang
# @File       : add_member_error_1.py
# @Software   : PyCharm
# @Description: PageObject演练（一）
import os

from selenium.webdriver.common.by import By
from selenium import webdriver
from python_base.base11.base11_7_11_8.add_member.page.contact import Contact
from python_base.base11.base11_7_11_8.add_member.uitl.util import Util


class AddMember:
    def __init__(self):
        self.driver=webdriver.Chrome()
    def add_member(self):
        filename=os.path.dirname(__file__)
        member_info=Util.get_yaml(filename)
        index=0
        # 2.在添加成员页面输入姓名
        self.driver.find_element(By.ID, "username").send_keys(member_info[index][0])
        # 3.输入账号
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys(member_info[index][1])
        # 4.输入手机号
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys(member_info[index][2])
        # 5.点击保存
        self.driver.find_elements_by_css_selector("qui_btn ww_btn js_btn_save").click()
        # PS：此时需要return跳转的联系人列表页面
        return Contact()