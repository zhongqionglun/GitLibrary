# -*-coding:UTF-8-*-

import string, random
import mysql.connector


class GenRcode():
    def genrcode():
        chars = string.ascii_letters + string.digits
        s = "".join(random.choice(chars) for i in range(10))
        t = "".join(random.sample(chars, 10))
        rcode = s + " ******** " + t
        return rcode

    genrcode = staticmethod(genrcode)


class OpMysql():
    def __init__(self):
        self.conn = mysql.connector.connect(user='root', password='123456', database='test')

    def Insert(self, id, code):
        self.cursor = self.conn.cursor()
        self.cursor.execute('insert into cdkey (id,code) values (%s,%s)', (id, code))
        self.conn.commit()

    def SelectAll(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("select * from cdkey")
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def Close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == "__main__":
    mycon = OpMysql()
    rcode = []
    for i in range(100):
        rcode.append(GenRcode.genrcode())
        print(str(i) + " and " + rcode[i])
        mycon.Insert(i + 1, rcode[i])
    mycon.SelectAll()
    mycon.Close()
