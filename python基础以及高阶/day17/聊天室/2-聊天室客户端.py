#!/usr/bin/python3
# auther@hy
# 2022年06月18日
import sys
from socket import *
import select
tcp_client = socket(AF_INET,SOCK_STREAM)
if len(sys.argv) != 2:
    print("ip和端口号参数不正确!")
addr = (sys.argv[1],7788)
name = input("请输入你的名字:")
tcp_client.connect(addr)
epoll = select.poll()
epoll.register(sys.stdin.fileno(),select.EPOLLIN)
epoll.register(tcp_client.fileno(),select.EPOLLIN)
while True:
    event_list = epoll.poll()
    for fd,event in event_list:
        if fd == sys.stdin.fileno():
            try:
                data = input("请输入数据:")
            except Exception as e:
                print("中止")
                tcp_client.close()
                exit(2)
            send_data = name + ":" + data
            tcp_client.send(send_data.encode('utf8'))
        elif fd == tcp_client.fileno():
           recv_data = tcp_client.recv(1024).decode('utf8')
           if recv_data:
               print(recv_data)
           else:
               exit(0)
tcp_client.close()

