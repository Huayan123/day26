#!/usr/bin/python3
# auther@hy
# 2022年06月19日
from multiprocessing import Queue,Process
import time
def writer1(q:Queue):
    for i in ['A','B','C']:
        q.put(i)
    print("writer写完")
    time.sleep(1)

def reader1(q:Queue):
    if not q.empty():
        data = q.get(True)
        print("reader1 取到了 %s"%data)
        time.sleep(1)
if __name__ =='__main__':
    q = Queue(4)
    p1= Process(target=writer1,args=(q,))
    p1.start()
    time.sleep(1)
    print("-"*50)
    p2 = Process(target=reader1,args=(q,))
    p2.start()
    time.sleep(1)
    p1.join()
    p2.join()