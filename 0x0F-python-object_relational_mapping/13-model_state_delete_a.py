#!/usr/bin/python3
"""
    This is a script that deletes al State objects
    with a name containing the letter 'a'
    from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine(f'mysql+mysqldb://{user}:{passwd}@localhost:\
                           3306/{db}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    rows_to_delete = session.query(State).filter(State.name.like("%a%")).all()

    for row in rows_to_delete:
        session.delete(row)

    session.commit()
    session.close()
