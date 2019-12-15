#!/usr/bin/python3
"""
adds the State object “Louisiana” to
the database hbtn_0e_6_usa
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

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    print(new_state.id)
