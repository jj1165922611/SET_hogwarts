#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-17
# @Author     : Joey Jiang
# @File       : test_9_6_8.py
# @Software   : Pycharm
# @Description: 测试报告美化与定制

'''
通过allure.attach("xxxx",attachment_type,exntension)加入纯文本信息
'''
import pytest
import allure

def test_attach_text():
    allure.attach("这是一个纯文本",attachment_type=allure.attachment_type.TEXT)
