# -*-coding:UTF-8-*-
import datetime, time, json, threading
import multiprocessing


class run_sn(object):

	def Now_time(self):
		s = datetime.datetime.now()
		return s.strftime("%Y-%m-%d %H:%M:%S")

	def Time_id(self, a):
		return a

	def sn_test(self, x):
		x = '%04d' % x
		sn_t = ('0000-0000-0000-' + x)
		return str(sn_t)

	def data1(self, x):
		global a
		a += 1
		wa = {"msg": 1, "id": self.Time_id(a), "ver": "1.0", "sn": self.sn_test(x), "pid": 18, "pname": "DAG1000-8S ",
		      "productVersion": "02181003 2017-12-20 14:52:25 offical"}
		j = json.dumps(wa)
		return j

	def data2(self, x):
		global a
		a += 1
		wa = {"msg": 1, "id": self.Time_id(a), "ver": "1.0", "sn": self.sn_test(x), "pid": 18, "pname": "DAG1000-8S ",
		      "productVersion": "02181003 2017-12-20 14:52:25 offical",
		      "hash": "REEwMC0wMDQwLUM5MDAtMDIyMTo6bUI0aE5iaXJqRUhHVDVGSA=="}
		j = json.dumps(wa)
		return j

	def data_it(self):
		global a
		a += 1
		wa = {"msg": 0, "id": self.Time_id(a), "ver": "1.0", "time": self.Now_time()}
		j = json.dumps(wa)
		return j

	def run(self, x):
		import socket
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(('172.28.89.116', 3100))
		while True:
			s.settimeout(60)
			try:
				s.send(self.data1(x).encode())
				time.sleep(0.1)
				answer = s.recv(128).decode('utf-8')
				if not repr(answer):
					continue
				else:
					print("Received answer of data1 %s" % answer + "=====received X num ..%d" % x)
					break
			except socket.timeout:
				continue

		time.sleep(0.5)
		print("send data2.....%d" % x)
		s.send(self.data2(x).encode())
		while True:
			s.send(self.data_it().encode())
			print('%s:  ' % self.sn_test(x) + "Received answer of data_it %s" % s.recv(128).decode('utf-8'))
			time.sleep(10)


def run_test(x, n):
	for i in range(x, n):
		wa = run_sn()
		ta = threading.Thread(target=wa.run, name='Ta', args=(i,))
		ta.start()


def run_loop():
	print("create process...")
	p1 = multiprocessing.Process(target=run_test, args=(1, 1000),)
	p2 = multiprocessing.Process(target=run_test, args=(1001, 2000), )

	p1.start()
	p2.start()
	# p.apply_async(run_test, args=(3001,4501),)
	# p.apply_async(run_test, args=(4501,6001),)
	# p.apply_async(run_test, args=(6001,7501),)
	# p.apply_async(run_test, args=(7501,9001),)


if __name__ == "__main__":
	# run_test(1, 2)
	run_loop()
	# run_sn()
	# run_sn.run(1)
