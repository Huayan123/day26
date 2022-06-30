#!/usr/bin/python3
# auther@hy
# 2022年06月20日
from threading import Thread,Lock
import time
num = 0
def run1(mutex:Lock):
    global num
    for i in range(10000000):
        # 加锁
        mutex.acquire()
        num += 1
        # 释放锁
        mutex.release()

def run2(mutex:Lock):
    global num
    for i in range(10000000):
        mutex.acquire()
        num += 1
        mutex.release()

if __name__=='__main__':
    mutex = Lock()
    t1 = Thread(target=run1,args=(mutex,))
    t2 = Thread(target=run2,args=(mutex,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(num)