#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-12
# @Author     : Joey Jiang
# @File       : test_base9_3_3.py
# @Software   : Visual Studio Code
# @Description: pytest测试框架

'''
1、测试文件test_*开头，测试类以Test开头，测试方法以test_*开头
2、Pycharm运行pytest
'''
import pytest
class TestDemo:
    
    def func(self,x):
        x=x+1
        print(f"x={x}")
        return x

    def test_func(self):
        assert self.func(1)==2
        print("31132")
        assert self.func(2)==4

    def test_func1(self):
        assert self.func(2)==3

if __name__ == "__main__":
    # pytest.main()
    # pytest.main(['-v','-s','test_base9_3_3.py'])
    pytest.main(['-v','-s','python_base/base9/base9_3/'])