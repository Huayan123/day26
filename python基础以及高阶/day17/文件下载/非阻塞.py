#!/usr/bin/python3
# auther@hy
# 2022年06月18日
from socket import *
tcp_server = socket(AF_INET,SOCK_STREAM)
tcp_server.setsockopt(SOL_SOCKET,SO_REUSEADDR)
dest_addr = ('192.168.0.102',7788)
tcp_server.bind(dest_addr)
tcp_server.listen(128)
tcp_server.setblocking(False)
client_socket = None
while True:
    try:
        client_socket,addr = tcp_server.accept()
        client_socket.setblocking(False)
        text = client_socket.recv(4)
        if not text:
            print("断开了...")
            exit(2)
        print(text)
    except Exception as e:
        pass