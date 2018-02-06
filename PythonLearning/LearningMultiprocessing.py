# -*-coding:UTF-8-*
from multiprocessing import Pool
import os, time, random


def long_time_task(name):
	print('Start task %s(%s)...' % (name, os.getpid()))
	start = time.time()
	time.sleep(random.random() * 10)
	end = time.time()
	print('The task %s(%s) runs %0.2f seconds' % (name, os.getpid(), (end - start)))


if __name__ == "__main__":
	print('The parent process %s' % os.getpid())
	p = Pool(4)
	for i in range(5):
		p.apply_async(long_time_task, args=(i,))
	print('Waiting for all subprocesses done...')
	p.close()
	p.join()
	print('All subprocesses done.')
