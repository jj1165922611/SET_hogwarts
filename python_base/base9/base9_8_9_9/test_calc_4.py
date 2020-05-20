#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-20
# @Author     : Joey Jiang
# @File       : test_calc_4.py
# @Software   : PyCharm
# @Description: pytest测试实战（二）
from python_base.base9.base9_8_9_9.calc_1 import Calc
import pytest,yaml
class TestCalc:
    def setup_class(self):
        self.calc=Calc()
    def get_setp(self):
        with open("step.yml","rb") as f:
            return yaml.safe_load(f)
    def any_setps(self,data,expect):
        data1=self.get_setp()
        for i in data1:
            if i=="add":
                print(i)
                assert self.calc.add(*data)==expect
            elif i =="add1":
                print(i)
                assert self.calc.add1(data)==expect

    @pytest.mark.parametrize("a,b,expect",yaml.safe_load(open("test_calc.yml","rb")))
    def test_add(self,a,b,expect):
        data=(a,b)
        self.any_setps(data,expect)
        # assert self.calc.add(*data)==expect
        # assert self.calc.add1(data)==expect