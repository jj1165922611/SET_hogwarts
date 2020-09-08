#!usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2020-09-07
# @Author    : Joey Jiang
# @File      : c014.py
# @Software  : PyCharm
# @Descrption: Python调试方法以及技巧

import os
print(os.getcwd())
print(__file__)
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.join(os.getcwd(),"不存在.txt"))

