#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-06-11
# @Author     : Joey Jiang
# @File       : test_label_manager.py
# @Software   : PyCharm
# @Description: 企业微信标签管理接口
import pytest
import requests

class TestLabelManager:

    def setup(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {
            "corpid": "wwaa5e12b39afbafe3",
            "corpsecret": "2_YAsegpEFFziREvf3GB5Vr2bIgAP7cBIWr35DN_b-s"
        }
        r = requests.get(url=url, params=params)
        self.token = r.json()["access_token"]
        print(r.json()["access_token"])
    @pytest.mark.parametrize("tagname,tagid",[("Testing",1),("Tetsing2",2),("Tetsing3",3)])
    def test_create_label(self,tagname,tagid):
        """
        *创建标签
        """
        url="https://qyapi.weixin.qq.com/cgi-bin/tag/create"
        params={
            "access_token": self.token,
        }
        json={
            "tagname": tagname,
            "tagid": int(tagid),
        }
        r=requests.post(url=url,params=params,json=json)
        print(r.json())
        assert r.json()['errcode']==0

    def test_update_label_name(self):
        """
        *更新标签名字
        """
        url = "https://qyapi.weixin.qq.com/cgi-bin/tag/update"
        params = {
            "access_token": self.token,
        }
        json={
            "tagname": "Testing1",
            "tagid": 1
        }
        r = requests.post(url=url, params=params,json=json)
        print(r.json())
        assert r.json()['errcode'] == 0
    def test_delete_label(self):
        """
        *删除标签
        """
        url = "https://qyapi.weixin.qq.com/cgi-bin/tag/delete"
        params = {
            "access_token": self.token,
            "tagid": 3,
        }
        r = requests.get(url=url, params=params)
        print(r.json())
        assert r.json()['errcode'] == 0

    def test_get_label_member(self):
        """
        *获取标签成员
        """
        url="https://qyapi.weixin.qq.com/cgi-bin/tag/get"
        params={
            "access_token" : self.token,
            "tagid": 1
        }
        r=requests.get(url=url,params=params)
        print(r.json())
        assert r.json()['errcode'] == 0

    def test_add_label_member(self):
        """
        *增加标签成员
        """
        url = "https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers"
        params = {
            "access_token": self.token,
        }
        json={
            "tagid": 1,
            "userlist": ["cjg1","cjg2","cjg3"],
        }
        r = requests.post(url=url, params=params,json=json)
        print(r.json())
        assert r.json()['errcode'] == 0

    def test_delete_label_member(self):
        """
        *删除标签成员
        """
        url = "https://qyapi.weixin.qq.com/cgi-bin/tag/deltagusers"
        params = {
            "access_token": self.token,
        }
        json={
            "tagid": 1,
            "userlist": ["cjg3"]
        }
        r = requests.post(url=url, params=params,json=json)
        print(r.json())
        assert r.json()['errcode'] == 0
    def test_getlist_label(self):
        """
        *获取标签列表
        """
        url = "https://qyapi.weixin.qq.com/cgi-bin/tag/list"
        params = {
            "access_token": self.token,
        }
        r = requests.get(url=url, params=params)
        print(r.json())
        assert r.json()['errcode'] == 0