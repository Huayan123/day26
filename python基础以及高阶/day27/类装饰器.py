#!/usr/bin/python3
# auther@hy
# 2022年06月29日

class Test():
    """
    类装饰器
    call 函数用对象()访问
    """
    def __init__(self,func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print("call....")
        return self.func(*args,**kwargs)
@Test
def test():
    print("----test----")
test()