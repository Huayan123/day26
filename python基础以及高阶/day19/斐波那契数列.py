#!/usr/bin/python3
# auther@hy
# 2022年06月20日
from collections.abc import Iterator
class FibonaqieIter(object):
    def __init__(self,n):
        self.n = n
        self.current = 0
        self.num1 = 0
        self.num2 = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < self.n:
            self.num = self.num1
            self.num1,self.num2 = self.num2 , self.num1+self.num2
            self.current += 1
            return self.num
        else:
            raise StopIteration
if __name__ == '__main__':
    f = FibonaqieIter(8)
    for i in f:
        print(i)