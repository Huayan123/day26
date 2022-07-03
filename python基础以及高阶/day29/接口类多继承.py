#!/usr/bin/python3
# auther@hy
# 2022年07月02日
"""
接口类子类调用方法，该方法实现需要父类中也要有

"""
from abc import abstractmethod,ABCMeta
class Walk_animal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):
        pass
class Swim_animal(metaclass=ABCMeta):
    @abstractmethod
    def swim(self):
        pass


class Fly_animal(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass

"""
抽象类
子类必须要实现Swim、Walk类中的方法
"""
class Tiger(Walk_animal,Swim_animal):
    def swim(self):
        print('tiger swim')

    def walk(self):
        print('tiger walk')
t =  Tiger()
t.walk()