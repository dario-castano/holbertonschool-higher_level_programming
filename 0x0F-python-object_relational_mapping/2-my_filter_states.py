#!/usr/bin/python3
import sys
import MySQLdb


if __name__ == '__main__':
    state = sys.argv[4].translate({39: None})
    db_conf = {
        'host': 'localhost',
        'port': 3306,
        'user': sys.argv[1],
        'passwd': sys.argv[2],
        'db': sys.argv[3],
    }

    db = MySQLdb.connect(**db_conf)
    cursor = db.cursor()
    statement = "SELECT * FROM states WHERE name=\'{:s}\' ORDER BY states.id ASC".format(state)
    cursor.execute(statement)
    out = cursor.fetchall()
    for row in out:
        print(row)
    cursor.close()
    db.close()
