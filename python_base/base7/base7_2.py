#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-07-10
# @Author     : Joey Jiang
# @File       : base7_2.py
# @Software   : PyCharm
# @Description: python基本数据类型与操作

# 1、变量
a = 1
b = 2
print(a)
print(b)
c, d = 3, 4
print(c)
print(d)

# 2、数字
int_aa = 1
float_bb = 2.0
complex_cc = 2j
print(type(int_aa))
print(type(float_bb))
print(type(complex_cc))

# 3、字符串
aaa = "String@%$(*$ewqe122"
print(aaa)
bbb = "hello"
ccc = "world"
print(bbb + ccc)
print("bbb" "ccc")
print(f"aaaa{aaa}")
ddd = "xdsad{x}{y}"
print(ddd.format(x=1, y="das"))
# 列表
list_a = [1, 3, 4, "a", "c"]
print(list_a[0])
print(list_a[1])
print(list_a[2])
print(list_a[3])
print(list_a[4])
print(list_a[-1])
print(list_a[0:3])
