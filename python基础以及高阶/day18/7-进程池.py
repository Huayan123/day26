#!/usr/bin/python3
# auther@hy
# 2022年06月19日
from multiprocessing.pool import Pool
import time,os,random
def run(msg):
    start_time = time.time()
    print("%d 开始由pid:%d运行.."%(msg,os.getpid()))
    time.sleep(random.random())
    end_time = time.time()
    print("%s 执行了 %0.2f..."%(msg,end_time-start_time))

if __name__=='__main__':
    pl = Pool(3) # 调用三个进程池
    for i in range(10):
        pl.apply_async(run,(i,)) # 向哪个客户服务，异步通信
    print("-"*50)
    pl.close()
    print("close")
    # 运行之后不会立即结束所有进程
    pl.join()
    print("end")

