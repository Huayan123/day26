#!/usr/bin/python3
# auther@hy
# 2022年06月22日
import copy
# 深浅拷贝
a = [1,2]
b = [3,4]
c = [a,b]
d = copy.copy(c) # 浅拷贝
e = copy.deepcopy(c) # 深拷贝，递归拷贝，两者的变化不会同时发生变化
c[0][0] = 5
# 只拷贝了第一层，内部的数值变换仍会改变，id号不相同
print(d)
print(c)
print("-"*50)


print(c)
print(e)

print(id(c))
print(id(e))