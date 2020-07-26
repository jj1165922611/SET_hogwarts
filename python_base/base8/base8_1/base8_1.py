#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-07-26
# @Author     : Joey Jiang
# @File       : base8_1.py
# @Software   : PyCharm
# @Description: python脚本编写实战（一）


# 1、冒泡排序
def bubble_sort():
    list=[1,3,5,2,7,6]
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    print(list)
bubble_sort()

# 2、字典解包
def foo(a,b):
    print(a)
    print(b)

dict1=dict(a=1,b=2)
dict2=dict(a=1,b=2,c=3)
foo(**dict1)
foo(**dict2) # 执行会报错