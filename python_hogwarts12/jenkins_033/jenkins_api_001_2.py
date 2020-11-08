#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-10-25
# @Author     : Joey Jiang
# @File       : jenkins_api_001_2.py
# @Software   : PyCharm
# @Description: jenkins api接口

from jenkinsapi.jenkins import Jenkins

jk=Jenkins("http://localhost:8888","JoeyJiang","1220jj",useCrumb=True)
jk.build_job("iInterface_python")