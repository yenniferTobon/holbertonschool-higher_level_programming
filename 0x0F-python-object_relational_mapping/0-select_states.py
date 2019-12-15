#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa"""

if __name__ == '__main__':
    """ get data from db """

    import MySQLdb
    import sys
    argv = sys.argv
    miConnection = MySQLdb.connect(
            db=argv[3],
            user=argv[1], host='localhost', port=3306, password=argv[2])
    c = miConnection.cursor()
    c.execute("SELECT * FROM states ORDER BY id ASC")
    for states in c.fetchall():
        print(states)
    c.close()
    miConnection.close()
