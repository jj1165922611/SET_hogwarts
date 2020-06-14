#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-06-14
# @Author     : Joey Jiang
# @File       : label_manager.py
# @Software   : PyCharm
# @Description: 企业微信标签管理接口(Api封装)
from python_base.base20.base20_4_20_9.homework.base_api.we_work import WeWork


class LabelManager(WeWork):

    def __init__(self):
        self._filename="G:/python/SET_hogwarts/python_base/base20/base20_4_20_9/homework/base_api/config.yml"
        self._data=self.get_yaml(self._filename)
        self.token = self.get_token(self._filename)

    def create_label(self,testdata=None):
        data=self._data["create_label"]
        req={
            "url": data["url"],
            "method":data["method"],
            "params":{"access_token":self.token},
            "json": testdata
        }
        return self.send_api(req)

    def update_label_name(self,testdata=None):
        data = self._data["update_label_name"]
        req = {
            "url": data["url"],
            "method": data["method"],
            "params": {"access_token": self.token},
            "json": testdata,
        }
        return self.send_api(req)

    def delete_label(self,tagid=None):
        data = self._data["delete_label"]
        req = {
            "url": data["url"],
            "method": data["method"],
            "params": {"access_token": self.token,"tagid":tagid},
        }
        return self.send_api(req)

    def get_label_member(self,tagid=None):
        data = self._data["get_label_member"]
        req = {
            "url": data["url"],
            "method": data["method"],
            "params": {"access_token": self.token,"tagid":tagid},
        }
        return self.send_api(req)

    def add_label_member(self,testdata=None):
        data = self._data["add_label_member"]
        req = {
            "url": data["url"],
            "method": data["method"],
            "params": {"access_token": self.token},
            "json": testdata
        }
        return self.send_api(req)

    def delete_label_member(self,testdata=None):
        data = self._data["delete_label_member"]
        req = {
            "url": data["url"],
            "method": data["method"],
            "params": {"access_token": self.token},
            "json": testdata
        }
        return self.send_api(req)

    def getlist_label(self):
        data = self._data["getlist_label"]
        req = {
            "url": data["url"],
            "method": data["method"],
            "params": {"access_token": self.token},
        }
        return self.send_api(req)
