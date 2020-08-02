#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-17
# @Author     : Joey Jiang
# @File       : test_9_6_10.py
# @Software   : Pycharm
# @Description: 测试报告美化与定制

'''
通过allure.attach.flie(source,name,attachment_type,extension)加入图片
'''
import pytest
import allure

def test_attach_photo():
    allure.attach.file("./a.png","图片",attachment_type=allure.attachment_type.PNG)

