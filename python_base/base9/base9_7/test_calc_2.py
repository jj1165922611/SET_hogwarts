#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-14
# @Auhtor     : Joey Jiang
# @File       : test_calc_2.py
# @Software   : Visual Studio Code
# @Description: 计算器
'''
使用一次setup()方法，有多条用例时，每个用例执行前都会先进行一次实例化calc=Calc()，用例中不需要写多次
'''
import pytest
from python_base.base9.base9_7.calc import Calc
from decimal import Decimal
class TestCalc:
    def setup(self):
        print("setup")
        self.calc=Calc()
    def teardown(self):
        print("teardown")
    def test_add_(self):
        calc=self.calc
        assert calc.add(1,2)==3
    def test_add_2(self):
        calc=self.calc
        assert calc.add(0.1,0.2)==0.3
    def test_add_3(self):
        calc=self.calc
        assert calc.add(Decimal('0.1'),Decimal('0.2'))==Decimal('0.3')
    def test_div(self):
        calc=self.calc
        assert calc.div(3,2)==1.5
if __name__ == "__main__":
    pytest.main(['-v','-s','test_calc.py'])