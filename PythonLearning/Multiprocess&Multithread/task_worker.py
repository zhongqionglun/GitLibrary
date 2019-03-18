# -*-coding:UTF-8-*-
import time, sys, queue
from multiprocessing.managers import BaseManager

"""
auth:zhongqionglun
time:2019/3/18
description:分布式进程中的任务进程
"""


# 由于这个QueueManager只从网络上获取Queue，所以注册只提供名
BaseManager.register('get_task')
BaseManager.register('get_result')

# 连接到服务器，也就是运行task_master的机器
server_addr = '127.0.0.1'
print('Connect to server %s ...' % server_addr)

# 端口和验证码与服务器一致
m = BaseManager(address=(server_addr, 5000), authkey=b'abc')

#从网络连接
m.connect()

# 获取Queue的对象
task = m.get_task()
result = m.get_result()

# 从task队列取任务，并把结果写入result队列
for i in range(10):
	try:
		n = task.get(timeout=1)
		print('Run task %d * %d ...' % (n, n))
		r = '%d * %d = %d' % (n, n, n*n)
		time.sleep(1)
		result.put(r)
	except Queue.Empty:
		print('task queue is empty ...')

# task 处理完成
print('Worker has done.')
