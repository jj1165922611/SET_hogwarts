#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-07-26
# @Author     : Joey Jiang
# @File       : param.py
# @Software   : PyCharm
# @Description: python脚本编写实战（一）作业

# 1、关键字参数
def param1(a):
    print(a)
dict=dict(a=[1,23,4])
param1(**dict)
# 2、默认参数
def param2(a="我是a"):
    print(a)
param2()