#!/usr/bin/python3
# auther@hy
# 2022年07月02日
from abc import ABCMeta,abstractmethod
class Walk_animal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):
        pass
    @abstractmethod
    def sleep(self):
        pass
class Swim_animal(metaclass=ABCMeta):
    @abstractmethod
    def swim(self):
        pass
    @abstractmethod
    def sleep(self):
        pass
animal = Walk_animal()
animal.walk()
