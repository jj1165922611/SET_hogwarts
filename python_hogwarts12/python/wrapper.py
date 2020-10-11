#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2020-10-10
# @Author     : Joey Jiang
# @File       : wrapper.py
# @Software   : PyCharm
# @Description: 打造自己的测试框架

'''
装饰器
1、不使用装饰器，多个方法中出现很多重复代码
2、仅使用装饰器，不使用语法糖，调用时不够优雅，但是已经可以解决重复代码的问题
'''
from functools import wraps


def tmp0():
    print("hello")
    print("tmp0")
    print("goodbye")


def tmp1():
    print("hello")
    print("tmp1")
    print("goodbye")


def wrapper0():
    tmp0()
    tmp1()


wrapper0()


def tmp():
    print("tmp")


def tmp1():
    print("tmp1")


def wrapper1():
    tmp()
    tmp1()


wrapper1()


def outer1(tmp):
    def inner(*args, **kwargs):
        print("hello")
        tmp(*args, **kwargs)
        print("goodbye")

    return inner


def wrapper2():
    outer1(tmp)()
    outer1(tmp)()


wrapper2()


@outer1
def tmp3():
    print("tmp3")


def wrapper3():
    tmp3()


wrapper3()


def outer2(tmp):
    @wraps(tmp)
    def inner(*args, **kwargs):
        print("hello")
        print(args)
        print(kwargs)
        tmp(*args, **kwargs)
        print("goodbye")
    return inner


@outer2
def tmp4(a:int, b, c, d)->int:
    print("tmp4")

def wrapper4(a, b, c, d):
    tmp4(a, b, c, d)
    print(tmp4.__annotations__)

wrapper4(1, 2, 3, d=10)

def outer3(a):
    def outer2(tmp):
        def inner(*args,**kwargs):
            print("hello")
            print(a)
            tmp()
            print("goodbye")
        return inner
    return outer2
@outer3("aaaaaa")
def tmp5():
    print("tmp5")
tmp5()