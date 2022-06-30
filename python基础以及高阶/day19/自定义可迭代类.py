#!/usr/bin/python3
# auther@hy
# 2022年06月20日
from collections.abc import Iterable,Iterator
class MyIterator(object):
    def __init__(self,mylist):
        self.mylist = mylist
        self.currernt = 0
    def __iter__(self):
        return self
    """
    可迭代器多了个next
    """
    def __next__(self):
        if self.currernt < len(self.mylist.container):
            item = self.mylist.container[self.currernt]
            self.currernt +=1
            return item
        else:raise StopIteration
class MyList(object):
    def __init__(self):
        self.container = []
    def __iter__(self):
       myiter = MyIterator(self)
       return myiter
    def add(self,item):
        self.container.append(item)
mylist = MyList()
mylist.add(1)
mylist.add(2)
mylist.add(3)
print(isinstance(mylist,Iterable))
print(isinstance(iter(mylist),Iterator))
print(isinstance([],Iterator))
print("-"*50)
iter_list = iter(mylist)
print("-"*50)
for i in mylist:
    print(i)
