#!/usr/bin/python3
"""script that changes the name of a State object"""

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

    db.query(State).filter(State.id == 2).update({'name': "New Mexico"})
    db.commit()
    db.close()
