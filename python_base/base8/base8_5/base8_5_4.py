#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-06
# @Author     : Joey Jiang
# @File       : base8_5_4.py
# @Software   : Visual Studio Code
# @Description: python多线程处理

import logging
from time import sleep,ctime
import threading
logging.basicConfig(level=logging.INFO)
def loop0():
    logging.info("start loop0 at "+ctime())
    sleep(2)
    logging.info("end loop0 at "+ctime())
def loop1():
    logging.info("start loop1 at "+ctime())
    sleep(4)
    logging.info("end loop1 at "+ctime())
def main():
    logging.info("start all at "+ctime())
    t1=threading.Thread( target=loop0)
    t1.start()
    t2=threading.Thread(None,loop1)
    t2.start()
    t1.join()
    # t2.join()
    print(t1.getName())
    print(t2.getName())
    print(t1.is_alive())
    logging.info("end all at "+ctime())
    sleep(2.1)
    print(t1.is_alive())
if __name__ == "__main__":
    main()