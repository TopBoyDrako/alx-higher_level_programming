#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":

    mydb = MySQLdb.connect(host="localhost", port=3306, uname=argv[1],
                           password=argv[2], mydb=argv[3])

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM states")

    rows = cursor.fetchall()
    for i in rows:
        print(i)

    cursor.close()
    mydb.close()
