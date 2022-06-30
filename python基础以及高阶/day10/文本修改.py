#!/usr/bin/python3
# auther@hy
# 2022年06月10日
import os
import string
import re
def tran_text():
    file1 = open('README.txt',mode='r',encoding='UTF-8')
    file2 = open('README1.txt',mode='a',encoding='UTF-8')
    while True:
        text = file1.readlines()
        if not text:
            break
        item = ""
        for line in text:
            item = item+" ".join(line.split(","))
        file2.write(item)
    file1.close()
    file2.close()
def tongji():
    f = open("README1.txt",mode='rb')
    lines = f.readlines()

if __name__=="__main__":
    tran_text()
    tongji()