#!/usr/bin/python3
"""
deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
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
        .filter(State.name.contains('a'))

    for elem in query:
        session.delete(elem)

    session.commit()
