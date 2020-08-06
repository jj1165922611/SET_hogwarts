#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-21
# @Author     : Joey Jiang
# @File       : test_base9_9_6.py
# @Software   : PyCharm
# @Description: pytest测试实战（三）

'''
provide()是yield生成器，使用next()才能取值，或者list数据类型强转也可以读取生成器的值
'''
def provide():
    for i in range(5):
        print("before")
        yield i
        print("after")
p=provide()
print(next(p))
print(next(p))
