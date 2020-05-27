#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-26
# @Author     : Joey Jiang
# @File       : util.py
# @Software   : PyCharm
# @Description: Page Object演练
import yaml

class Util:
    def get_yaml(filename):
        with open(filename,"rb") as f:
            return yaml.safe_load(f)