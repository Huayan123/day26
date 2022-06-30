#!/usr/bin/python3
# auther@hy
# 2022年06月30日
class Objectclass(object):
    pass
def echo(obj):
    print(obj)
    obj.new_attribute = 'foo'
    print(obj())
print(Objectclass)
print(Objectclass.new_attribute)
print(hasattr(Objectclass,'new_attribute'))
