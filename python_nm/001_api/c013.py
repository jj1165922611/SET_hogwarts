#!usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2020-09-07
# @Author    : Joey Jiang
# @File      : c013.py
# @Software  : PyCharm
# @Descrption: Python函数篇函数参数类型学习使用

"""
1、编写一个函数，将用户输入的所有数字相乘，返回乘积模除20后的值
2、编写函数，检查传入列表的长度，如果大于2，那么仅仅保留前两位的内容，并将新内容返回
3、定义一个函数，传入一个字典和字符串，判断字符串是否为字典中的值。
如果字符串不在字典中，则添加到字典中，并返回新的字典
4、通过定义一个计算器函数，调用函数传入两个值和运算符，然后可以进行加减乘除
"""
def mul(*kwargs):
    result=1
    for i in kwargs:
        result *= i
    return result % 20
def change_list(list1: list):
    if len(list1)>2:
        return list1[:2]
def add_str(dict1:dict,str1:str):
    if str1 in dict1.values():
        return
    dict1["key"]=str1
def calc(a,b,ysf):
    return eval(f'{a},{ysf},{b}')

