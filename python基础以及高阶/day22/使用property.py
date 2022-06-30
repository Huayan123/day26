#!/usr/bin/python3
# auther@hy
# 2022年06月24日
class Foo():
    """
    nihao

    """
    def get_fun(self):
        """
        I am a function
        :return:
        """
        return 'lisi'
    fun = property(get_fun)
f = Foo()
# 类注释
print(Foo.__doc__)
print(f.get_fun)
# 方法注释
print(f.get_fun.__doc__)
