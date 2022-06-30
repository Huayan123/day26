#!/usr/bin/python3
# auther@hy
# 2022年06月07日
# 将元组 (1,2,3) 和集合 {4,5,6} 合并成一个列表
tuple1 = (1,2,3)
list1 = list(tuple1)
set1 = {4,5,6}
for i in set1:
    list1.append(i)
print(list1)
print("-"*50)
# 在列表 [1,2,3,4,5,6] 首尾分别添加整型元素 7 和 0
list2 = [1,2,3,4,5,6]
list2.insert(0,7)
list2.insert(len(list2),0)
print(list2)
print("-"*50)
# 反转列表 [0,1,2,3,4,5,6,7]
list3 = [0,1,2,3,4,5,6,7]
print(list3[::-1])
print("-"*50)
# 反转列表 [0,1,2,3,4,5,6,7] 后给出中元素 5 的索引号
list4 = [0,1,2,3,4,5,6,7]
list4.sort()
print(list4.index(list4[5]))
print("-"*50)
# 分别统计列表 [True,False,0,1,2] 中 True,False,0,1,2的元素个数，发现了什么？
list5 =[True,False,0,1,2]
print(list5.count(0))
print(list5.count(1))
# 真的值有两个，假的值有两个
list6 = [True, 1, 0,'x', None,'x', False, 2, True]
print([i  for i in list6 if i!='x'])
print("-"*50)
for i in range(len(list6)):
    if i%2==0:
        print(list6[i])
print("-"*50)
# [3,0,8,5,7]
list7 = [3,0,8,5,7]
list7.sort()
print(list7)
list7.reverse()
print(list7)
print([x if x>5 else x==0 for x in list7])
print("-"*50)
list8 = ['x','y','z']
print(list(enumerate(list8)))
