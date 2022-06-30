#!/usr/bin/python3
# auther@hy
# 2022年06月16日
from socket import *
import sys
import select
tcp_client = socket(AF_INET,SOCK_STREAM)
dest_addr = ('192.168.0.102',7788)
socket.connect(dest_addr)
epoll = select.epoll()
epoll.register(sys.stdin.fileno(),select.EPOLLIN)
epoll.register(tcp_client.fileno(),select.EPOLLIN)
while True:
    events = epoll.poll(-1,2)
    for fd,event in events:
        if fd == sys.stdin.fileno():
            send_data = input("请输入数据：")
            tcp_client.send(send_data.encode('utf8'))
        elif fd == socket.fileno():
            recv_data = tcp_client.recv(128)
            if not recv_data:
                print("服务器断开了....")
                exit()
            print(recv_data.decode('utf8'))

tcp_client.close()