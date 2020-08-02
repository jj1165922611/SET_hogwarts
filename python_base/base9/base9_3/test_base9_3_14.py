#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-13
# @Author     : Joey Jiang
# @File       : test_base9_3_14.py
# @Software   : Visual Studio Code
# @Description: pytest测试框架
'''
mark.skipif,如果符合条件，跳过某个用例
当系统平台是windows时，跳过用例test_login_2
'''
import pytest
import sys
test_user_data=['Jack','Joey']
@pytest.fixture(scope="module")
def login_1(request):
    user=request.param
    print(f"登录用户：{user}")
    return user
@pytest.mark.skip
@pytest.mark.parametrize("login_1",test_user_data,indirect=True)
def test_login_1(login_1):
    a=login_1
    print(f"测试用例中login_1的返回值{a}")
    assert a !=""
@pytest.mark.skipif(sys.platform=="win32",reason="不在windows系统上执行")
def test_login_2():
    print("test_login_2")

if __name__ == "__main__":
    pytest.main(['-v','-s','test_base9_3_14.py'])