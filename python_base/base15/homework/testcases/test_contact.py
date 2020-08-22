#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-08-22
# @Author     : Joey Jiang
# @File       : test_contact.py
# @Software   : PyCharm
# @Descrtption: 企业微信自动化测试实战
import pytest
import yaml

from python_base.base15.homework.page.app import App


class TestContact():
    def setup(self):
        self.main=App().start().main()
    @pytest.mark.parametrize("name,gender,phonenum",yaml.safe_load(open("../data/add_contact_data.yaml",'rb')))
    def test_add(self,name,gender,phonenum):
        result=self.main.goto_contact().add_member().add_contact().set_name(name).set_gender(gender).set_phonenum(phonenum).click_save()
        assert result.get_toast()=='添加成功'
    def test_del(self):
        name='川建国31'
        result=self.main.goto_contact().detail_member(name).edit_info().del_contact().del_member()
        assert result.search_department().search_member(name)=='无搜索结果'

