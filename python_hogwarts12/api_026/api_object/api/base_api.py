#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-10-17
# @Author     : Joey Jiang
# @File       : base_api.py
# @Software   : PyCharm
# @Description: apiobject模式应用
import requests
from string import Template

import yaml


class BaseApi:

    def requests(self, data: dict):
        r = requests.request(**data)
        return r
    def template(self,file,data):
        with open(file) as f:
            re=Template(f.read()).substitute(**data)
        return yaml.safe_load(re)
