#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-19
# @Author     : Joey Jiang
# @File       : test_calc.py
# @Software   : PyCharm
# @Description: pytest实战（一）作业

'''
编写 Calc 这个类add() ，div() 这两个方法的测试用例
按照等价类去设计测试用例
把代码上传到github, 并回贴你的github的地址
'''
from python_base.base9.base9_7.calc import Calc
import yaml,pytest
'''
定义一个类，类名为TestCalc
'''
class TestCalc():

    '''
    *创建一个test_add测试用例
    *参数
        a: 加数
        b: 加数
        expect: 期望结果
    '''
    @pytest.mark.parametrize("a,b,expect",yaml.safe_load(open("test_calc.yml", "rb"))["add"])
    def test_add(self,a,b,expect):
        # 判断a+b的和是否等于expect
        assert  a+b == expect

    '''
    *创建一个test_div测试用例
    *参数
        a: 除数
        b: 被除数
        expect: 期望结果
    '''
    @pytest.mark.parametrize(["a","b","expect"],yaml.safe_load(open("test_calc.yml", "rb"))["div"])
    def test_div(self,a,b,expect):
        # 判断a/b的商是否等于expect
        assert  a/b == expect
