#!/usr/bin/python3
# auther@hy
# 2022年06月16日
import sys
from socket import *
import select
tcp_socket = socket(AF_INET,SOCK_STREAM)
tcp_socket.bind(('192.168.0.102',7788))
tcp_socket.listen(10)
client_socket,addr = tcp_socket.accept()
epoll = select.epoll()
epoll.register(sys.stdin.fileno(),select.EPOLLIN)
epoll.register(tcp_socket.fileno(),select.EPOLLIN)
while True:
    events = epoll.poll(-1,2)
    for fd,event in events:
        if fd == sys.stdin.fileno():
            data = input("请输入数据：")
            client_socket.send(data.encode('utf8'))
        elif fd == client_socket.fileno():
            recv_data = client_socket.recv()
            if not recv_data:
                print("客户端没有数据:")
                exit()
            print(recv_data.decode('utf8'))
client_socket.close()
tcp_socket.close()


