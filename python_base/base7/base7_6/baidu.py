#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-07-23
# @Author     : Joey Jiang
# @File       : baidu11.py
# @Software   : PyCharm
# @Description: 自定义模块

def add(a,b):
    return a+b

class Baidu:
    def sub(self,a,b):
        return a-b


print(add(1, 3))
print(Baidu().sub(3, 4))