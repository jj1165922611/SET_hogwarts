#!/usr/bin/env python
# -*-coding: utf-8 -*-
# @Time       : 2020-04-27
# @Author     : Joey Jiang
# @File       : list_comprehension.py
# @Software   : Visual Studio Code
# @Description: 列表推导式

'''
使用列表推导式写下面这个算法题
给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。

* 示例 1：
输入：[-4,-1,0,3,10]
输出：[0,1,9,16,100]
* 示例 2：
输入：[-7,-3,2,3,11]
输出：[4,9,9,49,121]
* 提示：
1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A 已按非递减顺序排序。
'''
list_a = [-4, -1, 0, 3, 10]  # 定义一个列表list_a，赋值为[-4, -1, 0, 3, 10]
print([i**2 for i in set(list_a)])  # 将列表list_a转成集合，对集合中的值进行平方运算，将结果存入新的列表
# print(set([i**2 for i in list_a])) # 对列表list_a中的值进行平方运算并将结果存入新的列表，将新的列表转成集合
# print(set([i**2 for i in set(list_a)])) # 将列表list_a转成集合，对集合中的值进行平方运算，将结果存入新的列表，将新的列表转成集合
