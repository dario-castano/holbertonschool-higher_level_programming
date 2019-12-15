#!/usr/bin/python3
import sys
import MySQLdb


def print_cursor(result):
    """Prints a cursor recursively
    """
    if not result:
        return
    else:
        print(result[0])
        print_cursor(result[1:])


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
    statement = "SELECT cities.id, cities.name, states.name \
                FROM cities INNER JOIN states \
                ON (states.id=cities.state_id) \
                ORDER BY cities.id ASC"
    cursor.execute(statement)
    out = cursor.fetchall()
    print_cursor(out)