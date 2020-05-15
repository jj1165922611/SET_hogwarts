#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-04
# @Author     : Joey Jiang
# @File       : base8_6.py
# @Software   : Visual Studio Code
# @Description: python第三方库

import requests

response=requests.get("https://www.baidu.com")

print(response.status_code)
print(response.encoding)
response.encoding="utf-8"
print(response.text)

print("*"*20)
response=requests.post("http://httpbin.org/post",data={"key":"value"})
print(response.text)