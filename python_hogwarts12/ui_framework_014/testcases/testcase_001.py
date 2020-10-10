#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-10-06
# @Author     : Joey Jiang
# @File       : testcase_001.py
# @Software   : PyCharm
# @Description: pageobject改造
import pytest
import yaml

from python_hogwarts12.ui_framework_014.page.app import App
from python_hogwarts12.ui_framework_014.testcases.test_base import TestBase


class TestCase(TestBase):

    @pytest.mark.parametrize("value1,value2",yaml.safe_load(open("../testcases/testcase_001.yaml","rb")))
    def test_search(self,value1,value2):
        self.app.start().main().goto_search()