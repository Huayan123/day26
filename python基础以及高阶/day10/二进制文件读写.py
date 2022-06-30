#!/usr/bin/python3
# auther@hy
# 2022年06月10日
def read_add_bin():
    f = open('README',mode='rb+')
    text = f.read()
    print(text)
    f.seek(2)
    f.write(b"123")
    f.close()

if __name__=="__main__":
    read_add_bin()
