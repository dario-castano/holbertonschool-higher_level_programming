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
    cursor.execute("""SELECT * FROM states WHERE name=%s ORDER BY states.id ASC""", (state,))
    out = cursor.fetchall()
    print_cursor(out)
