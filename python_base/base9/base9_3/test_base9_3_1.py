#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-10
# @Author     : Joey Jiang
# @File       : test_base9_3_1.py
# @Software   : Visual Studio Code
# @Description: pytest测试框架

'''
测试文件test_*开头，测试函数以test_*开头
'''
def func(x):
    x=x+1
    print(f"x={x}")
    return x

def test_func():
    assert func(1)==2
    print("31132")
    assert func(2)==3
    