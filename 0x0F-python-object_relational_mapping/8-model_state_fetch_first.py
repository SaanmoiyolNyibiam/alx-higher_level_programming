#!/usr/bin/python3
"""
    This is a script that prints the first State objects
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
    session = Session().query(State).order_by(State.id).first()
    if session is None:
        print("Nothing")
    else:
        print(f"{session.id}: {session.name}")
