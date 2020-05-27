#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-23
# @Author     : Joey Jiang
# @File       : main_error_1.py
# @Software   : PyCharm
# @Description: Page Object演练
from time import sleep
from selenium import webdriver
from python_base.base11.base11_7_11_8.add_member.page.add_member import AddMember

'''
企业微信首页PO封装
'''
class Main:
    def __init__(self):
        # PS：在main中get方法打开一个页面后，后面page就可以不用再使用get方法打开页面，而是直接在这个页面内进行跳转。
        option=webdriver.ChromeOptions()
        option.debugger_address="localhost:9222"
        self.driver=webdriver.Chrome(option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
    def goto_add_member(self):
        # 传统测试用例步骤
        # 1.进入首页点击添加成员
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # PS：加10秒等待，防止需要登录，这一步就不算到add_member需要的PO中了
        sleep(10)
        self.driver.find_element_by_css_selector('[class="index_service_cnt_item_title"]').click()
        # PS：此时需要return跳转的添加成员页面类
        return AddMember()
