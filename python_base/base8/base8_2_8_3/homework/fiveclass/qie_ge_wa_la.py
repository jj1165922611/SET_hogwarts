#!usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-04-28
# @Author     : Joey Jiang
# @File       : qie_ge_wa_la.py
# @Software   : Visual Studio Code
# @Description: 窃格瓦拉类

'''
定义一个类，类名为QieGeWaLa
'''


class QieGeWaLa:
    name = "窃格瓦拉"  # 定义一个变量name，赋值为“窃格瓦拉”
    age = "28"  # 定义一个变量age，赋值为“28”

    '''
    *创建一个get_caught方法
    '''

    def get_caught(self):
        print("他告诉警察：")
        print("里面的人个个都是人才，说话又好听")
        print("打工是不可能打工的，这辈子都不可能打工的")


if __name__ == "__main__":
    qie_ge_wa_la = QieGeWaLa()  # 实例化QieGeWaLa类
    print(f"故事的主人公是{qie_ge_wa_la.name}")
    print(f"今年{qie_ge_wa_la.age}岁")
    qie_ge_wa_la.get_caught()  # 调用QieGeWaLa类中get_caught()方法
