#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-10-10
# @Author     : Joey Jiang
# @File       : wrapper.py
# @Software   : PyCharm
# @Description: 打造自己的测试框架
import logging

import allure
from appium.webdriver.common.mobileby import MobileBy


def handle_black(method):
    logging.basicConfig(level=logging.INFO)

    def inner(*args, **kwargs):
        _error_num = 0
        _max_num = 5
        _black_list = [
            (MobileBy.XPATH, '//*[@text="同意"]'),
            (MobileBy.XPATH, '//*[@text="确定"]'),
            (MobileBy.XPATH, '//*[@text="确认"]'),
            (MobileBy.XPATH, '//*[@text="下次再说"]')
        ]
        from python_hogwarts12.appium_xueqiu_015.page.basepage import BasePage
        instance: BasePage = args[0]
        try:
            logging.info("run" + method.__name__ + "\n args: \n" + repr(args[1:]) + "\n" + repr(kwargs))
            ele = method(*args, **kwargs)
            _error_num = 0
            return ele
        except Exception as e:
            instance.implicitly_wait(1)
            logging.error("element not found,handle black list")
            instance.screenshot("tmp.png")
            with open("tmp.png", "rb") as f:
                content = f.read()
            allure.attach(content, attachment_type=allure.attachment_type.PNG)
            if _error_num > _max_num:
                raise e
            _error_num += 1
            for black in _black_list:
                elements = instance.finds(*black)
                if len(elements) > 0:
                    elements[0].click()
                    instance.implicitly_wait(5)
                    return inner(*args, **kwargs)
            raise e

    return inner
