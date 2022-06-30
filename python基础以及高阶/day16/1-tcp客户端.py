#!/usr/bin/python3
# auther@hyifconfig
# 2022年06月16日
import socket
# 先socket,再connect，最后发送
from socket import *
tcp_client = socket(AF_INET,SOCK_STREAM)
tcp_client.connect("192.168.0.32",7788)
tcp_client.send(b"hello pythpn6")
recv_data = tcp_client.recv(5)
print(recv_data)
tcp_client.close()
