#!/usr/bin/python3
# auther@hy
# 2022年06月08日

class Printer():
    """

    单列模式：类对象一直是new出来的对象

    """
    isinstance = None
    def __new__(cls, *args, **kwargs):
        if cls.isinstance is None:
            cls.isinstance = super().__new__()
            return cls.isinstance
        return cls.isinstance
    def __init__(self,name):
        print("初始化："+name)

printer1 = Printer("惠普")

printer2 = Printer("联想")

print(printer1 is printer2)
# python的引用技术
# 挂标签
