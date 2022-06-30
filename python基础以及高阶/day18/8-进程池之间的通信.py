#!/usr/bin/python3
# auther@hy
# 2022年06月19日
import os,time
from multiprocessing import Pool,Manager
def reader(q):
    print("子进程的pid=%d,父进程的ppid=%d" % (os.getpid(),os.getppid()))
    for i in range(q.size()):
        print("从Queue中读取到的消息:%s" % q.get(True))

def writer(q):
    print("子进程的pid=%d,父进程的ppid=%d" % (os.getpid(),os.getppid()))
    for i in 'kaoyan':
        q.put(i)
    time.sleep(2)
if __name__=='__main__':
    q = Manager().Queue()
    pl = Pool()
    pl.apply_async(writer,(q,))
    time.sleep(1)
    pl.apply_async(reader,(q,))
    pl.close()
    pl.join()
    print("进程pid:%s 结束.."%os.getpid())