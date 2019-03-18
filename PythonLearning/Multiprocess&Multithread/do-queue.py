# -*-coding:UTF-8-*-

from multiprocessing import Process, Queue
import os, time, random


def write(q):
	print('Process to write %s ...' % os.getpid())
	for i in ['A', 'B', 'C']:
		print('Put %s to queue ...' % i)
		q.put(i)
		time.sleep(random.random())


def read(q):
	print('Process to read %s ...' % os.getpid())
	while True:
		i = q.get(True)
		print('Get %s from queue ...' % i)


if __name__ == '__main__':
	q = Queue()
	pw = Process(target=write, args=(q,))
	pr = Process(target=read, args=(q,))
	pw.start()
	pr.start()
	pw.join()
	# pr进程里是死循环，无法等待其结束，只能强行终止
	pr.terminate()
