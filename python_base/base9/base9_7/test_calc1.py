#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-14
# @Auhtor     : Joey Jiang
# @File       : test_calc_1.py
# @Software   : Visual Studio Code
# @Description: 计算器
import pytest
from python_base.base9.base9_7.calc import Calc
class TestCalc:
    def test_add_(self):
        calc=Calc()
        assert calc.add(1,2)==3
    def test_add_2(self):
        calc=Calc()
        assert calc.add(0.1,0.2)==0.3
    def test_div(self):
        calc=Calc()
        assert calc.div(3,2)==1.5
pytest.main(['-v','-s','test_calc.py'])