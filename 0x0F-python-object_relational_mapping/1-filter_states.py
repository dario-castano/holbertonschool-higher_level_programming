#!/usr/bin/python3
"""lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb


if __name__ == '__main__':
    db_conf = {
        'host': 'localhost',
        'port': 3306,
        'user': sys.argv[1],
        'passwd': sys.argv[2],
        'db': sys.argv[3],
    }

    db = MySQLdb.connect(**db_conf)
    cursor = db.cursor()
    statement = "SELECT * \
                FROM states \
                WHERE name LIKE BINARY 'N%' \
                ORDER BY states.id ASC"
    cursor.execute(statement)
    out = cursor.fetchall()
    for row in out:
        print(row)
    cursor.close()
    db.close()
