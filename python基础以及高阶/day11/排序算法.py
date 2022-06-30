#!/usr/bin/python3
# auther@hy
# 2022年06月13日
import random
class Paixu_Sort:
    def __init__(self,n,num_range):
        self.n = n
        self.arr = [0]*n
        self.num_range = num_range
        self.arr = [random.randint(0,num_range) for i in range(n)]

    def count(self):
        """
        计数排序
        """
        arr = self.arr
        current_arr = [0]*(self.num_range+1)
        # 统计出现的次数
        for i in arr:
            current_arr[i] += 1
        # 将统计的数组回填到原数组
        k = 0
        for i in range(0,self.num_range+1):
            for j in range(0,current_arr[i]):
                 arr[k] = i
                 k += 1
    def adjust_max_heap(self,pos,len):
        """
        大根堆调整过程
c       pos 调整的子树的父亲
        len 堆元素的个数
        :return:
        """
        dad = pos
        son = dad*2+1
        arr = self.arr
        # 判断左右子节点的大小
        while son<len:
            if son+1 < len and arr[son]<arr[son+1]:
                son+1
            # 判断子节点与父节点的大小
            if arr[dad]<arr[son]:
                arr[son],arr[dad] = arr[dad],arr[son]
                dad = son
                son = dad*2+1
            else:break


    def heap(self):
        arr =self.arr
        # 调整为大根堆
        for i in range(self.n // 2 - 1,-1,-1):
            self.adjust_max_heap(i,self.n)
        arr[0],arr[self.n-1]=arr[self.n-1],arr[0]
        # 调整剩余的部分为大根堆
        for i in range(self.n-1,-1,-1):
            self.adjust_max_heap(0,i)
            arr[0],arr[i-1]=arr[i-1],arr[0]

    def test_sort(self,sort_method,*args,**kwargs):
        """

        回调函数
        不加括号
        :param sort_method:
        :param args:
        :param kwargs:
        :return:
        """
        print(self.arr)
        sort_method(*args,**kwargs)
        print('-'*50)
        print(self.arr)
    def use_sort(self):
        for i in range(5,-1,-1):
            print(i)

if __name__=='__main__':
    sort = Paixu_Sort(10,99)
    sort.test_sort(sort.count)









