#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-10-10
# @Author     : Joey Jiang
# @File       : test_search.py
# @Software   : PyCharm
# @Description: 打造自己的测试框架
import pytest
import yaml

from python_hogwarts12.appium_xueqiu_015.page.app import App


class TestSearch:
    @pytest.mark.parametrize("name",yaml.safe_load(open("test_search.yaml","rb")))
    def test_search(self,name):
        self.app=App()
        len = self.app.start().main().goto_market().goto_search().search(name).is_choose(name)
        assert len > 0