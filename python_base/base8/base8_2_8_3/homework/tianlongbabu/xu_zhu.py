#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2020-04-27
# @Author      : Joey Jiang
# @File        : xu_zhu.py
# @Software    : Visual Studio Code
# @Description : 虚竹类

'''
* 定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
* 加入模块化改造
'''
from tong_lao import TongLao  # 从模块tong_lao中导入类TongLao

'''
定义一个类，类名为XuZhu，继承与TongLao类
'''


class XuZhu(TongLao):
    '''
    初始化XuZhu类，覆盖父类的__init__方法
    '''

    def __init__(self, hp, power):
        super()
        self.hp = hp
        self.power = power

    '''
    *创建一个read方法
    '''

    def read(self):
        print("罪过罪过")

    '''
    *覆盖父类see_people方法
    *参数
        name: 名字
    '''

    def see_people(self, name):
        if name == "DY":  # 判断name是否等于“DY”(段誉)
            print("二哥")
        elif name == "QF":  # 判断name是否等于“QF”(乔峰)
            print("大哥")


if __name__ == "__main__":
    xu_zhu = XuZhu(1000, 200)  # 实例化XuZhu类
    xu_zhu.see_people("DY")  # 调用XuZhu类中see_people方法，名字为“DY”
    xu_zhu.fight_zms(1000, 200)  # 调用父类中fight_zms方法，敌人血量为1000，敌人武力值为200
    xu_zhu.read()  # 调用XuZhu类中read方法
