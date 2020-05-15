#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-04-26
# @Author     : Joey Jiang
# @File       : python.py
# @Software   : Visual Studio Code
# @Description: python类

'''
定义一个类，类名为Python
'''


class Python:

    interpreter = "python3"  # 解释器
    package_management = "pip3"  # 标准库管理器
    basic_data_type = ["variable", "number", "string", "list"]
    control = ["if", "else", "elif", "for", "in",
               "while", "break", "continue"]  # 控制流语法
    function = ["def", "return", "*name", "**name", "lambda", "类型提示"]  # 函数
    module = ["package", "System", "extra", "custom"]  # 模块
    input_output = ["format", "F-String", "%"]  # 输入与输出
    json = ["dump", "dumps", "load", "loads"]  # Json
    file_x = ["open", "read", "close"]  # 文件
    exception = ["try", "except", "else", "finally"]  # 异常
    literal = ["number", "string", "boolean",
               "list", "set", "tuple", "dict", "None"]  # 字面量
    object_x = ["class", "method", "init", "extend", "方法覆盖"]  # 对象

    '''
    *创建一个install_package()方法
    *参数
        package_name: 包名字
    '''

    def install_package(self, package_name):
        print(f"使用pip3 install {package_name}的方式安装包")


if __name__ == "__main__":
    python = Python()  # 实例化Python类
    python.install_package("selenium")
