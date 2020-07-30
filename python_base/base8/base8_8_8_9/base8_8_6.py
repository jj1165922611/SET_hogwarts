#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-10
# @Author     : Joey Jiang
# @File       : base8_8_6.py
# @SOftware   : Visual Studio Code
# @Description: python外部源文件处理（三）

'''
写一个简单的例子
'''

register=[]

def registy(func):
    register.append(func)
    return func

@registy
def f1():
    print("f1")
@registy
def f2():
    print("f2")
def f3():
    print("f3")
if __name__=="__main__":
    print("hello")
    print(f"register ->{register}")
    f1()
    f2()
    f3()