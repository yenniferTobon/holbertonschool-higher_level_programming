#!/usr/bin/python3
import MySQLdb
import sys
argv=sys.argv
myConnection=MySQLdb.connect(user=argv[1], password=argv[2], db=argv[3], port=3306, host='localhost')
c=myConnection.cursor()
c.execute("SELECT id,name FROM states WHERE name='{:s}' ORDER BY id ASC".format(argv[4]))
for states in c.fetchall():
	print(states)
myConnection.close()
