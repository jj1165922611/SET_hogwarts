#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-27
# @Author     : Joey Jiang
# @File       : contact.py
# @Software   : PyCharm
# @Description: 企业微信web端自动化测试实战（一）
from time import sleep

from python_base.base11.base11_7_11_8.homework.page.base_page import BasePage

class ContactPage(BasePage):
    def select_member(self,name=None):
        while True:
            # 1、得到当前页和总页数
            page_number=self.find(self.by_css_selector(),'.ww_pageNav_info_text').text
            current_page,total_page=page_number.split("/")
            # 2、得到当前页的所有姓名
            name_list=self.finds(self.by_css_selector(),"#member_list td:nth-child(2)")
            # 3、判断想选择的姓名是否在当前页
            for i in range(len(name_list)):
                if name == name_list[i].text:
                    # 4、选中被找到的那一条，并勾上复选框
                    ele=self.finds(self.by_css_selector(),"#member_list td:nth-child(1)")
                    ele[i].click()
                    return 1
            # 5、判断是否为最后一页
            if current_page == total_page:
                return 0
            else:
                # 6、点击下一页
                self.find(self.by_xpath(),'//*[@id="js_contacts66"]/div/div[2]/div/div[2]/div[3]/div[1]/div[1]/div/a[2]').click()

    def set_up_department(self,department_list=None):
        ele=self.find(self.by_xpath(),'//*[@id="js_contacts66"]/div/div[2]/div/div[2]/div[3]/div[1]/a[2]')
        ele.click()
        search_box=self.finds(self.by_css_selector(),"#memberSearchInput")
        for department in department_list:
            search_box[1].send_keys(department)
            self.find(self.by_xpath(),'//*[@id="searchResult"]/ul/li').click()
        self.find(self.by_xpath(),'//*[contains(@id,"__dialog__MNDialog") and not(contains(@style,"none"))] //*[@class="qui_btn ww_btn ww_btn_Blue js_submit"]').click()

    def get_departments(self,name=None):
        while True:
            # 1、得到当前页和总页数
            page_number = self.find(self.by_css_selector(), '.ww_pageNav_info_text').text
            current_page, total_page = page_number.split("/")
            # 2、得到当前页的所有姓名
            name_list = self.finds(self.by_css_selector(), "#member_list td:nth-child(2)")
            # 3、判断想选择的姓名是否在当前页
            for i in range(len(name_list)):
                if name == name_list[i].text:
                    # 4、选中被找到的那一条，并勾上复选框
                    ele = self.finds(self.by_css_selector(), "#member_list td:nth-child(4)")
                    return ele[i].text
            # 5、判断是否为最后一页
            if current_page == total_page:
                return 0
            else:
                # 6、点击下一页
                self.find(self.by_xpath(),
                          '//*[@id="js_contacts66"]/div/div[2]/div/div[2]/div[3]/div[1]/div[1]/div/a[2]').click()

    def select_member_fail(self, name=None):
        pass

    def set_up_department_fail(self, name=None,department_list=None):
        pass

    def get_departments_fail(self, name=None):
        pass
