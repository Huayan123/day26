#!/usr/bin/python3
# auther@hy
# 2022年06月19日
import time
from multiprocessing import Process
import os
def get_process_pid():
    print("当前进程的pid号:pid = %d"%os.getpid())
    while True:
        time.sleep(1)

if __name__ == '__main__':
    process = Process(target=get_process_pid)
    print("-"*50)
    print("当前进程的pid号：pid=%d"%os.getpid())
    process.start()
    # 主动中止
    process.terminate()
    time.sleep(3)
    # 主动将进程回收
    process.join()
    time.sleep(5)
