#!/usr/bin/python3
"""
This script lists all states with a name starting with N from the database
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         password=argv[2], db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name\
                    LIKE BINARY 'N%' ORDER BY id ASC")

    rows = cursor.fetchall()
    for i in rows:
        print(i)

    cursor.close()
    db.close()
