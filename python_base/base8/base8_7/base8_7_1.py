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
        self.dict={'name':'xiaohong','age':12}
    def practice_dump(self):
        print("---------------dump------------------")
        with open("demo.json","w") as fs:
            json.dump(self.dict, fp=fs)
    def practice_dumps(self):
        print("---------------dumps------------------")
        print(type(self.dict))
        print(json.dumps(self.dict))
        print(type(self.dict))
    def practice_load(self):
        print("---------------load------------------")
        with open("demo.json","r") as f:
            print(json.load(f))
    def practice_loads(self):
        print("---------------loads------------------")
        json_data=json.dumps(self.dict)
        print(type(json_data))
        print(type(json.loads(json_data)))

if __name__ == "__main__":
    PracticeJson().practice_dump()
    PracticeJson().practice_dumps()
    PracticeJson().practice_load()
    PracticeJson().practice_loads()