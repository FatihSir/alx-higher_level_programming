#!/usr/bin/python3
""" a script that takes in an argument and displays all values in
   the states table of hbtn_0e_0_usa where name matches the argument
   safe from MySQL injections! """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = %s", [argv[4]])
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
