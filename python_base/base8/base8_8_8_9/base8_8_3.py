#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-10
# @Author     : Joey Jiang
# @File       : base8_8_3.py
# @SOftware   : Visual Studio Code
# @Description: python外部源文件处理（二）
'''
打印各种纯量
'''

import yaml
print(yaml.safe_load(open("data.yml",'rb')))