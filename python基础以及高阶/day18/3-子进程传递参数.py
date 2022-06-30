#!/usr/bin/python3
# auther@hy
# 2022年06月19日
from multiprocessing import Process
import os
import time
def get_process_pid(name,**kwargs):
    # print("当前进程的pid号:pid = %d"%os.getpid())
    print(kwargs)
    while True:
        time.sleep(1)
if __name__ == '__main__':
    process = Process(target=get_process_pid,args=('lisi',),kwargs={'m':3})
    print("-"*50)
    # print("当前进程的pid号：pid=%d"%os.getpid())
    process.start()
