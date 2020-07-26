#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-04-28
# @Author     : Joey Jiang
# @File       : base8_4.py
# @Software   : Visual Studio Code
# @Description: python标准库

import os
import time
import urllib.request
import math

# os
print("--------------------os-----------------------")
os.mkdir("a")
if os.path.exists("a"):
    os.removedirs("a")
    os.mkdir("a")
    print(os.getcwd())
    print(os.listdir("./"))
if not os.path.exists("d"):
    os.mkdir("d")
if not os.path.exists("d/test.txt"):
    f = open("d/test.txt", "w")
    f.write("1111")
    f.close()

# time
print("--------------------time-----------------------")
print(time.time())
time.sleep(1)
print(time.localtime())
print(time.asctime())
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 获取两天前的时间
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()-60*60*24*2)))


# urllib
print("--------------------urllib-----------------------")
response=urllib.request.urlopen("http://www.baidu.com")
print(response.status)
# print(response.read())
print(response.headers)

# math
print("--------------------math-----------------------")
print(math.ceil(3.111))
print(math.floor(3.11))
print(math.sqrt(9))
