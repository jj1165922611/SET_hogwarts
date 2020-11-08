#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-11-08
# @Author     : Joey Jiang
# @File       : test_execute_script_demo.py
# @Software   : PyCharm
# @Description: execute_script处理js脚本
import time

from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestExecuteScriptDemo:
    _url="https://www.baidu.com"
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
    def teardown(self):
        self.driver.quit()
    def test_execute_script_scroll(self):
        '''
        Demo1：滚动到底部
        :return:
        '''
        #1、进入百度首页
        self.driver.get(self._url)
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located((By.ID,"kw")))
        #2、在搜索框中输入"我是谁"
        self.driver.find_element_by_id("kw").send_keys("我是谁")
        #3、点击百度一下
        self.driver.find_element_by_id("su").click()
        #4、滚动到底部
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        #5、点击下一页
        self.driver.find_element_by_link_text("下一页 >").click()

    def test_execute_script_return(self):
        '''
        return返回JS执行结果
        :return:
        '''
        #1、进入百度首页
        self.driver.get(self._url)
        #2、return返回页面的title和加载时间
        for code in (
            ["return document.title","return JSON.stringify(performance.timing)"]
        ):
            print(self.driver.execute_script(code))
    def test_execute_script_time_control(self):
        '''
        处理时间控件
        :return:
        '''
        #1、进入12306首页
        self.driver.get("https://www.12306.cn/index/")
        #2、移除时间控件的readonly属性
        self.driver.execute_script("document.getElementById('train_date').readOnly=false")
        time.sleep(3)
        #3、将时间修改为2020-11-23
        self.driver.execute_script(f"document.getElementById('train_date').value='2020-11-23'")
        time.sleep(3)
        #4、取出值，查看是否修改成功
        result=self.driver.execute_script("return document.getElementById('train_date').value")
        assert result=='2020-11-23'