#!/usr/bin/python3
"""
This is a script that lists all states with its name starting with N (upper N)
from the DB
"""
import MySQLdb
from sys import argv

# The code should not be executed when imported
if __name__ == '__main__':
    # make a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # This iss the ability to have multiple seperate working environments
    # through the same connection to the database.
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name\
                LIKE BINARY 'N%' ORDER BY id ASC")

    rows = cur.fetchall()
    for i in rows:
        print(i)
    #The clean up process
    cur.close()
    db.close()
