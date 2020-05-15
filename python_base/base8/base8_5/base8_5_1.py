#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-04
# @Author     : Joey Jiang
# @File       : base8_5_1.py
# @Software   : Visual Studio Code
# @Description: python多线程处理

'''
不使用多线程
'''
import logging,_thread
from time import sleep,ctime

logging.basicConfig(level=logging.INFO)
def loop0():
    logging.info("start loop0 at "+ ctime())
    sleep(4)
    logging.info("end loop0 at "+ ctime())
def loop1():
    logging.info("start loop1 at "+ ctime())
    sleep(2)
    logging.info("end loop1 at "+ ctime())

def main():
    logging.info("start all at "+ctime())
    loop0()
    loop1()
    logging.info("end all at " +ctime())
if __name__ == "__main__":
    main()