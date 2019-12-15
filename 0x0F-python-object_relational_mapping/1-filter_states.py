#!/usr/bin/python3
"""list data from db starting with 'N'"""

if __name__ == '__main__':
    import sys
    import MySQLdb
    argv = sys.argv
    myConnection = MySQLdb.connect(
        db=argv[3],
        host='localhost', port=3306, user=argv[1], password=argv[2])
    c = myConnection.cursor()
    c.execute(
        "SELECT id, name FROM states WHERE name like 'N%' ORDER BY id ASC")
    for states in c.fetchall():
        print(states)
    c.close()
    myConnection.close()
