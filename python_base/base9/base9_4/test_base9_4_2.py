#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-16
# @Author     : Joey Jiang
# @File       : test_base9_4_2.py
# @Software   : Pycharm
# @Description: 参数化用例

import pytest
import yaml

@pytest.mark.parametrize("a,b",yaml.safe_load(open(r"G:\python\SET_hogwarts\python_base\base9\base9_4\data.yml","rb")))
def test_string(a,b):
    print(a+b)
@pytest.mark.parametrize(["a","b"],[(10,20),(20,30)])
def test_list(a,b):
    print(a+b)
@pytest.mark.parametrize(("a","b"),[(10,20),(20,30)])
def test_tuple(a,b):
    print(a+b)
if __name__ == '__main__':
    pytest.main(['-v','-s','test_base9_4_2.py'])