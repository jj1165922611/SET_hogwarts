#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-06-28
# @Author     : Joey Jiang
# @File       : test_base23_4_1.py
# @Software   : PyCharm
# @Description: H5性能分析
from selenium import webdriver


class TestH5:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.baidu.com")
    def test_H5(self):
        time="return JSON.stringify(window.performance.getEntriesByName(document.querySelector('img').src)[0],null,2)"
        print(self.driver.execute_script(time))
    def teardown(self):
        self.driver.quit()