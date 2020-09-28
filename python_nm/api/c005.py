#!usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2020-09-07
# @Author    : Joey Jiang
# @File      : c005.py
# @Software  : PyCharm
# @Descrption: 常用数据类型List&dict

"""
1、某相亲节目需要获取你的个人信息，请存储你的：姓名、性别、年龄
2、有一个对你很感兴趣，平台需要补充您的身高和联系方式
3、平台为了保护您的隐私，需要删除您的联系方式
4、你为了获取更好的成绩，需要取一个花名，并修改身高和其他你觉得需要修改的信息
5、你进一步添加自己的兴趣，至少需要3项。一经确定，不可单独修改各个兴趣点
"""
info=["小明","男",18]
print("1: ",info)
info.extend([175.5,123456789012])
print("2: " ,info)
info.pop(-1)
print("3: ",info)
info.append("鸣人")
print("4: ",info)
info.append(("羽毛球","毛笔字","画画"))
print("5: " , info)