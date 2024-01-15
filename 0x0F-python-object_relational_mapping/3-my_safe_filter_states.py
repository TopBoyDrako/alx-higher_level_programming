#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the
states table but it is safe from sql injections
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         password=argv[2], db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE BIINARY name = %s", [argv[4]])

    rows = cursor.fetchall()
    for i in rows:
        print(i)

    cursor.close()
    db.close()
