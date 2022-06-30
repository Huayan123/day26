#!/usr/bin/python3
# auther@hy
# 2022年06月15日

# udp实现客户端
import socket
client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
dest_addr = ('192.168.0.32',7788)
client_socket.sendto("hello".encode('utf8'),dest_addr)
recv_data = client_socket.recvfrom(1024)
print(recv_data[0].decode('utf8'))
client_socket.close()

