#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2020-07-21
# @Author     : Joey Jiang
# @File       : base7_3.py
# @Software   : PyCharm
# @Description: python控制流语法

# 1.1、分支结构
import random

a = 0
if a == 0:
    print("a=0")
else:
    print("a!=0")
# 1.2、多重分支
a = 1
if a == 1:
    print("a=1")
elif a == 2:
    print("a=2")
elif a == 3:
    print("a==3")
else:
    print("a!=1、2、3")
# 1.3、练习
# 分别使用分支嵌套以及多重分支去实现分段函数求值
#        3x - 5 (x>1)
# f(x)= x + 2 (-1<=x<=1)
#        5x + 3(x<-1)
# 1.3.1分支嵌套
x = -2
if x > 1:
    print(3 * x - 5)
else:
    if x >= -1:
        print(x + 2)
    else:
        print(5 * x + 3)
# 1.3.2多重分支
if x > 1:
    print(3 * x - 5)
elif x >= -1:
    print(x + 2)
else:
    print(5 * x + 3)

# 2.1练习
# 计算1~100的和
sum1 = 0
for i in range(1, 101):
    sum1 = sum1 + i
print(sum1)

# 2.2练习
# 加入分支结构实现1~100之间偶数的求和
sum2 = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum2 = sum2 + i
print(sum2)

# 2.3练习
# 使用python实现1~100之间偶数求和
sum3 = 0
for i in range(2, 101):
    if i % 2 == 0:
        sum3 = sum3 + i
print(sum3)

# 3、While循环
# 3.1、While Else
while_a = 1
while while_a == 1:
    print("while_a=1")
    while_a = while_a + 1
else:
    print("while_a!=1")
    print(while_a)
# 3.2、简单语句组
flag = 10
while flag == 10:
    flag = flag + 1
else:
    print(flag)

# 4、break语句
for i in range(4):
    if i == 2:
        break
    print("i=", i)
# 5、continue语句
for j in range(4):
    if j == 2:
        continue
    print("j=", j)
# 6、练习
"""
猜数字游戏，计算机出一个1~100之间的随机数由人来猜，
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""
guess_number = random.randint(1, 100)
print(guess_number)
while True:
    number = int(input("请输入一个1~100之间的整数>"))
    if number == guess_number:
        print("猜对了")
        break
    elif number > guess_number:
        print("大一点")
    else:
        print("小一点")
