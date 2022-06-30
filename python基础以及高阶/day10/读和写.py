#!/usr/bin/python3
# auther@hy
# 2022年06月09日
import os
def write_read():
    f = open('README',mode='r+',encoding='UTF-8')
    f.write("hello python")
    f.seek(0,os.SEEK_CUR)
    text = f.read()
    print(text)
    f.close()
def read_write():
    f = open('README',mode='r+',encoding='utf8')
    text = f.read(6)
    print(text)
    f.seek(0,os.SEEK_CUR)
    f.write("day10")
    f.close()
if __name__=='__main__':
     # write_read()
     read_write()