#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-05
# @Author     : Joey Jiang
# @File       : base8_5_2.py
# @Software   : Visual Studio Code
# @Description: python多线程处理

'''
使用_thread运行多线程，但不守护
注意：32行的sleep(6)必须要加，因为_thread没有守护线程的机制，一旦主线程执行结束，子线程无论执行与否也就结束了。当然使用锁可以解决这个问题
'''
import _thread
from time import sleep,ctime
import logging

logging.basicConfig(level=logging.INFO)

def loop0():
    logging.info("start loop0 at "+ctime())
    sleep(4)
    logging.info("end loop0 at " + ctime())

def loop1():
    logging.info("start loop1 at "+ctime())
    sleep(2)
    logging.info("end loop1 at " + ctime())

def main():
    logging.info("start all at "+ctime())
    _thread.start_new_thread(loop0,())
    _thread.start_new_thread(loop1,())
    # sleep(6)
    logging.info("end all at "+ctime())

if __name__=="__main__":
    main()