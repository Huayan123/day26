#!/usr/bin/python3
# auther@hy
# 2022年06月18日
import sys
from socket import *
import select
tcp_client = socket(AF_INET,SOCK_STREAM)
if len(sys.argv) != 2:
    print("请输入正确的IP和port")
    exit(2)
server_addr = (sys.argv[1],7788)
tcp_client.bind(server_addr)
tcp_client.listen(100)
epoll = select.epoll()
epoll.register(tcp_client.fileno(),select.EPOLLIN) # tcp派了小弟epoll监控谁连接
client_dict = {}
while True:
    event_list = epoll.poll()
    for fd,event in event_list:
        if fd == tcp_client.fileno(): # 判断是否有连接
            client_socket,addr = tcp_client.accept() # 连接的客户端和IP地址
            epoll.register(client_socket.fileno(),select.EPOLLIN) # 派小弟监控
            client_dict[client_socket.fileno()] = client_socket
        else:
            recv_data = client_dict[fd].recv(1024)
            if recv_data:
                for fillo,client in client_dict.items():
                    if fillo != fd:
                        client.send(recv_data)
            else:
                print("客户端断开了....")
                epoll.unregister(fd)
                client_dict[fd].close()
                client_dict.pop(fd)







