#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-22
# @Author     : Joey Jiang
# @File       : test_calc_2.py
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

    @pytest.mark.parametrize("a,b,expect",get_data()["add"])
    def calc_add(self,a,b,expect,start):
        assert start.add(a,b)==expect

    @pytest.mark.parametrize("a,b,expect", get_data()["div"])
    def calc_div(self,a,b,expect,start):
        assert start.div(a,b)==expect

    @pytest.mark.parametrize("a,b,expect", get_data()["sub"])
    def calc_sub(self,a,b,expect,start):
        assert start.sub(a,b)==expect

    @pytest.mark.parametrize("a,b,expect", get_data()["mul"])
    def calc_mul(self,a,b,expect,start):
        assert start.mul(a,b)==expect