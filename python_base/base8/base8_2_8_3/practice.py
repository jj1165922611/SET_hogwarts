#!/usr/bin/env python
# -*- coding -*-
# @Time       : 2020-07-26
# @Author     : Joey Jiang
# @File       : practice.py
# @Software   : PyCharm
# @Description: 练习

'''
给你一个整数数组nums，请你返回其中位数为偶数的数字的个数．
    示例1：
        输入：nums = [12,345,2,6,7896]
        输出：2
        解释：
            12是2位数字（位数为偶散） 345是3位敌字（位数为奇数） 2是1位数字（位数为奇数） 6是1位数字位数为奇数） 7896足4位数字《位数为偶数）
            因此只有，12和7896是位敖为偶数的数字
    示例2:
        输入：nums = [555,901,482,17711,1]
        输出：1
        解释：
            只有1771是位数为偶数的数字。
提示：
1<= nums. length＜= 500
1<= nums[i] <= 10^5
'''
def even_number_digits(nums:list)->int:
    count=0
    for i in nums:
        if len(str(i)) % 2==0:
           count+=1
    return count

nums=[1,233,4444,6666,777,98,111100]
print(even_number_digits(nums))