#!/usr/bin/python3
"""
This script takes in an argument and displays all it's values
in the states table where name matches the argument
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         password=argv[2], db=argv[3])

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(argv[4])
    cursor.execute(query)

    rows = cursor.fetchall()
    for i in rows:
        print(i)

    cursor.close()
    db.close()
