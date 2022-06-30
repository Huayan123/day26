#!/usr/bin/python3
# auther@hy
# 2022年06月20日
import threading
from threading import Thread
from time import ctime,sleep
def sing():
    for i in range(5):
        print("%d is sing"%i)
        sleep(1)
def dance():
    for i in range(3):
        print("%d is dance"%i)
    sleep(1)
if __name__ == '__main__':
    print("---开始时间----%s"%ctime())
    t1 = Thread(target=sing)
    t2 = Thread(target=dance)
    t1.start()
    t2.start()
    while True:
        length = len(threading.enumerate())
        print('当前运行的线程数为:%d'%length)
        if length<1:
            break
        sleep(1)