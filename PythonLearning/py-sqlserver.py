# -*-coding:UTF-8-*-
import sys
import pymssql

try:
	conn = pymssql.connect(host='.', database='master')
except pymssql.OperationalError:
	print("error:Could not Connection SQL Server, Please check your dblink configure!")
	sys.exit()
else:
	cur = conn.cursor()
cur.execute('select top 5  * from dbo.spt_monitor')
print(cur.fetchall())
cur.close()
conn.close()
