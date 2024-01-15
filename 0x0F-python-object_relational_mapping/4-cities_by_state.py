#!/usr/bin/python3
"""
This script list all cities in the database
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         password=argv[2], db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELET cities.id, cities.name, states.name FROM cities\
                    INNER JOIN states ON cities.state_id = states.id\
                     ORDER BY cities.id ASC")

    rows = cursor.fetchall()
    for i in rows:
        print(i)

    cursor.close()
    db.close()
