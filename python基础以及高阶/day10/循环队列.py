#!/usr/bin/python3
# auther@hy
# 2022年06月11日
from collections import deque

def use_deque():
    """
    使用双端的队列
    增删改查
    :return:
    """
    queue = deque([1,2,3,4])
    queue.append(5)
    queue.popleft()
    print(queue)
if __name__ == "__main__":
    use_deque()
class Circle_Queue:
    def __init__(self,maxsize):
        """
        生成队列
        定义最大值
        :param maxsize:
        """
        self.front = 0
        self.rear = 0
        self.maxsize = maxsize
        self.arr = [0]*maxsize
    def enqueue(self,ele):
        """
        判断循环队列是否为满
        :return:
        """
        arr = self.arr
        if (self.front-self.rear+1)%self.maxsize==0:
            return "队列满了"
        arr[self.rear]=ele
        self.rear = (self.rear+1)%self.maxsize
        return True
    def dequeue(self):
        """
        判断队列是否为空
        :return:
        """
        arr = self.arr
        if self.rear == self.front:
            return "队列空"
        ele = arr[self.front]
        self.front = (self.front+1)%self.maxsize
        return ele
if __name__ == "__main__":
    queue1 = Circle_Queue(6)
    queue1.enqueue(1)
    queue1.enqueue(3)
    queue1.enqueue(4)
    queue1.enqueue(6)
    queue1.enqueue(7)
    print(queue1.dequeue())