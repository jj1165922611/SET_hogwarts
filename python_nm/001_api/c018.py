#!usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2020-09-08
# @Author    : Joey Jiang
# @File      : c018.py
# @Software  : PyCharm
# @Descrption: 面向对象编程--类作业讲解

"""
1、实现一个手机类，并实例化你的手机
要求类里要有：属性+行为，至少应该具有品牌，型号等信息。有拨打电话、发短信等功能
"""
class Mobile:
    def __init__(self,brand,style):
        self.brand=brand
        self.style=style
    def call(self,phone_num):
        print("您拨打的电话不在服务区",phone_num)
    def send_message(self,phone_num):
        print("发送成功",phone_num)
"""
2、灰色的Tom猫，今年1岁，吃着美味的食物，喝着可口的饮料，非常享受的样子
a、根据以上信息，抽象出一个类
b、定义相关属性，并能在类的外面调用
c、定义相关方法，并在方法中打印
"""
class Cat:
    def __init__(self,name,age,color):
        self.name=name
        self.age=age
        self.color=color
    def eat(self):
        print("吃着美味的食物")
    def drink(self):
        print("喝着可口的饮料")
tom=Cat("Tom",1,"grey")
print(tom.name)
print(tom.age)
print(tom.color)
tom.eat()
tom.drink()

"""
3、编写如下程序

创建一个名为Restaurant的类，要求拥有饭店名（restaurant_name）和美食种类(cooking_type)两个属性
a、需创建一个名为describe_restaurant()的方法(描述饭店名和美食种类相关信息)，和一个名为open_restaurant()的方法
b、根据这个类创建一个名为restaurant的实例，分别打印其两个属性，再调用两个方法
"""
class Restaurant:
    def __init__(self,restaurant_name,cooking_type):
        self.restaurant_name=restaurant_name
        self.cooking_type=cooking_type
    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cooking_type)
    def open_restaurant(self):
        print(f"{self.restaurant_name}正在营业")
restaurant=Restaurant("和平","猪爪")
restaurant.describe_restaurant()
restaurant.open_restaurant()

"""
4、编写如下程序
创建一个data.txt文件，来添加数据
a、第一行添加：name,age,gender
b、从第一行开始，每行添加用户信息，例如
张三,11,男
李四,13,男
小红,12,女
c、具体信息要求来自一个嵌套字典的列表
person_info=[
    {"name":"张三","age":11,"gender":"男"},
    {"name":"李四","age":13,"gender":"男"},
    {"name":"小红","age":12,"gender":"女"}
    ]
d、需要将所有用户信息写入data.txt再读出
"""
person_info=[
    {"name":"张三","age":"11","gender":"男"},
    {"name":"李四","age":"13","gender":"男"},
    {"name":"小红","age":"12","gender":"女"}
]

def dict_to_str(dict1,flag):
    str1=""
    line=[]
    for i in (dict1.keys() if flag=="keys" else dict1.values()):
        line.append(i)
    str1=",".join(line)+"\n"
    return str1

with open("data.txt","w+",encoding="utf-8") as f:
    f.write(dict_to_str(person_info[0],"keys"))
    for i in person_info:
        f.write(dict_to_str(i,"values"))

with open("data.txt","r",encoding="utf-8") as f:
    print(f.read())

"""
5、编写如下程序
有两行数据，存放在txt文件里
url:xxx1@moblie:1234@pwd:1234
url:xxx2@moblie:1235@pwd:1235

取出数据，并返回下列格式的数据
[
    {"url":"xxx1","moblie":"1234","pwd":"1234"},
    {"url":"xxx2","moblie":"1235","pwd":"1235"},
]
"""
def str_to_dcit(str1: str):
    list1=str1.split("@")
    dict1={}
    for i in  list1:
        key,value=i.split(":")
        dict1[key]=value
    return dict1
str1="url:xxx1@moblie:1234@pwd:1234"
print(str_to_dcit(str1))
# 省略了文件读写，编写了核心部分

"""
6、编写如下程序
优化生鲜超市买橘子程序
a、收银员输入橘子的价格，单位：元/斤
b、收银员输入用户买橘子的重量，单位：斤
c、计算并且输出付款金额
新需求
d、使用捕获异常的方式，处理用户输入无效的情况
"""
price=input("橘子价格(元/斤)：")
weight=input("橘子重量(斤)：")
try:
    print(float(price) * float(weight))
except ValueError:
    print("ValueError")
except TypeError:
    print("TypeError")
except:
    print("others expection")