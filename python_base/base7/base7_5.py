#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-04-21
# @Author     : Joey Jiang
# @File       : base7_5.py
# @Software   : Visual Studio Code
# @Description: Python常用数据结构

# 1.1、列表
'''
    在列表末尾添加一个元素：list.append(x)
	在给定的位置插入一个元素：list.insert(i, x)
	移除列表中第一个值为x的元素：list.remove(x)
	删除列表中给定位置的元素并返回：list.pop(x)
	对列表中元素进行排序：list.sort()
	反转列表中元素：list.reverse()
'''
list_test=[1]
list_test.append(2)
print(list_test)
list_test.insert(0,1)
print(list_test)
list_test.append(3)
list_test.append(3)
list_test.remove(3)
print(list_test)
list_test.pop()
print(list_test)
list_test.append(0)
list_test.sort()
print(list_test)
list_test.reverse()
print(list_test)

# 1.2.1、不使用列表推导式得到[1,4,9]
list_1=[]
for i in range(1,4):
    list_1.append(i*i)
print(list_1)
# 1.2.2、使用列表推导式得到[1,4,9]
list_2=[i*i for i in range(1,4)]
print(list_2)
# 1.2.3、使用列表推导式嵌套if语句
list_3=[i**2 for i in range(1,4) if i != 1]
print(list_3)
# 1.2.4、嵌套循环使用列表推导式
list_4=[i*j for i in range(1,3) for j in range (1,3)]
print(list_4)

#2.1、元组定义方式1
tuple1=(1,2,3,4)
print(type(tuple1))
#2.2、元组定义方式2
tuple2=1,2,3,4
print(type(tuple2))
#2.3、元组的不可变特性
tuple3=1,2,3,4,5
# tuple3[0]="a" # 执行会报错
# 2.3、注意：元组中有列表元素时，列表的值是可以修改的
ele_list=[1,2,4,5,5,6,5,5]
tuple4= 1,2,3,ele_list
print("tuple4 before:",tuple4)
ele_list.clear()
print("tuple4 after:",tuple4)

#3.1集合定义
set1={1,2,1}
print(set1)
set2=set()
print(set2)
print(len(set2))
#3.2集合函数
set_3={1,2,3,5,7}
set_4={1,3,5,8}
print(set_3.union(set_4))
print(set_3.intersection(set_4))
print(set_3.difference(set_4))
set_4.add(10)
print(set_4)

#4.1、字典定义
dict1={}
dict2=dict(a="a1",b="b1",c=2)
print(dict1)
print(dict2)
#4.2、函数
print(dict2.keys())
dict2.pop("a")
print(dict2)