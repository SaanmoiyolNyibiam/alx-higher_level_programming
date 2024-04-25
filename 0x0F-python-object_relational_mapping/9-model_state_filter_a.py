#!/usr/bin/python3
"""
    This is a script that lists all State objects
    that contain the letter a
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
    engine = create_engine(f'mysql+mysqldb://{user}:{passwd}@localhost/{db}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session().query(State)\
        .order_by(State.id)\
        .filter(State.name.like('%a%'))
    for row in session:
        print(f"{row.id}: {row.name}")