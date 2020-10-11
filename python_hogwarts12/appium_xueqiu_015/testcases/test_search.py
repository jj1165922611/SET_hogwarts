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
        self.app=App()
        name = "阿里巴巴"
        len = self.app.start().main().goto_market().goto_search().search(name).is_choose(name)
        assert len > 0