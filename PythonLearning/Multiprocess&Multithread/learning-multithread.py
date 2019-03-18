import time, threading


def loop(value):
	print('thread %s for %d running ...' % (threading.current_thread().name, value))
	m = 0
	while m <= 5:
		m += 1
		print('thread %s %s>>> %s' % (threading.current_thread().name, value, m))
		time.sleep(1)
	print('thread %s for %d ended ...' % (threading.current_thread().name, value))


if __name__ == '__main__':
	print('thread %s is running ...' % threading.current_thread().name)
	threads = []
	for n in range(5):
		thread = threading.Thread(target=loop, name='sub_thread', args=(n,))
		threads.append(thread)
		thread.start()
	for p in threads:
		p.join()
	print('thread %s ended ...' % threading.current_thread().name)

