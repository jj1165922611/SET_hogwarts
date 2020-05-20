#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-20
# @Author     : Joey Jiang
# @File       : test_calc_3.py
# @Software   : PyCharm
# @Description: pytest测试实战（二）
from python_base.base9.base9_8_9_9.calc_1 import Calc
import pytest,yaml
class TestCalc:
    def setup_class(self):
        self.calc=Calc()
    @pytest.mark.parametrize("a,b,expect",yaml.safe_load(open("test_calc.yml","rb")))
    def test_add(self,a,b,expect):
        data=(a,b)
        assert self.calc.add(*data)==expect
        assert self.calc.add1(data)==expect