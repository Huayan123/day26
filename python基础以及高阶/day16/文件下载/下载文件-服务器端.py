#!/usr/bin/python3
# auther@hy
# 2022年06月16日
from socket import *
import sys
def get_content(filename):
    """
    将存在的文件打印出来
    :param filename:
    :return:
    """
    try:
        with open(filename,mode='rb') as f:
            print(f.read())
    except:
        print("文件不存在！")
def main():
    if(len(sys.argv))!=2:
        print("ip地址和port端口号不对!")
        print("按照如下的方式输入:python xxx.py 7788")
        return
    else:
        port = int(sys.argv[1])

    tcp_socket = socket(AF_INET,SOCK_STREAM)
    addr = ('',port)
    tcp_socket.bind(addr)
    tcp_socket.listen(128)
    while True:
        client_socket,client_addr = tcp_socket.accept()
        filename = client_socket.recv(1024).decode('utf8')
        print("客户端请求下载的文件名:%s"%(filename))
        file_content = get_content(filename)
        if file_content:
            client_socket.send(file_content)
        client_socket.close()
    tcp_socket.close()
if __name__=='__main__':
    main()


