#!/usr/bin/python3
# auther@hy
# 2022年06月20日
from gevent import monkey
import gevent
monkey.patch_all()
def f(n):
    for i in range(n):
        # 获取当前协程号
        print(gevent.getcurrent(),i)
        gevent.sleep(1)
if __name__ =='__main__':
    # 协程自动切换
    g1 = gevent.spawn(f,5)
    g2 = gevent.spawn(f,5)
    g3 = gevent.spawn(f,5)
    g1.join()
    g2.join()
    g3.join()