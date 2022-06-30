#!/usr/bin/python3
# auther@hy
# 2022年06月24日
class Goods:
    @property
    def price(self):
        print('@property')

    @price.setter
    def price(self,value):
        print('@price.setter')

    @price.deleter
    def price(self):
        print('@price.deleter')
g = Goods()
# 装饰器的读
g.price
# 装饰器的属性设置
g.price = 100
# 销毁装饰器
del g.price