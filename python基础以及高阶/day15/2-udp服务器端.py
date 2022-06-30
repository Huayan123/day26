#!/usr/bin/python3
# auther@hy
# 2022年06月15日
from socket import *
import sys
server_socket = socket(AF_INET,SOCK_DGRAM)
local_addr = (sys.argv[1],7788)
server_socket.bind(local_addr)
# 服务器接受数据
recv_data = server_socket.recvfrom(5)
print(recv_data[0].decode('utf8'))
print(recv_data[1])
server_socket.sendto('我已收到！'.encode('utf8'),recv_data[1])
server_socket.close()