#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-10-10
# @Author     : Joey Jiang
# @File       : search.py
# @Software   : PyCharm
# @Description: 打造自己的测试框架
from appium.webdriver.common.mobileby import MobileBy

from python_hogwarts12.appium_xueqiu_015.page.basepage import BasePage


class Search(BasePage):
    def search(self):
        self.find(MobileBy.ID,"com.xueqiu.android:id/search_input_text").send_keys("alibaba")
        self.find(MobileBy.XPATH,"//*[@text='BABA']").click()
        self.find(MobileBy.XPATH,'//*[@resource-id="com.xueqiu.android:id/ll_stock_item_container"]//*[@text="阿里巴巴"]/../..//*[@text="加自选"]').click()
        return self
    def get_toast(self):
        text=self.find(MobileBy.XPATH,"//*[@text='已关注']").text
        return text