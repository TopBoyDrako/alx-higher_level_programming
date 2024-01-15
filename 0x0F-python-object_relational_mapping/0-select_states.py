#!/usr/bin/python3
""" 
This script lists all states from the database hbtn_0e_0_usa
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":

    username=sys.argv[1]
    password=sys.argv[2]
    mydb=sys.argv[3]

    mydb = MySQLdb.connect(host="localhost", port=3306)

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM states")

    rows = cursor.fetchall()
    for i in rows:
        print(i)

    cursor.close()
    mydb.close()
