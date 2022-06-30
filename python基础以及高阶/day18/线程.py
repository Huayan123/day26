#!/usr/bin/python3
# auther@hy
# 2022年06月19日
from threading import Thread
import time
def print_fun():
    print("hello python")
    time.sleep(1)
if __name__=="__main__":
    for i in range(5):
        t = Thread(target=print_fun)
        t.start()