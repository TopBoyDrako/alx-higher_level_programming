#!/usr/bin/python3
"""
This script takes in the name of a state as an argument
and lists all cities of that state
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         password=argv[2], db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, FROM cities\
                    INNER JOIN states ON cities.state_id = states.id\
                    WHERE states.name = %s", [argv[4]])

    rows = cursor.fetchall()
    p = []
    for i in rows:
        p.append(i[1])
    print(", ".join(p))

    cursor.close()
    db.close()
