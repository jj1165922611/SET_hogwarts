#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-05
# @Author     : Joey Jiang
# @File       : base8_5_3.py
# @Software   : Visual Studio Code
# @Description: python多线程处理

import logging
from time import ctime,sleep
import _thread
logging.basicConfig(level=logging.INFO)
def loop0(lock):
    logging.info("start loop0 at "+ ctime())
    sleep(2)
    logging.info("end loop0 at " + ctime())
    lock.release()
def loop1(lock):
    logging.info("start loop1 at "+ ctime())
    sleep(2)
    logging.info("end loop1 at " + ctime())
    lock.release()
def main():
    logging.info("start all at "+ ctime())
    lock0=_thread.allocate_lock()
    lock0.acquire()
    lock1=_thread.allocate_lock()
    lock1.acquire()
    _thread.start_new_thread(loop0,(lock0,))
    _thread.start_new_thread(loop1,(lock1,))
    while lock0.locked():pass
    while lock1.locked():pass
    logging.info("end all at "+ ctime())
if __name__ == '__main__':
    main()
