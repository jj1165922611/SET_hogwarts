#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-06-14
# @Author     : Joey Jiang
# @File       : base_api.py
# @Software   : PyCharm
# @Description: 企业微信标签管理接口(Api封装)
import requests
import yaml


class BaseApi:
    def send_api(self,req):
        """
        *封装requests
        :param seq: 字典格式的参数列表
        """
        r=requests.request(**req)
        return r
    def get_yaml(self,filename):
        with open(filename,"rb") as f:
            data=yaml.safe_load(f)
        return data