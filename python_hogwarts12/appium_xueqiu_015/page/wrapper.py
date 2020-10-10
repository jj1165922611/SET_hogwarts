#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-10-10
# @Author     : Joey Jiang
# @File       : wrapper.py
# @Software   : PyCharm
# @Description: 打造自己的测试框架
from appium.webdriver.common.mobileby import MobileBy




def handle_black(method):
    def inner(*args,**kwargs):
        _error_num = 0
        _max_num = 5
        _black_list = [
            (MobileBy.XPATH, '//*[@text="确定"]'),
            (MobileBy.XPATH, '//*[@text="下次再说"]')
        ]
        try:
            from python_hogwarts12.appium_xueqiu_015.page.basepage import BasePage
            isinstance:BasePage=args[0]
            ele=method(*args,**kwargs)
            _error_num=0
            return ele
        except Exception as e:
            if _error_num>_max_num:
                raise e
            _error_num+=1
            for black in _black_list:
                eles=isinstance._driver.find_elements(*black)
                if len(eles)>0:
                    eles.click()
                    return isinstance.inner(*args,**kwargs)
            raise e
        return inner





