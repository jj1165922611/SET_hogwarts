#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-22
# @Author     : Joey Jiang
# @File       : test_calc_3.py
# @Software   : PyCharm
# @Description: pytest实战（二）、（三）
import pytest,yaml
from python_base.base9.base9_8_9_9.homework.calc import Calc

@pytest.fixture()
def start():
    calc=Calc()
    return calc

def get_data():
    data=yaml.safe_load(open("test_calc.yml","rb"))
    return data
class TestCalc:

    def setup(self):
        self.data=yaml.safe_load(open("step.yml","rb"))

    def any_step(self,a,b,expect,start1,rule):
        for i in self.data[rule]:
            print(i)
            if "add"==i:
                assert start1.add(a,b)==expect
            elif "div"==i:
                assert start1.div(a,b)==expect

    @pytest.mark.parametrize("a,b,expect",get_data()["add"])
    def test_add(self,a,b,expect,start):
        rule="add"
        self.any_step(a,b,expect,start,rule)

    @pytest.mark.parametrize("a,b,expect",get_data()["div"])
    def test_div(self,a,b,expect,start):
        rule="div"
        self.any_step(a,b,expect,start,rule)