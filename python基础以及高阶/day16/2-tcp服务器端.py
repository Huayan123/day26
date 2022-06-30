#!/usr/bin/python3
# auther@hy
# 2022年06月16日
from socket import *
client_socket = socket(AF_INET,SOCK_STREAM)
client_socket.bind('192.168.0.32',7788)
client_socket.listen(128)
tcp_client,client_addr = client_socket.accept()
recv_data_server = tcp_client.recv(5)
print(recv_data_server.decode('utf8'))
tcp_client.send(b'收到！')
tcp_client.close()
client_socket.close()
