#!/usr/bin/env python
# -*-coding: utf-8 -*-
# @Time       : 2020-04-28
# @Author     : Joey Jiag
# @File       : jira.py
# @Software   : Visual Studio Code
# @Description: linux类

'''
定义一个类，类名为Linux
'''


class Linux:
    system = "centOS7"  # 定义一个变量system，赋值为“centOS7”
    shell = "bash"  # 定义一个变量shell，赋值为“bash”

    '''
    *初始化Linux类
    *参数
        usr: 用户
        passwd: 密码
    '''

    def __init__(self, usr, passwd):
        self.usr = usr  # 定义一个变量usr，赋值为“root”
        self.passwd = passwd  # 定义一个变量passwd，赋值为“123456”

    '''
    *创建一个login方法
    '''

    def login(self):
        if self.usr == "root" and self.passwd == "123456":  # 判断用户名和密码是否正确
            print(f"用户{self.usr}登录成功")
        else:
            print("登录失败，请检查用户名和密码")


if __name__ == "__main__":
    linux = Linux("root", "123456")  # 实例化Linux类，用户名为root，密码为123456
    print(f"用户名{linux.usr}")
    linux.login()  # 调用Linux类中login方法
