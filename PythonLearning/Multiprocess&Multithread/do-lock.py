# -*-coding:UTF-8-*-

import time, threading


def change_it(value):
	global balance
	balance = balance + value
	time.sleep(2)
	balance = balance - value
	print('balance is %s...' % balance)


def run_thread(value):
	print('thread %s for %d running ...' % (threading.current_thread().name, value))
	# change_it(value)
	for i in range(100000):
		# get lock
		lock.acquire()
		try:
			change_it(value)
		finally:
			# release lock
			lock.release()


if __name__ == '__main__':
	balance = 0
	threads = []
	lock = threading.Lock()
	print('thread %s is running ...' % threading.current_thread().name)
	for n in range(5):
		thread = threading.Thread(target=run_thread, name='sub_thread', args=(n,))
		threads.append(thread)
		thread.start()
	for m in threads:
		m.join()
	print(balance)
