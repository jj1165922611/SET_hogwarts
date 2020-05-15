#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-13
# @Author     : Joey Jiang
# @File       : test_base9_3_11.py
# @Software   : Visual Studio Code
# @Description: pytest测试框架
import pytest
@pytest.mark.parametrize("test_input,expected",[("3+5",8),("10+10",21),("30+30",60)])
def test_eval(test_input,expected):
    assert eval(test_input)==expected


if __name__ == "__main__":
    pytest.main(['-v','-s','python_base/base9/base9_3/test_base9_3_11.py'])