  # !/usr/bin/python3
# auther@hy
# 2022年06月24日
class Foo():
    """
    property实现读写分离
    """
    def func(self):
        print("I am func")
    @property
    # 装饰器，返回的只能读
    def prop(self):
        return 100
f = Foo()
print(f.prop)
f.func()
