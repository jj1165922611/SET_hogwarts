#!/usr/bin/env python
# -*- coding -*-
# @Time       : 2020-07-26
# @Author     : Joey Jiang
# @File       : python_oop.py
# @Software   : PyCharm
# @Description: 类与示例

class Drawing:
    area=100
    style="North Europe"
    __style2="China Style"

    def cook(self):
        # self._self_method()
        print("可以做饭")
    def sleep(self):
        print("可以睡觉")
    def __self_method(self):
        print("我是私有方法")


print(Drawing.cook)
my_house=Drawing()
my_house.sleep()
my_house._Drawing__self_method() # 通过name的重写方法可以调用到私有属性，但是不建议这么用
# my_house.__self_method() # 执行会报错，私有变量不能被引用调用
