#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-12
# @Author     : Joey Jiang
# @File       : test_base9_3_2.py
# @Software   : Visual Studio Code
# @Description: pytest测试框架
'''
1、测试文件以test_*开头，测试类以Test开头，测试方法以test_*开头
2、命令行执行，使用各种参数
3、失败重新运行
4、多条断言第一条失败也继续执行
'''
import pytest
class TestDemo:
    
    def func(self,x):
        x=x+1
        print(f"x={x}")
        return x

    def test_func(self):
        assert self.func(1)==2
        print("31132")
        assert self.func(2)==4

    def test_func1(self):
        assert self.func(2)==3
    def test_func2(self):
        pytest.assume(self.func(2)==4)
        pytest.assume(self.func(2)==3)
    