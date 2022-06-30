#!/usr/bin/python3
# auther@hy
# 2022年06月08日
class Women():
    def __init__(self,name):
        self.name = name
        self._height = 166
        self.__age = 20
    def __sercret(self):
        print("我的年龄%d"%self.__age)
    def boy_friend(self):
        self.__sercret()
xiaofang  = Women('小芳')
xiaofang.boy_friend()