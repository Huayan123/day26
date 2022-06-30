#!/usr/bin/python3
# auther@hy
# 2022年06月24日
class Province:
    country = '中国'

    def __init__(self, name,count):
        self.name = name
        self.count=count
    def __call__(self, *args, **kwargs):
        print('I am call')
        print(args)
    def func(self,*args):
        print('func')
# 获取类的属性
print(Province.__dict__)
# 获取对象的属性
p = Province('台湾',3000)
print("-"*50)
p('lisi')
print(p.__dict__)