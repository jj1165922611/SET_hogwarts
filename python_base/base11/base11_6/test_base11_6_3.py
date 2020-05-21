#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-21
# @Author     : Joey Jiang
# @File       : test_base11_6_3.py
# @Software   : PyCharm
# @Description: 企业微信的自动化登录

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
class TestCookie:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com")
    def test_set_cookie(self):
        '''
        获取cookie
        :return:
        '''
        cookies=[{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688849970736763'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'd_TXqVXFnCIvNltINh-FNfxiCC_BrMzudVj05rAvkkJrVdGE9_Lm2gpi1MHOMZnQAKX7EzgpZ3LhGCVR6cocQXASVPHKV7uiiT71d_7EEPiHkNjjWRdJ_lhFbu-L7AODG2GuKnzTtUYyBQ6_fKJL4rgkQWBHQ3xGrrmDE_neKYPDriBI7M_0qp02nHbrIGw2UWrE3fzOoH2E-jx2X1MZF5BlfxChzpIGYGvHySK7qtPkBxEJiqgUxP8ML8fpWIo422n9OkmFDaUGqqWQDRioWA'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688849970736763'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325023137513'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a4599381'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.logined', 'path': '/', 'secure': False, 'value': 'true'}, {'domain': 'work.weixin.qq.com', 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '4356096147'}, {'domain': '.qq.com', 'expiry': 1590152420, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.2090135659.1590066011'}, {'domain': '.qq.com', 'expiry': 1590066070, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 1653138020, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.857841632.1590066011'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1590066011'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '140254479311388'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'bIjbJQLOecBamlfg8tGqeKidLT3RhUAqdcTn7vQ4xWQYYS9K2vt1LTL2o9HE1Bsn'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'expiry': 1621602010, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1590066011'}, {'domain': '.work.weixin.qq.com', 'expiry': 1592658020.691038, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}]
        for cookie in cookies:
            self.driver.add_cookie(cookie)