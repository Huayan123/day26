#!/usr/bin/python3
# auther@hy
# 2022年06月29日
def set_func(func):
    def call_func(*args,**kwargs):
        print("---验证1----")
        print("---验证2----")
        func(*args,**kwargs)
    return call_func
@set_func
def test1(num,*args,**kwargs):
    print("-----tets1----%d"%num)
    print("-----test1----%d",args)
    print("-----test1----%d",kwargs)
test1(100)
test1(200,200,m=100)
