#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-06-14
# @Author     : Joey Jiang
# @File       : we_work.py
# @Software   : PyCharm
# @Description: 企业微信标签管理接口(Api封装)
import yaml

from python_base.base20.base20_4_20_9.homework.base_api.base_api import BaseApi


class WeWork(BaseApi):
    def get_token(self,filename):
        data=self.get_yaml(filename)["access_token"]
        seq={
            "url" : data["url"],
            "method" : data["method"],
            "params" : {"corpid": data["corpid"],"corpsecret": data["corpsecret"]},
        }
        we_work=WeWork()
        self.token = we_work.send_api(seq).json()[data["name"]]
        return self.token
