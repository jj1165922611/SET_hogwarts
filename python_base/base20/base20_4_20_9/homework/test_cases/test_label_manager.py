#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-06-14
# @Author     : Joey Jiang
# @File       : test_label_manager.py
# @Software   : PyCharm
# @Description: 企业微信标签管理接口(Api封装)
import json

import pytest
from hamcrest import *
from jsonpath import jsonpath
from jsonschema import validate

from python_base.base20.base20_4_20_9.homework.base_api.label_manager import LabelManager


class TestLabelManager:
    _create_data=[{"tagname":"Testing","tagid":1},
                  {"tagname":"Testing2","tagid":2},
                  {"tagname":"Testing3","tagid":3}]
    def setup_class(self):
        self.label_manager=LabelManager()
        self.token = self.label_manager.get_token(
            "G:/python/SET_hogwarts/python_base/base20/base20_4_20_9/homework/base_api/config.yml")

    @classmethod
    def teardown_class(cls):
        label_manager=LabelManager()
        label_manager.get_token("G:/python/SET_hogwarts/python_base/base20/base20_4_20_9/homework/base_api/config.yml")
        label_manager.delete_label(1)
        label_manager.delete_label(2)
        label_manager.delete_label(3)

    @pytest.mark.parametrize("testdata",_create_data)
    def test_create_label(self,testdata):
        r=self.label_manager.create_label(testdata)
        print(r.json())
        # assert r.json()['errcode']==0
        # assert jsonpath(r.json(), '$.errcode')[0] == 0
        schema=json.load(open("create_label_schema.json"))
        validate(r.json(),schema)
        assert_that(jsonpath(r.json(), '$.errcode')[0], equal_to(0),reason="响应失败")


    def test_update_label_name(self):
        """
        *更新标签名字
        """
        testdata={"tagid":1 ,"tagname":"Testing1",}
        r= self.label_manager.update_label_name(testdata)
        print(r.json())
        # assert r.json()['errcode'] == 0
        # assert jsonpath(r.json(), '$.errcode')[0] == 0
        schema = json.load(open("update_label_name_schema.json"))
        validate(r.json(), schema)
        assert_that(jsonpath(r.json(), '$.errcode')[0], equal_to(0), reason="响应失败")

    def test_delete_label(self):
        """
        *删除标签
        """
        tagid=3
        r=self.label_manager.delete_label(tagid)
        print(r.json())
        # assert r.json()['errcode'] == 0
        # assert jsonpath(r.json(), '$.errcode')[0] == 0
        schema = json.load(open("delete_label_schema.json"))
        validate(r.json(), schema)
        assert_that(jsonpath(r.json(), '$.errcode')[0], equal_to(0), reason="响应失败")

    def test_get_label_member(self):
        """
        *获取标签成员
        """
        tagid=1
        r=self.label_manager.get_label_member(tagid)
        print(r.json())
        # assert r.json()['errcode'] == 0
        # assert jsonpath(r.json(),'$.errcode')[0] == 0
        # schema = json.load(open("get_label_member_schema.json"))
        # validate(r.json(), schema)
        assert_that(jsonpath(r.json(), '$.errcode')[0], equal_to(0), reason="响应失败")

    def test_add_label_member(self):
        """
        *增加标签成员
        """
        testdata = {
           "tagid": 1,
           "userlist":[ "cjg1","cjg2","cjg3"],
        }
        r=self.label_manager.add_label_member(testdata)
        print(r.json())
        # assert r.json()['errcode'] == 0
        # assert jsonpath(r.json(), '$.errcode')[0] == 0
        # schema = json.load(open("add_label_member_schema.json"))
        # validate(r.json(), schema)
        assert_that(jsonpath(r.json(), '$.errcode')[0], equal_to(0), reason="响应失败")

    def test_delete_label_member(self):
        """
        *删除标签成员
        """
        testdata={
            "tagid": 1,
            "userlist": ["cjg3"]
        }
        r=self.label_manager.delete_label_member(testdata)
        print(r.json())
        # assert r.json()['errcode'] == 0
        # assert jsonpath(r.json(), '$.errcode')[0] == 0
        # schema = json.load(open("delete_label_member_schema.json"))
        # validate(r.json(), schema)
        assert_that(jsonpath(r.json(), '$.errcode')[0], equal_to(0), reason="响应失败")

    def test_getlist_label(self):
        """
        *获取标签列表
        """
        r=self.label_manager.getlist_label()
        print(r.json())
        # assert r.json()['errcode'] == 0
        # assert jsonpath(r.json(), '$.errcode')[0] == 0
        schema = json.load(open("getlist_label_schema.json"))
        validate(r.json(), schema)
        assert_that(jsonpath(r.json(), '$.errcode')[0], equal_to(0), reason="响应失败")