#!/usr/bin/python3
# auther@hy
# 2022年06月08日
class Dog:
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳的玩耍..." % self.name)
class XiaoTianQuan(Dog):
    def game(self):
        print("%s 飞到天上玩耍..."%self.name)
class Person:
    def __init__(self,name):
        self.name = name
    def game_with_dog(self,dog):
        print("%s 与 %s 一起快乐的玩耍..."%(self.name,dog.name))
        dog.game()
wangcai = XiaoTianQuan("哮天犬")
xaioming = Person('小明')
xaioming.game_with_dog(wangcai)