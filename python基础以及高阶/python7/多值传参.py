#!/usr/bin/python3
# auther@hy
# 2022年06月08日
def demo1(*args,**kwargs):
    print(args)
    print(kwargs)
def demo2(*args,**kwargs):
    demo1(*args[2:],**kwargs)
if __name__=='__main__':
    tuple1  = (1,2,3,4,5)
    dict1 ={'name': '小明', 'age': 18, 'gender': True}
    demo2(*tuple1,**dict1)
