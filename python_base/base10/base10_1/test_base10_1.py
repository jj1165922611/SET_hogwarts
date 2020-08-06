#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-23
# @Author     : Joey Jiang
# @File       : test_base10_1.py
# @SOftware   : PyCharm
# @Description: selenium安装

'''
selenium在python中如何使用
'''
from selenium import webdriver
def test_baidu():
    driver=webdriver.Chrome()
    driver.get("https://www.baidu.com")
    driver.quit()
