#!/usr/bin/env python
# -*-coding: utf-8 -*-
# @Time       : 2020-04-28
# @Author     : Joey Jiag
# @File       : jira.py
# @Software   : Visual Studio Code
# @Description: jira类

'''
定义一个类，类名为Jira
'''


class Jira:
    '''
    *初始化Jira类
    *参数
        project_name: 项目名称
        issue_name: 问题名称
        work_flow_name: 工作流名称
        screen_name: 界面名称
    '''

    def __init__(self, project_name, issue_name, work_flow_name, screen_name):
        self.project_name = project_name  # 定义一个类变量project_name，将参数project_name的值传给它
        self.issue_name = issue_name  # 定义一个类变量issue_name，将参数issue_name的值传给它
        # 定义一个类变量work_flow_name，将参数work_flow_name的值传给它
        self.work_flow_name = work_flow_name
        self.screen_name = screen_name  # 定义一个类变量screen_name，将参数screen_name的值传给它

    '''
    *创建一个create_project()方法
    '''

    def create_project(self):
        print(f"创建名称为{self.project_name}的项目")

    '''
    *创建一个create_issue()方法
    '''

    def create_issue(self):
        print(f"创建名称为{self.issue_name}的问题")

    '''
    *创建一个project_issue_link()的方法
    '''

    def project_issue_link(self):
        print("将{0}问题关联到{1}项目中".format(self.issue_name, self.project_name))


if __name__ == "__main__":
    # 实例化Jira类，项目名称为XQ，问题名称为test_case，工作流名称为work_flow_test_case
    # 界面名称为screen_test_case
    jira = Jira("XQ", "test_case", "work_flow_test_case", "screen_test_case")
    print(f"项目的名称为{jira.project_name}")
    print("问题的名称为%s" % jira.issue_name)
    print("工作流的名称为{}".format(jira.work_flow_name))
    print("界面的名称为{0}".format(jira.screen_name))
    jira.create_project()  # 调用Jira类中create_project方法
    jira.create_issue()  # 调用Jira类中create_issue方法
    jira.project_issue_link()  # 调用Jira类中project_issue_link方法
