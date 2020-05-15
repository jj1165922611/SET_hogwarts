#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-09
# @Author     : Joey Jiang
# @File       : test_base9_2_2.py
# @Software   : Visual Studio Code
# @Description: python unittest测试框架

import unittest
class Demo1Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls)->None:
        print("setUpClass")
    def setUp(self)->None:
        print("setUp")

    def tearDown(self)->None:
        print("tearDown")
    @classmethod
    def tearDownClass(cls)->None:
        print("tearDownClass")
    def test_case01(self):
        print("test_case01")
        self.assertEqual(1,1,msg="判断相等")
        self.assertIn('h','this',"包含") 
    def test_case02(self):
        print("test_case02")
        self.assertEqual(1,1,msg="判断相等")
        self.assertIn('h','this',"包含")
    @unittest.skip
    def test_case03(self):
        print("test_case03")
        self.assertEqual(1,1,msg="判断相等")
        self.assertIn('a','this',msg="包含")

class Demo2Test(unittest.TestCase):
    def test_case04(self):
        print("test_case04")
        self.assertIn("1","21")
if __name__ =="__main__":
    suite=unittest.TestSuite()
    suite.addTest(Demo1Test("test_case01"))
    suite.addTest(Demo2Test("test_case04"))
    unittest.TextTestRunner().run(suite)