#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-06
# @Author     : Joey Jiang
# @File       : base8_5_5.py
# @Software   : Visual Studio Code
# @Description: python多线程处理

'''
构造线程的另一种方法，继承thread类，并重写run()方法，在run()方法中定义具体要执行的任务
'''
import logging
import threading
from time import sleep,ctime
logging.basicConfig(level=logging.INFO)

class MyThread(threading.Thread):
    def __init__(self,func):
        threading.Thread.__init__(self)
        self.func=func
    def run(self):
        self.func()

def loop0():
    logging.info("start loop0 at "+ctime())
    sleep(2)
    logging.info("end loop0 at "+ctime())
def loop1():
    logging.info("start loop1 at "+ctime())
    sleep(2)
    logging.info("end loop1 at "+ctime())
def main():
    logging.info("start all at "+ctime())
    t1=MyThread(loop0)
    t2=MyThread(loop1)
    t1.start()
    t2.start()
    t1.join()
    # t2.join()
    logging.info("end all at "+ctime())

if __name__ == "__main__":
    main()