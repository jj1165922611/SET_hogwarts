#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-10-10
# @Author     : Joey Jiang
# @File       : test_search.py
# @Software   : PyCharm
# @Description: 打造自己的测试框架
from python_hogwarts12.appium_xueqiu_015.page.app import App


class TestSearch:
    def test_search(self):
        text=App().start().main().goto_market().goto_search().search().get_toast()
        assert text=="已关注"