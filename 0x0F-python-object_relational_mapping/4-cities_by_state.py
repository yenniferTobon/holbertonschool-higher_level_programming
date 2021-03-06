#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""

if __name__ == '__main__':
    import MySQLdb
    import sys
    argv = sys.argv
    myConnection = MySQLdb.connect(
        user=argv[1],
        password=argv[2], db=argv[3], port=3306, host='localhost')
    c = myConnection.cursor()
    c.execute(
        "SELECT cities.id, cities.name,states.name\
        FROM cities, states\
        WHERE cities.state_id = states.id\
        ORDER BY cities.id ASC")
    for cyties in c.fetchall():
        print(cyties)
    c.close()
    myConnection.close()
