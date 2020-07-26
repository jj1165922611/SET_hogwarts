#!/usr/bin/env python
# -*- coding -*-
# @Time       : 2020-07-26
# @Author     : Joey Jiang
# @File       : tips.py
# @Software   : PyCharm
# @Description: 其他tips

# 1、参数的类型提示
def excute_data(a:list,b):
    a.append(b)

# 2、方法返回值的类型提示
def return_data(a)->list:
    list=[]
    list.append(a)
    print(list)
    return list
print(return_data("a").pop())

# 3、三目运算
a=2
if a==1:
    print("a=1")
else:
    print("a!=1")

print("a=1")  if a==1 else print("a!=1")