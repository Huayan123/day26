#!/usr/bin/python3
# auther@hy
# 2022年06月30日
class Set_Foo(type):
    def __new__(cls,class_name,class_parents,class_attr):
        new_dict = {}
        for key,values in class_attr.items():
            if not key.startswith('__'):
                new_dict[key.upper()]=values
        # 创建对象
        return type(class_name,class_parents,new_dict)


class Foo(object,metaclass=Set_Foo):
    bar = 'python'
print(hasattr(Foo,'BAR'))