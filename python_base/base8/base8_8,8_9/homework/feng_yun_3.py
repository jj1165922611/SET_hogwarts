#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2020-05-10
# @Author     : Joey Jiang
# @File       : feng_yun_3.py
# @Software   : Visual Studio Code
# @Description: 使用yaml改良小游戏代码
'''
游戏规则：
设定一个回合制2人对打游戏。
每个人物都有hp，power，skill

hp代表血量，power代表攻击力，
每三个回合可以使用一次skill，skill将攻击力翻倍
'''

'''
规则改为：
四个人物，随机分成两组，进行两回合比赛，每个人物获胜为本组赢得一分。比分高的组获胜，独得奖金；若比分一致，奖金平分。
每个人物都有hp，power，skill

hp代表血量，power代表攻击力，
每三个回合可以使用一次skill，skill将攻击力翻倍
'''
import yaml
import sys
import random
'''
定义一个类，类名为GameYaml
'''
class GameYaml:
    group_list1=[] # 定义一个列表group_list1，用来存放第一队的人物信息
    group_list2=[] # 定义一个列表group_list1，用来存放第二队的人物信息
    score=dict(group_core1=0,group_core2=0) # 定义一个字典score，用来存放两队的得分

    '''
    *初始化类GameYaml
    *参数
        filename: yaml文件的路径
    '''
    def __init__(self,filename):
        with open(filename,"rb") as fp:
            self.data=yaml.safe_load(fp) # 定义一个变量data，读取指定yaml文件，将文件中数据赋值给它

    '''
    *创建一个方法create_group,将四个人物进行分组
    '''
    def create_group(self):
        data=self.data # 定义一个变量data，将self.data的值赋给它
        name_list=list(data.keys()) # 定义一个变量name_list，将data的关键字强转成列表传给它
        for i in range(2): # 定义一个循环，循环次数为2，变量为i
            name=random.choice(name_list) # 定义一个变量name，从name_list列表中随机取一个值赋给它
            GameYaml.group_list1.append(name) # 将name添加到第一队的列表group_list1中
            name_list.remove(name) # 将name从name_list列表中移除
        GameYaml.group_list2=name_list # 将name_list中剩余的两个人物赋值给第一队的列表group_list2
    
    '''
    *创建一个fight方法，进行两队的pk，得出两队pk最终结果
    '''
    def fight(self):
        self.create_group()
        group_list1=GameYaml.group_list1 # 定义一个变量group_list1，将第一队group_list1列表赋值给它
        group_list2=GameYaml.group_list2 # 定义一个变量group_list2，将第一队group_list2列表赋值给它
        print("首先让我们来认识下即将pk的两支队伍，")
        print("第一队选手是{0}和{1}，".format(*group_list1))
        print("第二队选手是{0}和{1}，".format(*group_list2))
        print("让我们热烈欢迎两队选手！！！\(^o^)/~")
        print("*"*20)
        print("比赛正式开始。")
        print("现在登上pk台的选手是第一队的{}和第二队的{}".format(group_list1[0],group_list2[0]))
        round_result=self.round_info(group_list1[0],group_list2[0]) # 定义一个变量round_result，将round_info方法的返回值赋给它
        round_result["winning"]="大胜对手" if round_result["hp"] > 80 else "以较大的优势胜出" # 向字典中添加键值对，key是winning，value是根据血量判断得到的结果
        print("经过{round}轮你来我往，恭喜第{group}支队伍的{name}率先为自己的队伍夺得1分,并且{winning}".format(**round_result))
        score=self.get_score(GameYaml.score,round_result["group"]) # 定义一个变量score，将get_score的返回值传给它
        print("现在的两支队伍的得分情况是：第一队{group_core1}分，第二队{group_core2}分".format(**score))
        print("*"*20)

        print("下面进行第二轮PK")
        print("有请第一队的{}和第二队的{}".format(group_list1[1],group_list2[1]))
        round_result=self.round_info(group_list1[1],group_list2[1]) # 将round_info方法的返回值赋给变量round_result
        round_result["winning"]="大胜对手" if round_result["hp"] > 80 else "以较大的优势胜出"
        print("经过{round}轮你来我往，恭喜第{group}支队伍的{name}为自己的队伍夺得1分,并且{winning}".format(**round_result))
        score=self.get_score(GameYaml.score,round_result["group"]) # 将get_score的返回值传给变量score
        print("现在的两支队伍的得分情况是：第一队{group_core1}分，第二队{group_core2}分".format(**score))
        print("*"*20)
        if score["group_core1"]==score["group_core2"]: # 判断第一队和第二队得分是否相等
            print("恭喜两队平分今晚的100万美元大奖~~~")
        elif score["group_core1"]>score["group_core2"]: # 判断第一队得分是否高于第二队
            print("恭喜第一队胜出，赢得今晚的100万美元大奖~~~")
        else: # 判断第一队得分是否低于第二队
            print("恭喜第二队胜出，赢得今晚的100万美元大奖~~~")
    '''
    *创建一个方法round_info，进行两个人物的pk
    *参数
        role1: 人物1的名字
        role2: 人物2的名字
    *返回值
        round_result: 回合数以及胜出人物的血量，队伍名，名字
    '''
    def round_info(self,role1,role2):
        hp="hp" # 定义一个变量hp，赋值为'hp'
        power="power" # 定义一个变量power，赋值为'power'
        skill="skill" # 定义一个变量skill，赋值为'skill'
        round_num=0 # 定义一个变量round_num，赋值为0，存放回合数
        role1_power=self.data[role1][power] # 定义一个变量role1_power，赋值为人物1的攻击力
        role2_power=self.data[role2][power] # 定义一个变量role2_power，赋值为人物2的攻击力
        role1_skill=self.data[role1][skill] # 定义一个变量role1_skill，赋值为人物1的翻倍数
        role2_skill=self.data[role2][skill] # 定义一个变量role2_skill，赋值为人物2的翻倍数
        role1_hp=self.data[role1][hp] # 定义一个变量role1_hp，赋值为人物1的血量
        role2_hp=self.data[role2][hp] # 定义一个变量role2_hp，赋值为人物2的血量
        while True:
            round_num=round_num+1 # 随着循环次数的增加，回合数每次循环加1
            if round_num % 3==0: # 判断回合数是否为3
                role1_power=self.data[role1][power]*role1_skill # 将人物1的攻击力翻倍
                role2_power=self.data[role2][power]*role2_skill # 将人物2的攻击力翻倍
            else:
                role1_power=self.data[role1][power] # 将人物1的攻击力赋值给role1_power
                role2_power=self.data[role2][power] # 将人物2的攻击力赋值给role2_power
            role1_hp=role1_hp-role2_power # 人物1的剩余血量=人物1的血量-人物2的攻击力
            if role1_hp<=0: # 判断人物1的剩余血量是否小于等于0
                print(f"{role1}最终血量为:\t{role1_hp}")
                print(f"{role2}最终血量为:\t{role2_hp}")
                round_result={"hp":role2_hp,"round":round_num,"group":2,"name":role2} # 将回合数以及人物2的信息赋值给round_result
                return round_result # 返回round_result
            else:
                role2_hp=role2_hp-role1_power # 人物2的剩余血量=人物2的血量-人物1的攻击力
            if role2_hp<=0:
                print(f"{role1}最终血量为:\t{role1_hp}")
                print(f"{role2}最终血量为:\t{role2_hp}")
                round_result={"hp":role1_hp,"round":round_num,"group":1,"name":role1} # 将回合数以及人物1的信息赋值给round_result
                return round_result # 返回round_result
                
    '''
    *创建一个方法get_score，计算两队得分
    *参数 
        score: 两队得分
        group：队名
    *返回值
        score: 两队得分
    '''
    def get_score(self,score,group):
        if group==1: # 判断是否为第一队
            score["group_core1"]=score["group_core1"]+1 # 第一队的得分加1
        else: # 判断是否为第二队
            score["group_core2"]=score["group_core2"]+1 # 第二队的得分加1
        return score # 返回两队得分
if __name__ == "__main__":
    path=sys.path[0] # 获取当前文件所在绝对路径
    filename=path+"/"+"data.yml" # 定义一个变量filename，将指定yaml文件的路径赋值给它
    GameYaml(filename).fight() # 调用GameYaml类中的fight方法