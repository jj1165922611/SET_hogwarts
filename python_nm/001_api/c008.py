#!usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2020-09-07
# @Author    : Joey Jiang
# @File      : c008.py
# @Software  : PyCharm
# @Descrption: Python函数篇编写函数&return

"""
1、商场降价促销，所有原价都是整数。
如果购买金额50-100元，打9折；如果大于100，打8折。根据客人购买商品总价显示折扣和折后价
"""
price=int(input("打折前总价："))
if price<50:
    print("不享受优惠，最终价为：",price)
elif price<=100:
    print("打9折，最终价为：",price*0.9)
else:
    print("打8折，最终价为：", price * 0.8)
"""
3、使用遍历循环完成剪刀石头布，提示用户要出的拳：石头(1)/剪刀(2)/布(3)/退出(4)
电脑随机出拳比较胜负，显示用户胜、负还是平局
"""
print("""尊敬的用户，您可以输入下面的数字进行选择：
1、出石头输入1
2、出剪刀输入2
3、出布输出3
4、退出输入4
""")
import random
while True:
    robot = random.randint(1, 3)
    human = int(input("请选择:"))
    if human==4:
        print("您已退出")
        break
    if human==robot:
        print("平局")
        continue
    if human==3:
        if robot==1:
            print("胜利！")
            continue
        else:
            print("失败！")
            continue
    elif human==2:
        if robot==1:
            print("失败！")
            continue
        else:
            print("胜利！")
            continue
    elif human==1:
        if robot==2:
            print("胜利！")
            continue
        else:
            print("失败！")
            continue


"""
4、求三个整数中的最大值
"""
a=input("第一个数")
b=input("第二个数")
c=input("第三个数")