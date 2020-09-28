#!usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2020-09-07
# @Author    : Joey Jiang
# @File      : c006.py
# @Software  : PyCharm
# @Descrption: Python运算符&amp;if条件语句

"""
t1=("aa",11)
t2=("bb",22)
list1=[("cc",33)]
转成字典{'aa': 11, 'bb': 22, 'cc': 33}
"""
# 方法1
t1=("aa",11)
t2=("bb",22)
list1=[("cc",33)]
my_tuple=(t1,t2,list1[0])
print(dict(my_tuple))
# 方法2
dict={}
dict[t1[0]]=t1[1]
dict[t2[0]]=t2[1]
dict[list1[0][0]]=list1[0][1]
print(dict)