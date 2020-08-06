#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-20
# @Author     : Joey Jiang
# @File       : test_calc.py
# @Software   : PyCharm
# @Description: pytest测试实战（二）
'''
pytest-ordering控制执行顺序
'''
from python_base.base9.base9_8_9_9.calc import Calc
import pytest,yaml
class TestCalc:
    def setup_class(self):
        self.calc=Calc()
    @pytest.mark.parametrize("a,b,expect",yaml.safe_load(open("test_calc.yml","rb")))
    @pytest.mark.run("third")
    def test_add(self,a,b,expect):
        assert self.calc.add(a,b)==expect

    @pytest.mark.run(order=1)
    def test_div(self):
        assert self.calc.div(2,1)==2

    @pytest.mark.run(order=-1)
    def test_sub(self):
        assert self.calc.sub(2,1)==1

    @pytest.mark.run(order=0)
    def test_mul(self):
        assert self.calc.mul(2,2)==4