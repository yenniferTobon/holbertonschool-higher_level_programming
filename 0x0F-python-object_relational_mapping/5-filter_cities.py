#!/usr/bin/python3
"""takes in the name of a state as an argument and lists all cities"""

if __name__ == '__main__':
    import MySQLdb
    import sys
    argv = sys.argv
    cities_name = ""
    myConnection = MySQLdb.connect(
        user=argv[1],
        password=argv[2], db=argv[3], port=3306, host='localhost')
    c = myConnection.cursor()
    c.execute("SELECT cities.name\
        FROM cities JOIN states\
        ON cities.state_id = states.id\
        WHERE states.name= BINARY %s\
        ORDER BY cities.id ASC", (argv[4],))
    for rows in c.fetchall():
        cities_name = rows[0] + ", " + cities_name
    cities_name = cities_name[:-2]
    print("{}".format(cities_name))
    c.close()
    myConnection.close()
