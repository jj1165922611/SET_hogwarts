#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-10
# @Author     : Joey Jiang
# @File       : base8_8_2.py
# @SOftware   : Visual Studio Code
# @Description: python外部源文件处理（二）
import yaml

'''
data=[1,2,3]
with open("demo.yml","w") as fp:
    yaml.dump(data,fp)
'''

print(yaml.safe_load(open("demo.yml")))

data='''
companies:
    -
        id: 1
        name: company1
        price: 200W
    -
        id: 2
        name: company2
        price: 500W
'''
print(yaml.safe_load(data))