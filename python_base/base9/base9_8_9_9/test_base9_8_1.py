#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-20
# @Author     : Joey Jiang
# @File       : test_base9_8_1.py
# @Software   : PyCharm
# @Description: pytest测试实战（二）

class Hello:
    hello="Hello"

    # 实例方法，不能被类直接调用
    def a1(self):
        print("a1")
    @classmethod
    def a2(self):
        print("a2")

print("实例变量和类变量")
h1=Hello()
h2=Hello()
print(h1.hello)
print(h2.hello)
print(Hello.hello)

h1.hello="Hello1"
print(h1.hello)
print(h2.hello)
print(Hello.hello)

Hello.hello="hello2"
print(h1.hello)
print(h2.hello)
print(Hello.hello)

h2.hello="hello3"
print(h1.hello)
print(h2.hello)
print(Hello.hello)

h1.a1()
h1.a2()
# Hello.a1()
Hello.a2()