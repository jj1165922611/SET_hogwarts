#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020/11/21 8:14
# @Author     : Joey Jiang
# @File       : app.py
# @Software   : PyCharm
# @Description: po封装
'''
app.py 存放app一些特有的操作
比如：启动应用，关闭应用，重启应用，进入到首页
'''

from appium import webdriver

from python_hogwarts_base2.base24_6.page.basepage import BasePage
from python_hogwarts_base2.base24_6.page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver is None:
            desired_caps={}

            self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
        else:
            # self.driver.start_activity(app_package=,app_activity=) # 启动任何应用
            self.driver.launch_app() # 启动desired_caps里面设置的app
        return self
    def stop(self):
        pass
    def restart(self):
        pass
    def goto_main(self):
        '''
        跳转到首页
        :return:
        '''
        return MainPage()
