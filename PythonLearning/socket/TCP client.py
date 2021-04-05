#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zql
# datetime:2020/04/18

'''
description:a simple example of socket

'''

import socket

target_host = "127.0.0.1"
target_port = 9999

# 创建socket 对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接
client.connect((target_host, target_port))

# 发送一些数据
client.send(str.encode("send request!"))

# 接收一些数据
response = client.recv(4096)

# 处理接收数据
print(bytes.decode(response))
