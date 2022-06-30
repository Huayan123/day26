#!/usr/bin/python3
# auther@hy
# 2022年06月09日
import os
def use_seek1():
    f = open('README',mode='r+',encoding='UTF-8')
    f.seek(6,os.SEEK_SET)
    text = f.read()
    print(text)
def use_seek2():
    f = open("README",mode='r+',encoding='UTF-8')
    f.seek(0,os.SEEK_END)
    f.write("nihao")
    f.close()
if __name__=='__main__':
    # use_seek2()
    use_seek1()