#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-04-25
# @Author     : Joey Jiang
# @File       : util_sort.py
# @Software   : Visual Studio Code
# @Description: 排序的工具类

'''
冒泡排序每一行加注释说明
'''

'''
定义一个类，类名为UtilSort
'''


class UtilSort:

    '''
    *创建一个bubble_sort_asc方法
    *参数
        list_input: 排序前的列表
    *返回值
        l: 排序后的列表
    '''

    def bubble_sort_asc(self, list_input: list) -> list:
        # 定义变量l，将传入参数list_input的值赋给它
        l = list_input
        # 排序次数，范围是(列表的长度-1)，
        # 可以写成range(len(1)-1)或者range(1,len(1))
        for i in range(len(l)-1):
            # 对比次数，范围是(列表的长度-排序次数)，随着排序次数增加而减少，
            # 因为需要跟索引对应，所以可以写成range(len(1)-i-1)
            for j in range(len(l)-i-1):
                # 判断列表中两个相邻值前一个值是否比后一个值大
                if l[j] > l[j+1]:
                    # 将两个相邻的值进行位置交换
                    l[j], l[j+1] = l[j+1], l[j]
        # 返回排序后的列表
        return l


if __name__ == "__main__":
    print(UtilSort().bubble_sort_asc([5, 1, 3, 4, 2, 6]))
