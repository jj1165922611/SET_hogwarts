#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-08-19
# @Author     : Joey Jiang
# @File       : base.py
# @Software   : PyCharm
# @Description: 企业微信移动app实战
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self,driver:WebDriver=None):
        self._driver=driver

    _black_list=[
        (MobileBy.ID,'tv_agree'),
        (MobileBy.ID,'image_cancel'),
        (MobileBy.XPATH,"//*[@text='下次再说']"),
        (MobileBy.XPATH,"//*[@text='确定']"),
    ]
    _error_num=0
    _find_maxnum=5

    def find(self,locator,value):
        try:
            if isinstance(locator,tuple):
                element=self._driver.find_element(*locator)
            else:
                element=self._driver.find_element(locator.value)
            # 如果成功，清空错误计数
            self._error_num=0
            return element
        except Exception as e:
            # 如果次数太多，就退出异常逻辑，直接报错
            if self._find_num>self._find_maxnum:
                raise e
            # 记录一直异常次数
            self._error_num+=1
            # 对黑名单里的弹框进行处理
            for ele in self._black_list:
                ele_list=self._driver.find_elements(*ele)
                if len(ele_list)>0:
                    ele_list[0].click()
                    # 继续寻找原来的正常控件
                    return self.find(locator,value)
            # 如果黑名单也没有，就报错
            raise e

