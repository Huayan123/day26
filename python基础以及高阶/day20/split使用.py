#!/usr/bin/python3
# auther@hy
# 2022年06月21日
import re

ret = re.split(r':| ',"info:xiaoZhang 33 shandong")
print(ret)
print("-"*50)
ret = re.match(r'a','A',re.I)
print(ret.group())
print("-"*50)
ret = re.match(r'.bc','\nbc',re.S)
print(ret.group())