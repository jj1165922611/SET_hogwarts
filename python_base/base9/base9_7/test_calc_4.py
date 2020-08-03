#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-14
# @Auhtor     : Joey Jiang
# @File       : test_calc_4.py
# @Software   : Visual Studio Code
# @Description: 计算器
'''
用例运行的级别分类以及调用顺序(2)
'''
import pytest
from python_base.base9.base9_7.calc import Calc
from decimal import Decimal

def setup_module():
    print("setup_module")
def teardown_module():
    print("teardown_module")

class TestCalc:
    def setup_class(self):
        print("setup_class")
        self.calc=Calc()
    def teardown_class(self):
        print("teardown_class")
    def setup(self):
        print("setup")
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