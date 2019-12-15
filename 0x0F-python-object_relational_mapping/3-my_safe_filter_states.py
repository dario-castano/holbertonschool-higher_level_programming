#!/usr/bin/python3
"""
 takes in arguments and displays all values
 in the states table of hbtn_0e_0_usa where
 name matches the argument
"""
import sys
import MySQLdb


if __name__ == '__main__':
    state = sys.argv[4]
    db_conf = {
        'host': 'localhost',
        'port': 3306,
        'user': sys.argv[1],
        'passwd': sys.argv[2],
        'db': sys.argv[3],
    }

    db = MySQLdb.connect(**db_conf)
    cursor = db.cursor()
    cursor.execute("""\
                    SELECT * FROM states \
                    WHERE name=%s \
                    ORDER BY states.id ASC""", (state,))
    out = cursor.fetchall()
    for row in out:
        print(row)
    cursor.close()
    db.close()
