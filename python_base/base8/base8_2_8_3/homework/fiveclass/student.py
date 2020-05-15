#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-04-26
# @Author     : Joey Jiang
# @File       : student.py
# @Software   : Visual Studio Code
# @Description: student类


'''
定义一个类，类名为Student
'''


class Student:
    # 定义一个变量name，赋值为“小蔡”
    name = "小蔡"
    # 定义一个变量age，赋值为15
    age = 15
    # 定义一个变量stu_no，赋值为1
    stu_no = 1
    # 定义一个字典score，
    # 创建关键字chinese、math、english并分赋值为90、100、85
    score = dict(chinese=90, math=100, english=85)

    '''
    *创建一个方法sing
    '''

    def sing(self):
        print("鸡你太美")

    '''
    *创建一个方法jump
    '''

    def jump(self):
        print("广场舞")

    '''
    *创建一个方法rap
    '''

    def rap(self):
        print("大碗面")


if __name__ == "__main__":
    student = Student()  # 实例化Student()类
    print(f"学号为{student.stu_no}号的学生，名字叫{student.name}，\
今年{student.age}岁，他的期末考试成绩为语文{student.score.get('chinese')}分，\
数学{student.score.get('math')}分，英语{student.score.get('english')}分")
    student.sing()  # 调用Student类中sing方法
    student.jump()  # 调用Student类中jump方法
    student.rap()  # 调用Student类中rap方法
