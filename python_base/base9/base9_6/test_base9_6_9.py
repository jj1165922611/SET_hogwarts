#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-17
# @Author     : Joey Jiang
# @File       : test_9_6_9.py
# @Software   : Pycharm
# @Description: 测试报告美化与定制

import pytest
import allure

def test_attach_text():
    allure.attach("这是一个纯文本",attachment_type=allure.attachment_type.TEXT)

def test_attach_html():
    allure.attach("<html>哈哈</html><body>我是谁</body>","一个网页",attachment_type=allure.attachment_type.HTML)
