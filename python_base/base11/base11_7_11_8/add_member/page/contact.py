#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-23
# @Author     : Joey Jiang
# @File       : contact.py
# @Software   : PyCharm
# @Description: Page Object演练
from selenium import webdriver
from selenium.webdriver.common.by import By


class Contact:
    def __init__(self):
        option = webdriver.ChromeOptions()
        option.debugger_address = "localhost:9222"
        self.driver = webdriver.Chrome(chrome_options=option)
        self.driver.implicitly_wait(3)
    def get_member(self):
        list = []
        while True:
            page:str=self.driver.find_element(By.CSS_SELECTOR, ".ww_pageNav_info_text").text
            current_page,total_page=page.split("/",1)
            # 6.获取成员列表的值
            member_list=self.driver.find_elements(By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)')
            for i in member_list:
                member=i.get_attribute("title")
                list.append(member)
            print(list)
            if current_page == total_page:
                break
            else:
                self.driver.find_element(By.CSS_SELECTOR,".ww_commonImg_PageNavArrowRightNormal").click()
        return list


