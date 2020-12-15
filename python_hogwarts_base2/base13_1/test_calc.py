#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020/12/15 0015 20:23
# @Author     : Joey Jiang
# @File       : test_calc.py
# @Software   : PyCharm
# @Description: 测试计算器的加减乘除功能
import pytest

from python_hogwarts_base2.base13_1.calc import Calc


class TestCalc:
    def setup(self):
        self.calc = Calc()

    def test_add(self):
        result = self.calc.add(3, 4)
        assert result == 7

    def test_sub(self):
        result = self.calc.sub(3, 4)
        assert result == -1

    # 参数化装饰函数
    # ids参数增加可读性
    @pytest.mark.parametrize("a,b,expect", [(3, 4, 12), (2, 2, 5)],ids=["success","fail"])
    def test_mul(self, a, b, expect):
        result = self.calc.mul(a, b)
        assert expect == result

    def test_div(self):
        result = self.calc.div(3, 3)
        assert result == 1
