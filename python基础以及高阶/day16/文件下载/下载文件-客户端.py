#!/usr/bin/python3
# auther@hy
# 2022年06月16日
from socket import *
def main():
    tcp_client = socket(AF_INET,SOCK_STREAM)
    dest_ip = input("请输入ip地址：")
    dest_port = int(input("请输入目的地址端口号："))
    tcp_client.connect((dest_ip,dest_port))
    file_name = input("请输入文件名:")
    tcp_client.send(file_name.encode('utf8'))
    recv_data = tcp_client.recv(1024)
    if recv_data:
        with open(file_name+'2',mode='wb') as f:
            f.write(recv_data)
    tcp_client.close()
if __name__=='__main__':
    main()
