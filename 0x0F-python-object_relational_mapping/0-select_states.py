#!/usr/bin/python3
""" write a Script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv

# This code should not be executed when imported
if __name__ == '__main__':

    # this is a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # It gives us the ability to have multiple seperate working environments
    # through the same connection to the database.
    cur = db.cursor()
    cur.execute("SELECT * FROM states")

    rows = cur.fetchall()
    for i in rows:
        print(i)
    # Clean up process
    cur.close()
    db.close()
