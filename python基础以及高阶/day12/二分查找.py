#!/usr/bin/python3
# auther@hy
# 2022年06月14日
def binsearch(arr,target):
    l  = 0
    h = len(arr) -1
    while l<=h:
        mid = (l+h)//2
        if arr[mid]>target:
            h = mid
        elif arr[mid]<target:
            l = mid
        else:return mid
    return -1

