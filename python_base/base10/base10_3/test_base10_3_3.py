#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-23
# @Author     : Joey Jiang
# @File       : test_base10_3_3.py
# @Software   : PyCharm
# @Description: selenium用例编写
'''
第一步，导入WebDriver包
第二步，调用WebDriver中的Chrome()方法启动ChromeDriver
第三步，调用get()方法打开浏览器输入网址
第四步，在页面中查找显示为“社团”的链接并点击
第五步，在页面中查找显示为“霍格沃兹测试学院”的链接并点击
第六步，在页面中查找显示为“绝对路径”的链接并打印text

注意：网络卡顿时元素可能找不到，隐式等待只对find_element和find_elements生效
'''
import time

from selenium import webdriver

class TestTesterHome:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()
    def test_case(self):
        self.driver.get("https://testerhome.com/")
        self.driver.find_element_by_link_text("社团").click()
        self.driver.find_element_by_link_text("霍格沃兹测试学院").click()
        el=self.driver.find_element_by_xpath("//div[@id='main']/div/div/div/div/div/div[2]/div/a")
        print(el.text)