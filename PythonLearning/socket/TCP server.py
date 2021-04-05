#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zql
# datetime:2020/04/18

'''
description:a simple example of TCP Server

'''

import socket
import threading

bind_ip = "127.0.0.1"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)
print("[*] Listening on %s:%d" % (bind_ip, bind_port))


# 这是客户处理线程
def handle_client(client_socket):
    # 打印客户端发送内容
    request = client_socket.recv(1024)
    print("[*] Received: %s" % (bytes.decode(request)))

    # 返回数据
    client_socket.send(str.encode("ack!"))
    client_socket.close()


while True:
    client, addr = server.accept()
    print("[*] Accepted connected from %s:%d" % (addr[0], addr[1]))

    # 挂起客户端线程，处理传入参数
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
