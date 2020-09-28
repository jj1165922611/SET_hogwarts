#!usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2020-09-09
# @Author    : Joey Jiang
# @File      : c024.py
# @Software  : PyCharm
# @Descrption: python之excel读写测试数据

"""
1、定义一个ExcelManual类，具有获取sheet表单，读取单元格和修改单元格功能
"""

class ExcelManual:
    def __init__(self,filename):
        self.wb=""
    def get_sheet(self,sheetname):
        print("获取sheet表单")
    def read_cell(self,row,column):
        print("读取单元格")
    def change_content(self,row,column,value):
        print("改变值")