#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time       : 2020-09-2
# @Author     : Joey Jiang
# @File       : calc.py
# @Software   : PyCharm
# @Description: pytest实战（一）
import sys
print(sys.path)
import unittest


from python_hogwarts12.python.calc import Calc


class TestCalc(unittest.TestCase):
    def test_add(self):
        assert  Calc().add(2,3)==5