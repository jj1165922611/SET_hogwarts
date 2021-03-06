#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-09
# @Author     : Joey Jiang
# @File       : test_base9_2_3.py
# @Software   : Visual Studio Code
# @Description: python unittest测试框架

'''
执行用例方法3：unittest.TestLoader(),同时测试多个类
'''
import unittest
from python_base.base9.base9_2.test_base9_2_2 import Demo1Test, Demo2Test
if __name__ == "__main__":
    suite1 = unittest.TestLoader().loadTestsFromTestCase(Demo1Test)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(Demo2Test)
    suite = unittest.TestSuite([suite1, suite2])
    unittest.TextTestRunner().run(suite)
