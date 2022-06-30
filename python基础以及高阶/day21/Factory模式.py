#!/usr/bin/python3
# auther@hy
# 2022年06月22日
class Animal():

    def eat(self):
        pass

    def voice(self):
        pass


class Dog(Animal):
    def eat(self):
        print('狗吃骨头')

    def voice(self):
        print('狗叫汪汪')


class Cat(Animal):
    def eat(self):
        print('猫吃鱼')

    def voice(self):
        print('猫叫喵喵')
class FactoryMode():
    def __init__(self):
        # 创建工厂
        self.Factory = {'cat':Cat,'dog':Dog}
    def create(self,animanl_name):
        # 生成对象
        return  self.Factory[animanl_name]()
f = FactoryMode()
animal = f.create('cat')
animal.eat()
animal.voice()