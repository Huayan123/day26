#!/usr/bin/python3
# auther@hy
# def caculate():
#     for j in range(1,10):
#         for i in range(1,j+1):
#             print('%d * %d=%d'%(i,j,i*j),end='\t')
#         print('\n')
# # caculate()
# list1 = [1,1,3,4,4,5,5]
# res = 0
# for i in list1:
#     res=i^res
# # print(res)
# # input1 = input("请输入:")
# def statical(num):
#     start = abs(num)
#     count = 0
#     while start != 0:
#         if start%2 == 1:
#             count += 1
#         start //= 2
#     if num<0:
#         count += 1
#     print(count)
# # statical(-5)
# print(type(input("请输入：")))
# print(type(1212))
# print(type('dada'))
list1 = [1,1,2,2,3,5,7,7]
def find_two_num(list1):
    start = 0
    list2=[]
    list3=[]
    for i in list1:
        start^=i
    tem = start&(-start)
    for i in list1:
        if i^tem==1:
            list2.append(i)
        else:list3.append(i)
    num1 = 0
    num2 = 0
    for i in list2:
        num1 ^= i

    for j in list3:
        num2 ^= j
    print(num1)
    print(num2)
find_two_num(list1)
