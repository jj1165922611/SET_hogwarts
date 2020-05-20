#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-20
# @Author     : Joey Jiang
# @File       : calc_1.py
# @Software   : PyCharm
# @Description: pytest测试实战（二）

class Calc:
    def add(self,a,b):
        return a+b
    def add1(self,data):
        return data[0]+data[1]
    def div(self,a,b):
        return a/b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b