#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-14
# @Auhtor     : Joey Jiang
# @File       : test_calc_4.py
# @Software   : Visual Studio Code
# @Description: 计算器
'''
使用pytest.mark.parametrize()进行参数化，结合yaml文件数据驱动
'''
import pytest
from python_base.base9.base9_7.calc import Calc
from decimal import Decimal
import yaml
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
    @pytest.mark.parametrize("a,b,expected",yaml.safe_load(open("test_calc_6.yml","rb")))
    def test_add_(self,a,b,expected):
        calc=self.calc
        assert calc.add(a,b)==expected
    def test_add_3(self):
        calc=self.calc
        assert calc.add(Decimal('0.1'),Decimal('0.2'))==Decimal('0.3')
    def test_div(self):
        calc=self.calc
        assert calc.div(3,2)==1.5
if __name__ == "__main__":
    pytest.main(['-v','-s','test_calc.py'])