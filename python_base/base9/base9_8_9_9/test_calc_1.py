#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-20
# @Author     : Joey Jiang
# @File       : test_calc_1.py
# @Software   : PyCharm
# @Description: pytest测试实战（二）
'''
参数化加数据驱动
'''
from python_base.base9.base9_8_9_9.calc import Calc
import pytest,yaml
class TestCalc:
    def setup_class(self):
        self.calc=Calc()
    @pytest.mark.parametrize("a,b,expect",yaml.safe_load(open("test_calc.yml","rb")))
    def test_add(self,a,b,expect):
        assert self.calc.add(a,b)==expect

    def select_div(self):
        assert self.calc.div(2,1)==2

    def test_sub(self):
        assert self.calc.sub(2,1)==1

    def test_mul(self):
        assert self.calc.mul(2,2)==4