#!/usr/bin/python3
"""
prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    state = sys.argv[4]
    db_conf = {
        'host': 'localhost',
        'port': 3306,
        'user': sys.argv[1],
        'passwd': sys.argv[2],
        'db': sys.argv[3],
    }

    address = 'mysql://{}:{}@{}:{}/{}'.format(
                    db_conf['user'],
                    db_conf['passwd'],
                    db_conf['host'],
                    db_conf['port'],
                    db_conf['db'])

    engine = create_engine(address)
    SMaker = sessionmaker(engine)
    session = SMaker()
    query = session\
        .query(State)\
        .filter(State.name == state)\
        .first()

    try:
        print(query.id)
    except AttributeError:
        print("Not found")
