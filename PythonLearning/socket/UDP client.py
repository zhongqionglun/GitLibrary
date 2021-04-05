#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zql
# datetime:2020/0418

'''
description:a simple example of socket

'''

import socket

target_host = "127.0.0.1"
target_port = 80

# 建立一个socket对象
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 发送一些数据
client.sendto(str.encode("test data"), (target_host, target_port))

# 接收一些数据
data, addr = client.recv(4096)

# 处理接收数据
print(data)
