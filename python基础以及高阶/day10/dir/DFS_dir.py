#!/usr/bin/python3
# auther@hy
# 2022年06月10日
import os
import sys
def DFS(path_name,width):
    list_filename = os.listdir(path_name)
    # 读取到当前目录下的所有文件夹以及文件
    for filename in list_filename:
        #判断是否是文件夹
        print(' '*width+filename)
        current_filename = path_name+'/'+filename
        if os.path.isdir(current_filename):
            DFS(current_filename,width+4)
def get_filename():
    """
    获取到路径名并将其传参
    :return:
    """
    print(sys.argv)



if __name__ == "__main__":
    DFS(sys.argv[1],0)
    # get_filename()