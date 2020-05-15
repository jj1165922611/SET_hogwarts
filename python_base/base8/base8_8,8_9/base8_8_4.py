#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-10
# @Author     : Joey Jiang
# @File       : base8_8_4.py
# @SOftware   : Visual Studio Code
# @Description: python外部源文件处理（三）

'''
写一个简单的例子
'''
def foo():
    print("this is a func ,foo")

def log(func):
    print("{} is running".format(func))
    func()

log(foo)