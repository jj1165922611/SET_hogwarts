#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-07-25
# @Author     : Joey Jiang
# @File       : base7_9.py
# @Software   : PyCharm
# @Description: python面向对象编程

# 1、类、方法和属性
class Person:
    name="name1"
    def get_name(self):
        return self.name
p2=Person()
print(p2.get_name())
p2.name="name2"
print(p2.get_name())

p3=Person()
print(p3.name)
Person.name="name3"
p4=Person()
print(p4.get_name())

# 实例、实例引用、实例变量
class Person1:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    # 设置只属于自己的属性
    def set_att(self,value):
        self.value=value
    def eat(self):
        print(f"name:{self.name},age:{self.age},gender:{self.gender}")
    def run(self):
        print(f"name:{self.name},age:{self.age},gender:{self.gender}")
    def drink(self):
        print(f"name:{self.name},age:{self.age},gender:{self.gender}")
xiaoming=Person1("xm",10,"M")
xiaohong=Person1("xh",11,"F")
print(xiaoming.name)
xiaoming.run()
xiaohong.drink()