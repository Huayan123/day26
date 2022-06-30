#!/usr/bin/python3
# auther@hy
# 2022年06月29日

from time import sleep,ctime
def set_func(func):
    def call_func(*args,**kwargs):
        print("%s called at %s"%(func.__name__,ctime()))
        """
        这里return的是被修饰函数打印的值,否则打印不了
        """
        return func(*args,**kwargs)
    return call_func
@set_func
def foo(num,*args,**kwargs):
    return num
print(foo(100))