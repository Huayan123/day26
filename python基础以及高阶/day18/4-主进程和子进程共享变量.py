#!/usr/bin/python3
# auther@hy
# 2022年06月19日
import os
from multiprocessing import Process
import time
list1 = [1,2]
def fun1():
    list1.append(3)
    list1.pop(0)
    time.sleep(1)
    print(list1)
    print("当前进程的pid号:pid1 = %d,list1 = %s"%(os.getpid(),list1))
def fun2():
    for i in range(3):
        list1.append(i)
        time.sleep(1)
    print("当前进程的pid号:pid2 = %d,list1 = %s" %(os.getpid(),list1))
if __name__ == '__main__':
        p1 = Process(target=fun1)
        p1.start()
        print("-"*50)
        time.sleep(1)
        p2 = Process(target=fun2)
        p2.start()
        time.sleep(1)
        print("-"*50)
        print(list1)