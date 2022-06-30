#!/usr/bin/python3
# auther@hy
# 2022年06月20日
from gevent import monkey
import time
import gevent
def coroutine_work(coroutine_name):
    for i in range(10):
        print(coroutine_name,i)
        time.sleep(0.5)
if __name__ == "__main__":
    gevent.joinall([gevent.spawn(coroutine_work,'work1'),gevent.spawn(coroutine_work,'work2')])

