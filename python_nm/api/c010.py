#!usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2020-09-07
# @Author    : Joey Jiang
# @File      : c010.py
# @Software  : PyCharm
# @Descrption: Python函数篇函数参数类型学习使用

"""
用户输入1-7七个数字，分别代表周一到周日

如果输入1-5，打印周一~周五；如果输入6-7，打印周末
如果输入0，退出循环
输入其他内容，提示"输入有误，请重新输入"
"""
dict_week={
    "1":"周一",
    "2":"周二",
    "3":"周三",
    "4":"周四",
    "5":"周五",
    "6":"周末",
    "7":"周末",
}
def get_week():
    while True:
        num=input("请输入数字：")
        # if type(num)!= int:
        #     print("输入有误，重新输入")
        #     continue
        if (num) not in dict_week.keys():
           print("输入有误，重新输入")
           continue
        elif int(num)==0:
            break
        else:
            print(dict_week.get(num))
            break
get_week()