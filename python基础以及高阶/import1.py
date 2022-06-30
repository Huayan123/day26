#!/usr/bin/python3
# auther@hy
# 2022年06月05日
''''
测试模块
'''
def print1():
    print("打印数字1")

if __name__ == '__main__':
    name = 1000   # 全局变量
    print(name)
    print1()  #测试接口
'''
_name_只有在本模块启动时，_name_变量等于_main_

'''