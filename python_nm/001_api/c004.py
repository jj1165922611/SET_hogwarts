#!usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2020-09-07
# @Author    : Joey Jiang
# @File      : c004.py
# @Software  : PyCharm
# @Descrption: 常用数据类型字符串元组

"""
str1='python cainiao 666'
1、请找出第5个字符
2、请复制一份字符串，保存为str_two
3、请找出最中间的字符(长度为偶数)
4、第3题字符串长度不确定时
"""
str1='pytho'
print("第五个字符是",str1[4])
str_two=str1
print(str_two)
print(len(str1))
print("最中间的字符是：",str1[int(len(str1)/2)])