#!/usr/bin/python3
# auther@hy
# 2022年06月29日
from functools import wraps
def set_func(func):
    # 打印被装饰函数的名字和备注
    @wraps(func)
    def call_func():
        """
        I am call_func
        :return:
        """
        print("calling call_func")
        func()
    return call_func
@set_func
def test():
    """
    I am test
    """
    print(test.__name__,test.__doc__)
test()