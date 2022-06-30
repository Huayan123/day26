#!/usr/bin/python3
# auther@hy
# 2022年06月11日
class Stack:
    def __init__(self):
        self.stack = []
    def push(self,ele):
        self.stack.append(ele)
    def pop(self):
        self.stack.pop()
    def top(self):
        if self.empty():
            return "stack is empty"
        else:
            return self.stack[-1]
    def empty(self):
        return self.stack == []
    def size(self):
        return len(self.stack)
if __name__=="__main__":
   s = Stack()
   s.push(1)
   s.push(2)
   s.push(3)
   s.push(4)
   s.pop()
   s.size()
   print(s.stack)