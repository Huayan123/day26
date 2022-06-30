#!/usr/bin/python3
# auther@hy
# 2022年06月14日
from  operator import itemgetter,attrgetter
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        """
        返回不是字符串类型
        :return:
        """
        return repr((self.name,self.grade,self.age))
student_lists =[
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]

student_tuples = [

    ('jone', 'B', 12),
    ('dave', 'B', 10),
    ('jahn', 'A', 15),
]
# sorted排序不改变原对象
print(sorted(student_lists,key=attrgetter('age')))
# 按照属性排序
print('-'*50)
# 按照下标排序，故是列表
print(sorted(student_tuples,key=itemgetter(1)))
print('-'*50)
# 隐匿函数实现sorted
print(sorted(student_tuples,key=lambda s:s[0]))
print('-'*50)
# 多层排序，先按姓名再按name排序
print(sorted(student_lists,key=attrgetter('name','age')))