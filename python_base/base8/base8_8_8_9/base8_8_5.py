#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-10
# @Author     : Joey Jiang
# @File       : base8_8_5.py
# @SOftware   : Visual Studio Code
# @Description: python外部源文件处理（三）

'''
使用装饰器例子
'''

def log(func):
    print("{} is running".format(func))
    return func # 装饰器必须有返回值
@log
def foo():
    print("this is a func ,foo")
foo()