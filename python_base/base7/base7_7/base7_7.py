#!/usr/bin/env python
# -*-coding: utf-8 -*-
# @Time       : 2020-04-24
# @Author     : Joey Jiang
# @File       : base7_7.py
# @Software   : Visual Studio Code
# @Description: python输入与输出

import json
# 1、字面量插值
name = "Joey"
age = 20
salary = 5000.133
list_a = ["Joey", 20, 5000.133]
dict_a = dict(name=name, age=age, salary=salary)
dict_b = {"name": name, "age": age, "salary": salary}
# %
print("my name is %s, my age is %d, my salary is %.2f" % (name, age, salary))
# str.format()
c = "my name is {}, my age is {}, my salary is {}" # 字符串
d = "my name is {0}, my age is {1}, my salary is {2}" # 列表
e = "my name is {name}, my age is {age}, my salary is {salary}" # 字典
print(c.format(name, age, salary))
print(d.format(*list_a))
print(e.format(**dict_a))
print(e.format(**dict_b))
# F-String，python3.6以后才出现
print(f"my name is {name}, my age is {list_a[1]}, my salary is {dict_a.get('salary')+1000}")

# 2、文件读取

file=open("file7_7.txt")
print(file.read())
file.close()
file=open("file7_7.txt")
print(file.readline())
file.close()
file=open("file7_7.txt")
print(file.readlines())
file.close()

with open("file7_7.txt") as f :
    while True:
        line =f.readline()
        if line:
            print(line)
        else:
            break

# 3、Json
str_a='{"name":"小明","age":20,"salary":100}'
json_a=json.loads(str_a)
print(json_a)
str_b=json.dumps(json_a,sort_keys=True,indent=4,ensure_ascii=False)
print(str_b)
str_c=json.dumps(json_a)
print(str_c)
json.dump(json_a,open("json7_7.json","w"),ensure_ascii=False)

json_b=json.load(open("json7_7.json","r"))
print(json_b)
print(json_b.get("name"))