#!/usr/bin/python3
# auther@hy
# 2022年06月29日
import time
def set_func(func):
    def call_time():
        begin = time.time()
        func()
        end = time.time()
        print("执行时间:%f"%(end-begin))
    return call_time
@set_func
def tset1():
    print("******test1********")
    for i in range(100000):
        pass
tset1()
