#!usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2020-09-08
# @Author    : Joey Jiang
# @File      : c020.py
# @Software  : PyCharm
# @Descrption: python单元测试-TestCase&TestSuite

"""
1、编写一个数学计算类，要求初始化方法带参数（两个数字），能够实现加减乘除（方法）
"""
class Calc:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1+self.num2
    def jian(self):
        return self.num1-self.num2
    def mul(self):
        return self.num1*self.num2
    def stu(self):
        try:
            return self.num1 / self.num2
        except ZeroDivisionError:
            print("除数不能为0")
"""
2、定义一个手机类，具有打电话和录音功能，打电话的时候可以录音，也可以不录音
"""
class Mobile:
    def record(self):
        print("录音")
    def call(self,is_record=False):
        if is_record:
            self.record()
        print("打电话")
"""
3、（选做题）
编写一个工具箱类和工具类，需要有工具的名称、功能描述、价格、能够添加工具、删除工具、查看工具，并且能够获取工具箱中工具的总数
"""
class Tool:
    def __init__(self,name,desc,price):
        self.name=name
        self.desc=desc
        self.price=price
class ToolBox:
    def __init__(self):
        self.tool_box_list=[]
    def add_tool(self,tool:Tool):
        self.tool_box_list.append(tool)
    def del_tool(self,tool:Tool):
        self.tool_box_list.remove(tool)
    def view_tool(self,tool:Tool):
        return self.tool_box_list[0]
    def count(self):
        return len(self.tool_box_list)
tool_box=ToolBox()
too1=Tool("扳手","拧螺丝","20")
too2=Tool("斧子","砍树","100")
tool_box.add_tool(too1)
#大致实现，省略很多内容
