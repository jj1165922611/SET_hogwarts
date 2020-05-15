#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-12
# @Author     : Joey Jiang
# @File       : test_base9_3_2.py
# @Software   : Visual Studio Code
# @Description: pytest测试框架
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
    