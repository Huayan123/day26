#!/usr/bin/python3
# auther@hy
# 2022年06月29日
from time import ctime
def set_func(pre = ''):
    def warpped_func(func):
        def call_func(*args,**kwargs):
            print("%s called at %s %s"%(func.__name__,ctime(),pre))
            return func(*args,**kwargs)
        return call_func()
    return warpped_func
@set_func('wangdao')
def foo(*args,**kwargs):
    print("I am foo")