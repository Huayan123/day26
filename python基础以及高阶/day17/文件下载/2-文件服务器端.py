#!/usr/bin/python3
# auther@hy
# 2022年06月18日
import struct
import sys
from socket import *
import time
import select
tcp_server_socket = socket(AF_INET,SOCK_STREAM)
# 地址和端口复用
tcp_server_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
addr = ('192.168.0.102',7788)
tcp_server_socket.bind(addr)
tcp_server_socket.listen(100)
client_socket,addr = tcp_server_socket.accept()

filename ='file'
b_file_name =(filename.encode('utf8'))
client_socket.send(struct.pack('I',len(b_file_name)))
client_socket.send(b_file_name)
f = open('file',mode='rb')
data = f.read()
client_socket.send(struct.pack('I',len(data)))
client_socket.send(data)
f.close()
f.close(time.sleep(5))
client_socket.close()
tcp_server_socket.close()

