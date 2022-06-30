#!/usr/bin/python3
# auther@hy
# 2022年06月29日
from time import sleep,ctime
def timefunc(func):
    def wrapped_func(a,b):
        print("%s called at %s"%(func.__name__,ctime()))
        func(a,b)
        print(a,b)
    return wrapped_func
# 被装饰函数带有参数
@timefunc
def foo(a,b):
    print(a+b)
foo(2,3)