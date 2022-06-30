#!/usr/bin/python3
# auther@hy
# 2022年06月27日
# python与mysql交互
from pymysql import *

def main():
    con = connect(user='root',password='123',host="81.70.243.245",database = 'day25',port=3306,charset='utf8')
    cs1 = con.cursor() # 移动光标
    for i in range(100000):
       cs1.execute("insert into test_index values ('ha-%d')"%i)
    con.commit()

if __name__ == '__main__':
    main()