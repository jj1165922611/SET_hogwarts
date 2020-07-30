#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-09
# @Author     : Joey Jiang
# @File       : test_base9_2_4.py
# @Software   : Visual Studio Code
# @Description: python unittest测试框架

'''
执行用例方法4：unittest.defaultTestLoader.discover(),匹配某个路径下所有以test开头的py文件，执行这些文件下所有的测试用例
'''
import os
import unittest
import time
from HTMLTestRunner_PY3 import HTMLTestRunner
if __name__ == '__main__':
    print(os.getcwd())
    test_dir=r'G:\python\SET_hogwarts\python_base\base9\base9_2'
    discover=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
    #unittest.TextTestRunner().run(discover)
    now=time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())
    filename=test_dir+"/"+now+"result.html"
    with open(filename,'wb') as fp:
        runner=HTMLTestRunner(stream=fp,title='测试报告',description='测试用例')
        runner.run(discover)