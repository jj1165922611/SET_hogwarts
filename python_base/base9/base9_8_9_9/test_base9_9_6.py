#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-21
# @Author     : Joey Jiang
# @File       : test_base9_9_6.py
# @Software   : PyCharm
# @Description: pytest测试实战（三）

def provide():
    for i in range(5):
        print("before")
        yield i
        print("after")
p=provide()
print(next(p))
print(next(p))
