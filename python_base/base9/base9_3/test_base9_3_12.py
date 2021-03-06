#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-13
# @Author     : Joey Jiang
# @File       : test_base9_3_12.py
# @Software   : Visual Studio Code
# @Description: pytest测试框架
'''
参数组合，如下共6条测试用例
'''
import pytest
@pytest.mark.parametrize("x",[1,2])
@pytest.mark.parametrize("y",[3,4,5])
def test_eval(x,y):
    print(f"{x}:{y}")


if __name__ == "__main__":
    pytest.main(['-v','-s','test_base9_3_12.py'])