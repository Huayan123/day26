#!/usr/bin/python3
# auther@hy
# 2022年06月09日
import os
def read_add():
    f_read = open('README',mode='r',encoding='UTF-8')
    f_write = open('README1',mode='w',encoding='utf8')
    while True:
        text = f_read.readline()
        if not text:
            break
        f_write.write(text)
    f_read.close()
    f_write.close()
def write_open():
    f = open('README',mode='w',encoding='UTF-8')
    f.write('你好')
def a_read():
    f = open('README',mode='a+',encoding='UTF-8')
    text = f.read()
    print(text,end="")  # 换行\n结束，读取到空格结束
    # f.write("\ndaddsdad")
    f.close()
if __name__=="__main__":
    # read_add()
    # write_open()
    read_add()