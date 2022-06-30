#!/usr/bin/python3
# auther@hy
# 2022年06月22日
print("多重继承使用类名.__init__发生的状态")
class People(object):
    def __init__(self,name,*args,**kwargs):
        print("parent的init开始被调用")
        self.name = name
        print('parent的init结束被调用')
class Father(People):
    def __init__(self,name,age,*args,**kwargs):
        print('Father的init开始调用')
        self.age = age
        super().__init__(name,*args,**kwargs)
        print('Father的init结束调用')
class Mother(People):
    def __init__(self,name,gender,*args,**kwargs):
        print('Mother的init开始调用')
        self.gender = gender
        super().__init__(name,*args,**kwargs)
        print('Mother的init结束调用')
class Son(Father,Mother):
    def __init__(self,name,age,gender):
        print('son的init开始调用')
        super().__init__(name,age,gender)
        print('son的init结束调用')
son1 = Son('lisi',18,'man')
print(son1.name)
print(son1.age)
print(son1.gender)
print("******多继承使用类名.__init__ 发生的状态******\n\n")