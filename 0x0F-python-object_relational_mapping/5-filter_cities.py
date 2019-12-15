#!/usr/bin/python3
"""
takes in the name of a state as an argument
and lists all cities of that state, using
the database hbtn_0e_4_usa
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
    statement = "SELECT cities.name \
                FROM cities INNER JOIN states \
                ON cities.state_id=states.id \
                WHERE states.name=%s \
                ORDER BY cities.id ASC"
    cursor.execute(statement, (state,))
    out = cursor.fetchall()
    cities = ", ".join([x[0] for x in out])
    print(cities)
    cursor.close()
    db.close()
