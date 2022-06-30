#!/usr/bin/python3
# auther@hy
# 2022年06月28日
"""
装饰器的顺序：
就近的先装饰但最后执行

"""
def fun1(func):
    def call_func():
        return "<b>"+func()+"</b>"
    return call_func
@fun1
def test1():
    return "test1"

def fun2(func):
    def s_func():
        return  "<i>"+func()+"</i>"
    return s_func
@fun2
def test2():
    return "test2"
@fun1
@fun2
def test3():
    return "test2"
print(test1())
print(test2())
print(test3())