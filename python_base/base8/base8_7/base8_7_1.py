#!usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-07
# @Author     : Joey Jiang
# @File       : base8_7_1.py
# @Software   : Visual Studio Code
# @Description: python外部数据源文件处理

import json
class PracticeJson:

    def __init__(self):
        self.data="{'name':'xiaohong','age':'12'}"
    def practice_dump(self):
        with open("./demo.json","w") as fs:
            json.dump(self.data,fp=fs)
    def practice_dumps(self):
        print(type(self.data))
        print(json.dumps(self.data))
        print(type(self.data))
    def practice_load(self):
        pass
    def practice_loads(self):
        pass

if __name__ == "__main__":
    PracticeJson().practice_dumps()
    PracticeJson().practice_dump()