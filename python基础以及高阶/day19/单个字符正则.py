#!/usr/bin/python3
# auther@hy
# 2022年06月20日
import re
# res = re.match('t.o','two')
# print(res.group())
#
# print('-'*50)
# res = re.match('[hH]ello Python','hello Python')
# print(res.group())
# print('-'*50)

res = re.match('[0-9]hello Python','7hello Python')
print(res.group())
print('-'*50)
res = re.match("嫦娥\s号","嫦娥 号发射成功")
print(res.group())
list1 =['bat','bit', 'but', 'hat', 'hit', 'hut']
for i in list1:
    res = re.match('[bh][\w][t]$',i)
    print(res.group())