#!/usr/bin/python3
# auther@hy
# 2022年06月20日
import time
def work1():
    print("-----work1-----")
    yield
    time.sleep(1)
def work2():
    print("-----work2-----")
    yield
    time.sleep(1)
def main():
    w1 = work1()
    w2 = work2()
    while True:
        next(w1)
        next(w2)
if __name__ == '__main__':
    main()