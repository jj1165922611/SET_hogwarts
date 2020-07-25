#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-07-23
# @Author     : Joey Jiang
# @File       : base7-6.py
# @Software   : PyCharm
# @Description: python模块

import sys
import time

# 1、系统模块
print(sys.argv)
time.sleep(3)
print("等待结束")

# 2、第三方模块
import  requests
r=requests.get("https://www.baidu.com/")
print(r.status_code)