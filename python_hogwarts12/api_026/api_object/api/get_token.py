#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-10-17
# @Author     : Joey Jiang
# @File       : get_token.py
# @Software   : PyCharm
# @Description: apiobject模式应用
import requests

from python_hogwarts12.api_026.api_object.api.base_api import BaseApi


class GetToken(BaseApi):

    def get_token(self, data: dict):
        return self.requests(url=data["url"],method=data["method"],params=data["params"])
