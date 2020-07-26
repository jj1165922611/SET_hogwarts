#!/usr/bin/env python
# -*- coding -*-
# @Time       : 2020-07-26
# @Author     : Joey Jiang
# @File       : bicycle.py
# @Software   : PyCharm
# @Description: 开小车

'''
写一个Bicycle（自行车）类，有run（骑行）方法，调用时显示骑行里程km（骑行里程为传入的数字）:

再写一个电动自行车类EBicycle继承自Bicycle，添加电池电量valume属性,通过参数传入，同时有两个方法：
    1. fill_charge(vol）用来充电，vol为电量（度） 。
    2. run(km）方法用于骑行，每骑行10km消耗电量1度，当电量消耗尽时调用 Bicycle的run方法骑行，通过传入的骑行里程数，显示骑行结果
'''

'''
自行车
'''
class Bicycle:
    def run(self,mileage):
        return mileage
'''
电动自行车
'''
class EBicycle(Bicycle):

    def __init__(self,valume=10):
        self._valume=valume
        self._total_mileage=self._valume*10

    def get_valume(self):
        return self._valume

    def fill_charge(self,vol):
        return vol

    def run(self,current_mileage):
        if self._total_mileage - current_mileage>0:
            print("电动自行车骑了:",current_mileage,"KM")
        else:
            print("电动自行车骑了:",self._total_mileage,"KM")
            print("自行车骑了:",super().run(current_mileage - self._total_mileage),"KM")

bike=EBicycle()
bike.run(101)
