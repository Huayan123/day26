#!/usr/bin/python3
# auther@hy
# 2022年06月21日
import re
labels = ["<html><h1>www.cskaoyan.com</h1></html>",
          "<html><h1>www.cskaoyan.com</h2></html>"]

for label in labels:
    ret=re.match(r'<([a-z]+)><(\w*)>.*</\2></\1>',label)
    if ret:
        print("%s 是符合要求的标签" % ret.group())
    else:
        print("%s 不符合要求" % label)
print("-"*50)
ret=re.match(r'<(?P<n1>\w*)><(?P<n2>\w*).*</(?P=n2)></(?P=n1)>',
             "<html><h1>www.cskaoyan.com</h1></html>")
print(ret.group())



# if ret:
#     print("%s 是符合要求的标签" % ret.group())
# else:
#     print("%s 不符合要求" % label)