#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-16
# @Author     : Joey Jiang
# @File       : test_base9_5_1.py
# @SOftware   : Pycharm
# @Description: 数据驱动

'''
yaml数据驱动
'''
import pytest
import yaml
class TestDemo:
    @pytest.mark.parametrize("env",yaml.safe_load(open("env.yml","rb")))
    def test_demo(self,env):
        print(env)
        if "test" in env:
            print("这是测试环境")
            print((f"测试环境的ip是{env['test']}"))
        elif "dev" in env:
            print("这是开发环境")