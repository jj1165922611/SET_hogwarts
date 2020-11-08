#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-10-25
# @Author     : Joey Jiang
# @File       : jenkins_api_001_2.py
# @Software   : PyCharm
# @Description: jenkins api接口

import requests

r=requests.get("http://JoeyJiang:1220jj@localhost:8888/job/iInterface_python/14/api/json")
print(r.text)