#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-07-29
# @Author     : Joey Jiang
# @File       : base8_8_7.py
# @SOftware   : Visual Studio Code
# @Description: python外部源文件处理（三）

'''
闭包函数
'''

def outer(foo):
    def inner(a,b):
        return a+b
    return inner

@outer
def foo():
    print("foo")

print(foo(1, 3))
print(foo(4, 5))