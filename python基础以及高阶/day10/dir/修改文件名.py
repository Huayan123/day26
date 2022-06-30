#!/usr/bin/python3
# auther@hy
# 2022年06月10日
import  os
import sys
def rename_file():
    os.rename('file1','file2')
def remove_file():
    os.remove('file2')
def use_dir():

    print(os.listdir('file2'))

    os.chdir('file2')
    print(os.path.isdir('file2'))
    print(os.getcwd())

if __name__=="__main__":
    # rename_file()
   # remove_file()
    use_dir()