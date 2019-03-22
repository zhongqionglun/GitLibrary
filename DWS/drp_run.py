





import datetime, time,json,threading
from multiprocessing import Pool

class run_sn(object):

    global a
    a = 1


    def Now_time(self):
        s = datetime.datetime.now()
        return s.strftime("%Y-%m-%d %H:%M:%S")


    def Time_id(self,a):
        return a

    def sn_test(self,x):
        x= '%04d'%x
        sn_t = ('0000-0000-0000-'+ x)
        return str(sn_t)



    def data1(self,x):
        global a
        a += 1
        wa ={"status": "","msg": 1, "id": self.Time_id(a), "ver": "1.0", "sn": self.sn_test(x), "pid": 18, "pname": "DAG1000-8S ","productVersion": "02181003 2017-12-20 14:52:25 offical"}
        j = json.dumps(wa)
        return (j)


    def data2(self,x):
        global a
        a += 1
        wa = {"status": "","msg": 1, "id": self.Time_id(a), "ver": "1.0", "sn": self.sn_test(x), "pid": 18, "pname": "DAG1000-8S ",
              "productVersion": "02181003 2017-12-20 14:52:25 offical",
              "hash": "REEwMC0wMDQwLUM5MDAtMDIyMTo6bUI0aE5iaXJqRUhHVDVGSA=="}
        j = json.dumps(wa)
        return (j)


    def data_it(self):
        global a
        a += 1
        wa = {"msg": 0, "id": self.Time_id(a), "ver": "1.0", "time": self.Now_time()}
        j = json.dumps(wa)
        return (j)

    # def  recv_form():
    #    t.settimeout(30)
    #     d,a=s.recvfrom(8192)


    def run(self,x):
        try:
            import socket
            n=0
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('172.28.53.20', 3100))

            s.send(self.data1(x).encode())
            print(s.recv(128).decode('utf-8'))
            time.sleep(0.5)
            s.send(self.data2(x).encode())
            print(s.recv(128).decode('utf-8'))
            while True:
                s.send(self.data_it().encode())
                s.settimeout(30)
                print('%s:  '%self.sn_test(x) + s.recv(128).decode('utf-8'))
                # print('此报文是:%s\n'%sn_test(x)+s.recv(1024).decode('utf-8'))
                time.sleep(5)
        except socket.timeout:
            run_sn.run(x)


def run_test(x,n):
    for a in range(x,n):
        wa = run_sn()
        ta= threading.Thread(target= wa.run,name='Ta',args=(a,))
        ta.start()


def run_loop():
    p = Pool(10)
    p.apply_async(run_test, args=(1,2500),)
    p.apply_async(run_test, args=(2501,5001),)
    # p.apply_async(run_test, args=(3001,4501),)
    # p.apply_async(run_test, args=(4501,6001),)
    # p.apply_async(run_test, args=(6001,7501),)
    # p.apply_async(run_test, args=(7501,9001),)

    p.close()
    p.join()





if __name__ == '__main__':
    # run_test(1,2)
    run_loop()
    # run_sn()
    # run_sn.run(1)
