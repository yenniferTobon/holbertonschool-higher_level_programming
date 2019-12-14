#!/usr/bin/python3
import MySQLdb
myConnection= MySQLdb.connect(db='hbtn_0e_0_usa', host='localhost', port=3306, user='root', password='')
c=myConnection.cursor()
c.execute("SELECT id,name FROM states WHERE name like 'N%' ORDER BY id ASC")
for states in c.fetchall():
	print(states)
myConnection.close()
