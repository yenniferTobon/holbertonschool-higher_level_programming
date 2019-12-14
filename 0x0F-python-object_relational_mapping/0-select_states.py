#!/usr/bin/python3
import MySQLdb
miConnection=MySQLdb.connect(db ='hbtn_0e_0_usa', user='root', host='localhost', port=3306, password='')
c=miConnection.cursor()
c.execute("SELECT * FROM states ORDER BY id ASC")
for states in c.fetchall():
	print(states)
miConnection.close()
