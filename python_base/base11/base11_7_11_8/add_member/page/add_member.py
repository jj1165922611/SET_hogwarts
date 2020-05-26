#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-26
# @Author     : Joey Jiang
# @File       : add_member.py
# @Software   : PyCharm
# @Description: PageObject演练（一）
from python_base.base11.base11_7_11_8.add_member.page.contact import Contact


class AddMember:
    def add_member(self):
        # 点击添加成员
        # 输入姓名
        # 输入账号
        # 输入手机号
        # 点击保存
        # 跳转到联系人列表
        def add_member(self):
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
            self.driver.find_element(By.ID, "username").send_keys("哈哈")
            self.driver.find_element(By.ID, "memberAdd_acctid").send_keys("123456")
            self.driver.find_element(By.ID, "memberAdd_phone").send_keys("17123456789")
            self.driver.find_elements_by_css_selector("qui_btn ww_btn js_btn_save").click()
            return Contact
        return Contact()