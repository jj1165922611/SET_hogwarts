#!usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2020-09-07
# @Author    : Joey Jiang
# @File      : c009.py
# @Software  : PyCharm
# @Descrption: Python函数篇内置函数的学习使用

"""
list1=[1,2,3,4,5]，分别删除所有元素，清空列表
"""
# 方法1
list1=[1,2,3,4,5]
for i in list1[:]:
    list1.remove(i)
print(list1)
# 方法2
list2=[1,2,3,4,5]
for i in range(-len(list2),0):
    print(list2)
    list2.remove(list2[i])
    # list2.pop(i)
print(list2)