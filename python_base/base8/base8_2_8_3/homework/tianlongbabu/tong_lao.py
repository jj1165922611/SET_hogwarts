#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-04-27
# @Author     : Joey Jiang
# @File       : tong_lao.py
# @Software   : Visual Studio Code
# @Description: 天山童姥类

'''
* 定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。
TongLao类里面有2个方法，
1. see_people方法，需要传入一个name参数，
如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，
如果传入“李秋水”，打印“呸，贱人”，
如果传入“丁春秋”，打印“叛徒！我杀了你”
2. fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。
需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
'''

'''
定义一个类，类名为TongLao
'''


class TongLao:
    '''
    *初始化TongLao类
    *参数
       hp: 血量
       power: 武力值
    '''

    def __init__(self, hp, power):
        self.hp = hp  # 定义类变量hp，将参数hp的值赋给它
        self.power = power  # 定义类变量power，将参数power的值赋给它

    '''
    *创建一个see_people方法
    *参数
       name: 名字
    '''

    def see_people(self, name):
        if name == "WYZ":  # 判断名字是否等于WYZ(无崖子)
            print("师弟！！！！")
        elif name == "LQS":  # 判断名字是否等于LQS(李秋水)
            print("呸，贱人")
        elif name == "DCQ":  # 判断名字是否等于DCQ(丁春秋))
            print("叛徒！我杀了你")

    '''
    *创建一个fight_zms方法
    *参数
       enemy_hp: 敌人的血量
       enemy_power: 敌人的武力值
    '''

    def fight_zms(self, enemy_hp, enemy_power):
        self.hp = self.hp/2  # 使用天山折梅手，类变量hp的值变为原来的一半
        self.power = self.power*10  # 使用天山折梅手，类变量power的值变为原来的10倍
        self.hp = self.hp-enemy_power  # 受到敌人攻击，类变量hp的值减去敌人的武力值power
        enemy_hp = enemy_hp-self.power  # 敌人受到攻击，敌人hp的值减去童姥的武力值power
        if self.hp > enemy_hp:  # 判断童姥的hp是否大于敌人的hp
            print("童姥武功盖世！")
        elif self.hp == enemy_hp:  # 判断童姥的hp是否小于敌人的hp
            print("真是势均力敌的战斗！")
        else:  # 判断童姥的hp是否等于敌人的hp
            print("那厮竟然赢了姥姥！一起上")


if __name__ == "__main__":
    tong_lao = TongLao(1000, 50)  # 实例化TongLao类，血量为1000，武力值为50
    tong_lao.see_people("WYZ")  # 调用TongLao类中see_people方法，名字为"WYZ"
    tong_lao.see_people("LQS")  # 调用TongLao类中see_people方法，名字为"LQS"
    tong_lao.see_people("DCQ")  # 调用TongLao类中see_people方法，名字为"DCQ"
    # 调用TongLao类中see_people方法，敌人的血量为501，敌人的武力值为500
    tong_lao.fight_zms(501, 500)
