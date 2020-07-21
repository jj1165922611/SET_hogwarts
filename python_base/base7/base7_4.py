#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-04-21
# @Author     : Joey Jiang
# @File       : base7_4.py
# @Software   : Visual Studio Code
# @Description: Python函数

# 1、定义函数
def method1():
    print("hello world")
print(method1())

# 2、必须参数
def method2(a):
    print(a)
print(method2(2))

# 3.1、默认参数
def fun(a=2):
    print(a)
print(fun())

# 3.2默认参数只会执行一次，这条规则在默认值为可变对象时很重要
def para(a, b=[]):
    b.append(a)
    return b
print(para(1))
print(para(2))

# 4.1、关键字参数
def keypara(a, b):
    print(a)
    print(b)
print(keypara(b="bbb", a="aaa"))
print(keypara("aaaa", b="bbbb"))
# print(keypara(b="bbbb","aaaa")) 关键字参数必须在位置参数的后面
# 4.2、字典参数
def dic(**aa):
    print(aa.keys())
    print(aa.values())
print(dic(b=2,c=3,d=4))
# 4.3、元组参数
print("----4.3元组参数-----")
def tuple_(*a):
    print(a[0])
    print(a[1])
    print(a[2])
print(tuple_(11321, 2, 3, 4))
# 4.4、特殊参数
def only(*, a):
    print(a)
print(only(a=1))
# 4.5、解包元组
print("-----4.5解包元组------")
list_a = (3, 6)
keypara(*list_a)
# 4.6、解包字典
dic = {"b": 1, "a": 2}
keypara(**dic)
# 5、Lambda表达式
y =lambda x, y, z:  x + y + z
print(y(2, 3, 4))

