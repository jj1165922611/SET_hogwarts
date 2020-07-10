#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-07-09
# @Author     : Joey Jiang
# @File       : test_base18_2.py
# @Software   : PyCharm
# @Description: 雪球app抓包与mock实战
import json

def response(flow):
    if "quote.json" in flow.request.pretty_url:
       res=json.loads(flow.response.content)
       res["data"]["items"][0]["quote"]["name"]="hogwarts22222!!"
       flow.response.text=json.dumps(res)