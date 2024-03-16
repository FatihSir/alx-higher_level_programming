#!/usr/bin/python3
"""a script that lists all states from the database hbtn_0e_0_usa"
import MySQLbd
from sys import argv


if __name__ == "__main__":
    db = MySQLbd.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], port="3306")
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()   
