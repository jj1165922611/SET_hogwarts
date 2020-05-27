#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-26
# @Author     : Joey Jiang
# @File       : add_member.py
# @Software   : PyCharm
# @Description: PageObject演练（一）
import os

from selenium.webdriver.common.by import By
from selenium import webdriver
from python_base.base11.base11_7_11_8.add_member.page.contact import Contact
from python_base.base11.base11_7_11_8.add_member.uitl.util import Util


class AddMember:
    _test="test"

    def __init__(self):
        option=webdriver.ChromeOptions()
        option.debugger_address="localhost:9222"
        self.driver=webdriver.Chrome(chrome_options=option)
        self.driver.implicitly_wait(3)
    def add_member(self):
        filename="G:/python/SET_hogwarts/python_base/base11/base11_7_11_8/add_member/conf/member_info.yml"
        member_info=Util.get_yaml(filename)
        index=27
        # 2.在添加成员页面输入姓名
        self.driver.find_element(By.ID, "username").send_keys(member_info[index][0])
        # 3.输入账号
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys(member_info[index][1])
        # 4.输入手机号
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys(member_info[index][2])
        # 5.点击保存
        self.driver.find_element(By.CSS_SELECTOR,'.js_btn_save').click()
        # PS：此时需要return跳转的联系人列表页面
        return Contact()

    def add_member_fail(self):
        filename="G:/python/SET_hogwarts/python_base/base11/base11_7_11_8/add_member/conf/member_info.yml"
        member_info=Util.get_yaml(filename)
        index=1
        # 2.在添加成员页面输入姓名
        self.driver.find_element(By.ID, "username").send_keys("川建国")
        # 3.输入账号
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys(member_info[index][1])
        # 4.输入手机号
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys(member_info[index][2])
        # 5.点击保存
        self.driver.find_element(By.CSS_SELECTOR,'.js_btn_save').click()
        # PS：此时需要return跳转的联系人列表页面
        return Contact()