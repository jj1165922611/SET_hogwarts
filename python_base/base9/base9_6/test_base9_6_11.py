#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-18
# @Author     : Joey Jiang
# @File       : test_9_6_11.py
# @Software   : Pycharm
# @Description: 测试报告美化与定制

import pytest,allure,time
from selenium import  webdriver

@allure.testcase("www.baidu.com","测试用例")
@allure.feature("百度搜索")
@pytest.mark.parametrize("test_data",["allure","pytest","unittest"])
def test_steps_demo(test_data):
    with allure.step("打开百度首页"):
        driver = webdriver.Chrome()
        driver.get("https://www.baidu.com")
        driver.maximize_window()
    with allure.step(f"输入搜索词：{test_data}"):
        driver.find_element_by_id("kw").send_keys(test_data)
    time.sleep(2)
    with allure.step("点击搜索框"):
        driver.find_element_by_id("su").click()
    time.sleep(2)
    with allure.step("保存图片"):
        driver.save_screenshot("result/a.png")
        allure.attach.file("result/a.png","网页保存图片",attachment_type=allure.attachment_type.PNG)
    with allure.step("关闭浏览器"):
        driver.quit()
