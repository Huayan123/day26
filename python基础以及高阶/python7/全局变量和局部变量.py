#!/usr/bin/python3
# auther@hy
# 2022年06月06日
num = 10
def demo1():
    '''
    global 修改为全局变量的标识符参数
    :return:
    '''

    print('demo1'+'-'*50)
    global num
    num = 100
    print(num)
def demo2():
    print('demo2'+'-'*50)
    print(num)
# demo1()
# demo2()
# print('over')
import import1
if __name__ == '__main__':
    print(import1.__name__)
    print(__name__)
    import1.print1()
