#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-09-29
# @Author     : Joey Jiang
# @File       : basepage.py
# @Software   : PyCharm
# @Description: 打造自己的测试框架
import inspect
import json

import yaml
from appium.webdriver.webdriver import WebDriver

from python_hogwarts12.appium_xueqiu_015.page.wrapper import handle_black


class BasePage:
    _params = {}
    _driver=None

    def __init__(self, driver: WebDriver = None):
        self._driver = driver
    def screenshot(self,name):
        self._driver.save_screenshot(name)
    @handle_black
    def find(self, locator, value: str=None):
        if isinstance(locator, tuple):
            ele = self._driver.find_element(*locator)
        else:
            ele = self._driver.find_element(locator, value)
        return ele

    @handle_black
    def finds(self, locator, value=None):
        if isinstance(locator, tuple):
            elements = self._driver.find_elements(*locator)
        else:
            elements = self._driver.find_elements(locator, value)
        return elements

    def steps(self, path):
        with open(path, encoding="utf-8") as f:
            name = inspect.stack()[1].function
            steps = yaml.safe_load(f)[name]
        raw = json.dumps(steps)
        for key, value in self._params.items():
            raw = raw.replace(f"{{{key}}}", value)
        steps = json.loads(raw)
        for step in steps:
            ele = None
            if "by" in step.keys():
                ele = self.find(step["by"], step["locator"])
            if "action" in step.keys():
                action = step["action"]
                if action == "click":
                    ele.click()
                if action == "text":
                    return ele.txt
                if action == "attribute":
                    return ele.get_attribute(step["value"])
                if action == "send":
                    # content: str = step["value"]
                    # for key, value in self._params.items():
                    #     content = content.replace(f"{key}", value)
                    # ele.send_keys(content)
                    ele.send_keys(step["value"])
                if action == "len > 0":
                    elements=self.finds(step["by"],step["locator"])
                    return len(elements)
