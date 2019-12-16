#!/usr/bin/python3
""" script that adds the State object “Louisiana” to the database"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    flag = 0
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    db = Session()

    state = State(name="Louisiana")
    db.add(state)
    db.commit()
    print(state.id)
    db.close()
