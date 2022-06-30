#!/usr/bin/python3
# auther@hy
# 2022年06月20日
import threading

import time
class Mythread(threading.Thread):
    # 线程的封装，start实际调用线程的run函数
    def run(self):
        for i in range(3):
            time.sleep(1)
            print(self.name+":"+str(i))

def test():
    for i in range(5):
        thread = Mythread()
        thread.start()
if __name__ == '__main__':
    test()