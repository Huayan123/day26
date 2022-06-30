#!/usr/bin/python3
# auther@hy
# 2022年06月20日
import time
# 协程导入的包
from greenlet import greenlet
"""
生成greenlet对象，分别主动切换到另外一个协程对象上
"""
def work1():
    print('-A-')
    # switch 切换
    w2.switch()
    time.sleep(1)
def work2():
    print('-B-')
    w1.switch()
    time.sleep(1)
if __name__ == '__main__':
    w1 = greenlet(work1)
    w2 = greenlet(work2)
    w1.switch()