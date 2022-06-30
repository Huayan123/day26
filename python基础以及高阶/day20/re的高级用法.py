#!/usr/bin/python3
# auther@hy
# 2022年06月21日
import re
# search findall 查找
ret = re.search(r'\d+','阅读次数为 9999')
print(ret.group())
print("-"*50)
# find 查找不需要加上group()
ret = re.match(r'\d+','python = 9999, c = 7890, c++ = 12345')
print(ret)
# sub 直接打印ret
def add(temp):
    str_num = temp.group()
    num=int(str_num)+10
    return str(num)

ret=re.sub(r'\d+',add,'python 995')
print(ret)

# sub 例子
s = 'hello world, now is 2020/7/20 18:48, 现在是2020年7月20日18时48分。'
ret_s = re.sub(r'年|月',r'/',s)
ret_s = re.sub(r'日',r'/',ret_s)
ret_s = re.sub(r'时',r':',ret_s)
ret_s = re.sub(r'分',r'',ret_s)
print(ret_s)
