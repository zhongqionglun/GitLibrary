# -*-coding:UTF-8-*-

import threading

# create global ThreadLocal
local_school = threading.local()


def process_student():
	# 取得当前线程的数据
	std = local_school.student
	print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
	local_school.student = name
	process_student()


t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

