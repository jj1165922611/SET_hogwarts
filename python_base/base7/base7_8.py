#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-04-25
# @Author     : Joey Jiang
# @File       : base7_8.py
# @Software   : Visual Studio Code
# @Description: python错误与异常

try:
    num1 = int(input("输入一个除数>"))
    num2 = int(input("输入一个被除数>"))
    print(num1/num2)
except ValueError:
    print("输入需要是数值型整数")
except ZeroDivisionError:
    print("被除数不能为0")
except:
    print("通用型异常")
else:
    print("程序没有发生异常")
finally:
    print("无论是否发生异常，都执行")

# 自定义异常
class MyException(Exception):
    def __init__(self,value1,value2):
        self.value1=value1
        self.value2=value2
raise MyException("value1","value2")

x=10
if x!=5:
    raise Exception("这是抛出的异常")
