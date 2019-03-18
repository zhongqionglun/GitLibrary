# -*-coding:UTF-8-*-
from multiprocessing import Process
import os


def func(name):
	print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
	print('Parent process %s...' % os.getpid())
	p = Process(target=func, args=('son',))
	print('Child process will start...')
	p.start()
	p.join()
	print('Child process end...')
