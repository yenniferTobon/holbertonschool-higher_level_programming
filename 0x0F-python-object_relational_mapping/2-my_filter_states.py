#!/usr/bin/python3
"""list data from db according to a name passed"""

if __name__ == '__main__':
    import MySQLdb
    import sys
    argv = sys.argv
    myConnection = MySQLdb.connect(
        user=argv[1],
        password=argv[1], db=argv[3], port=3306, host='localhost')
    c = myConnection.cursor()
    c.execute(
        "SELECT id, name FROM states WHERE name LIKE BINARY '{:s}'\
        ORDER BY id ASC".format(argv[4]))
    for states in c.fetchall():
        print(states)
    c.close()
    myConnection.close()
