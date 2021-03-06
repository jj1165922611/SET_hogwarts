#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-13
# @Author     : Joey Jiang
# @File       : test_base9_3_13.py
# @Software   : Visual Studio Code
# @Description: pytest测试框架
'''
indirect=True，传入的参数当做函数来执行
'''
import pytest
test_user_data=['Jack','Joey']
@pytest.fixture(scope="module")
def login_1(request):
    user=request.param
    print(f"登录用户：{user}")
    return user
@pytest.mark.parametrize("login_1",test_user_data,indirect=True)
def test_login_1(login_1):
    a=login_1
    print(f"测试用例中login_1的返回值{a}")
    assert a !=""


if __name__ == "__main__":
    pytest.main(['-v','-s','test_base9_3_13.py'])