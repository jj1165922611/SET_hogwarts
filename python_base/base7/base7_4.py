#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-04-21
# @Author     : Joey Jiang
# @File       : base7_4.py
# @Software   : Visual Studio Code
# @Description: Python函数

# 必须参数


def method(a):
    print(a)
    return a+2


print(method(1))

# 默认参数


def fun(a=2):
    print(a)


print(fun())

# 默认参数只会执行一次，这条规则在默认值为可变对象时很重要


def para(a, b=[]):
    b.append(a)
    return b


print(para(1))
print(para(2))

# 关键字参数


def keypara(a, b):
    print(a)
    print(b)


print(keypara(b="bbb", a="aaa"))
print(keypara("aaaa", b="bbbb"))
# print(keypara(b="bbbb","aaaa")) 关键字参数必须在位置参数的后面

# 字典参数


def dic(**a):
    print(a.keys())
    print(a.values())


print(dic(aa=1))

# 元组参数


def tuple_(*a):
    print(a[0])


print(tuple_(11321, 2, 3, 4))

# 特殊参数


def only(*, a):
    print(a)


print(only(a=1))

# 解包
list_a = [3, 6]
keypara(*list_a)
dic = {"b": 1, "a": 2}
keypara(**dic)

# Lambda表达式


def y(x, y, z): return x+y+z


print(y(2, 3, 4))
